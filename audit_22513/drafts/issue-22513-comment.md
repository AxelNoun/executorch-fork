# Brouillon de commentaire sur pytorch/executorch#22513 (close)

Statut : **en attente de E13** (run sur `main` avec `#22932` + `#23109`). Le point 1 ci-dessous est écrit
à partir des mesures sur le fork à jour (`3cdb8744ad`) ; si E13 montre que `main` corrige aussi le fichier
bf16, le point 1 devient « vérifié, plus rien à signaler » et le commentaire se réduit aux points 2 et 3.
Ne pas poster avant d'avoir tranché — voir § 7.1 de `AUDIT_22513.md`.

---

Thanks for closing the loop on this, and for posting the device numbers — the RSS vs `phys_footprint`
correction in particular saves anyone else from chasing a platform gap that isn't there.

I had been auditing this issue in parallel, on GitHub `macos-26` runners (paravirtualised GPU, so
mechanisms only — no device). Two things came out of it that #22932 does not cover. Both are about the
**published `.pte` files**, not about the runtime.

**1. `whisper_tiny_mlx_bf16.pte` does not benefit from the bounded graph.**

Running your three public files on your own fork at `3cdb8744ad` (which carries `713fa6050c` and
`7ac1e14ff0`), `encode`, 5 executions, `/usr/bin/time -l`:

| file | peak footprint, fork @ 7ba02ad0bb (17 Sep) | peak footprint, fork @ 3cdb8744ad (5 Oct) |
| --- | --- | --- |
| `whisper_small_mlx_int8.pte` | 905 MiB | **396 MiB** |
| `whisper_tiny_mlx_int8.pte` | 556 MiB | **358 MiB** |
| `whisper_tiny_mlx_bf16.pte` | 828 MiB | **827 MiB** |

The bf16 file is the only one that does not move, and it does not move under any back-pressure:
`MLX_MAX_MB_PER_BUFFER=10` leaves it at 830 MiB, and a 400 MB MLX memory limit leaves it at 820 MiB
while costing 55 → 249 ms — the throttle waits and nothing is freed.

The reason is on the AOT side. `pte_inspector … --mlx-instructions` reports **198 temp tensors** for its
`encode` chain and 235 for `decode`, against **5** and **6** for both int8 files. With one slot per
instruction, `ExecutionState::tensors` holds a reference to every intermediate until `state.reset()`,
so an evaluation barrier has nothing to release: the peak is the method's whole volume no matter when
you evaluate. Your "slot retention … ruled out" measurement was on `small int8`, which already had 7
slots — there was nothing there to recover.

For comparison, at the same architecture (whisper-tiny, 4 layers, d=384, 6 heads), bf16, same binary,
an encoder exported with the current pipeline peaks at **215.7 MiB** with materialised attention and
**108.2 MiB** with SDPA, against 829.6 MiB for the published file. That last gap is not a clean
measurement of slot reuse — the two files also differ in softmax dtype and in how many score-sized
tensors they materialise (four, two of them fp32, against two in bf16). What *is* clean is the
behaviour: back-pressure moves the current export (215.7 → 105-162 MiB under a 60 MB MLX memory limit,
run to run) and moves the published file by nothing.

If the withdrawn `whisper_small_mlx_bf16.pte` came out of the same builder, that is the most economical
explanation for the 3.80 GB jetsam: its total volume is ~4.9 GB, so the process dies before any barrier
can help. One line settles it, and only you can run it:

```
python -m executorch.backends.mlx.pte_inspector whisper_small_mlx_bf16.pte --mlx-instructions | grep "Temp tensors"
```

If it prints hundreds, the fix for those files is a re-export, not a runtime update.

**2. The published encoder is exported without attention fusion.**

`encode` in `whisper_small_mlx_int8.pte` has **0 `SdpaNode` and 12 `SoftmaxNode`**; `whisper_tiny_mlx_bf16.pte`
has 0 and 4. The corresponding `decode` chains have 24 and 8 `SdpaNode`, so the decoder is fused and the
encoder is not. The per-layer sequence (instructions 52-60: Multiply, Multiply, Transpose, Addmm,
AsType→fp32, Softmax, AsType→bf16, Addmm) matches the non-SDPA branch of `openai/whisper`
(`whisper/model.py:137-143` at `86098128c0`) term for term, which materialises four `[1, 12, 1500, 1500]`
tensors per layer — 324 MB per layer, ~3.9 GB of cumulative allocation per `encode` call.

At constant builder and architecture, fusing is worth ×2.2 on activations and −20 % on time at tiny size
(194.3 → 86.8 MiB, 34.9 → 27.8 ms). I can't tell from the file what disables it — is
`MultiHeadAttention.use_sdpa` false when the encoder is traced?

**3. Caveats on the numbers above.** All of them come from GitHub `macos-26` runners: the Metal device is
`Apple Paravirtual device` (`air64_v27`), where `is_nax_available()` is false, so kernel selection is not
an A18's. No measurement of mine is from a device. The substitute exports use random weights (shapes and
ops of whisper-{tiny,small}, not their values). Your `small int8` only runs on your fork's runtime and on
current `main`.

Reproduction workflow and raw outputs: <lien vers audit_22513/ci/audit-22513-macos.yml et les artefacts>.

---

## Notes de rédaction (à retirer avant publication)

- Ne pas reprendre RSS vs `phys_footprint` ni la paresse de MLX : il les a établis lui-même, avec des
  mesures sur appareil. Les citer comme acquis, pas comme apport.
- Ne pas écrire « le titre de l'issue est faux » : il l'a corrigé de lui-même dans le fil.
- Vérifier avant de poster : que le lien vers le workflow pointe un dépôt public (`AxelNoun/executorch-fork`
  l'est), et que les numéros de ligne `openai/whisper` sont encore ceux du commit cité
  (`data/openai_whisper_citations.txt`).
- Si E13 montre que `main` ramène le bf16 sous 300 MiB, remplacer le point 1 par une phrase : « sur `main`,
  `#23109` couvre aussi les fichiers sans recyclage AOT — rien à signaler », et garder le point 2.
