# Brouillon de commentaire — pytorch/executorch#22513 (close)

> **DÉCISION (2026-10-06) : ne pas poster sur #22513.** Le fil est clos, le correctif est du rapporteur,
> et ce qui resterait à dire n'a pas sa place dans une issue de runtime :
>
> - La « confirmation » que `#22932` + `#23109` aident ses fichiers publiés n'apprend rien d'actionnable :
>   il a mesuré le mécanisme sur iPhone 16, et la mise à jour du runtime le lui donnera sans qu'on le lui dise.
> - Le schema shift (op_type 122) est une divergence délibérée de son fork, qu'il connaît.
> - Le **seul** fait réellement nouveau est que le `tiny` qu'il a mesuré dans `#22932` (550,4 Mo de pic)
>   n'est pas celui qu'il publie (869,9 Mo décimaux, soit 829,6 Mio) : ses artefacts HF sortent d'un pipeline
>   plus ancien que ses exports de test. C'est une observation sur un produit, donc pour
>   `software-mansion/react-native-executorch`, pas pour une issue ExecuTorch close.
>
> Le texte est conservé ci-dessous comme trace de ce qui aurait été dit et de ce qui l'appuie.

---

Late to this, but I had been auditing the issue in parallel on GitHub `macos-26` runners and ended up with
two numbers that may be worth recording, both about the **published `.pte` files** rather than the runtime.

**#22932 + #23109 also help the published Whisper files, not just gemma4-e2b.** `whisper_tiny_mlx_bf16.pte`,
`encode`, 5 executions, `/usr/bin/time -l`, same binary throughout:

| runtime | peak footprint |
| --- | --- |
| v1.4.1 | 829.6 MiB |
| `main` @ `c77d0ee6fe`, no option set | **571 MiB** |
| `main`, `eval_threshold_bytes` = 256 MB | 263 MiB |
| `main`, `eval_threshold_bytes` = 64 MB | 232 MiB (53 → 91 ms) |

That file is one of the "one slot per instruction" plans #23109 targets — `pte_inspector --mlx-instructions`
reports 198 temp tensors for its `encode` chain and 235 for `decode`, against 5 and 6 for both int8 files —
so the release path does most of the work before the threshold is even set.

One side note from the same runs: neither `whisper_small_mlx_int8.pte` nor `whisper_tiny_mlx_int8.pte` loads
on `main` — `[scatter_add_axis] Axis 150 is out of bounds for array with 3 dimensions`, which is the op_type
122 shift between your fork's `OpNode` union (`CumMaxNode` inserted at 112) and upstream's. Worth knowing if
anyone moves the RN package to the upstream runtime.

**Caveats**: all of this is on a paravirtualised Metal device (`air64_v27`, `is_nax_available()` false), never
on a device, so the mechanisms carry over but the absolute numbers are not an A18's.

Reproduction workflow and raw outputs: <lien vers audit_22513/ci/audit-22513-macos.yml et les artefacts>.

---

## Point 2 — à poser plutôt sur software-mansion/react-native-executorch

The encoder in the published files is exported without attention fusion, which no runtime fix changes:
`encode` has 0 `SdpaNode` / 12 `SoftmaxNode` in `whisper_small_mlx_int8.pte` and 0 / 4 in
`whisper_tiny_mlx_bf16.pte`, while the matching `decode` chains have 24 and 8 `SdpaNode`. The per-layer
sequence (instructions 52-60, leaving aside the two `AsType` that cast the scale constants: Multiply,
Multiply, Transpose, Addmm, AsType→fp32, Softmax, AsType→bf16, Addmm) matches the non-SDPA branch of
`openai/whisper` (`whisper/model.py:137-143` at `86098128c0`) term for term, materialising four
`[1, 12, 1500, 1500]` tensors per layer, two of them fp32.

At constant exporter and builder, fusing is worth ÷2.2 on activations at tiny size (194.3 → 86.8 MiB,
34.9 → 27.8 ms) and −13 % on peak at small size (725.9 → 628.8 MiB). Is `MultiHeadAttention.use_sdpa` false
when the encoder is traced?

---

## Notes de rédaction (à retirer avant publication)

- Ne rien reprendre de ce qu'il a établi lui-même : RSS contre `phys_footprint`, paresse de MLX, rétention de
  slots. Les trois sont dans le fil ou dans les corps de `#22932` et `#23109`, avec des mesures sur appareil.
- Ne pas écrire « votre correctif ne couvre pas … » : E13 montre le contraire.
- Vérifier avant de poster : le lien vers le workflow pointe un dépôt public (`AxelNoun/executorch-fork` l'est) ;
  les numéros de ligne `openai/whisper` sont ceux de `data/openai_whisper_citations.txt`.
- Les chiffres cités viennent de `data/run10-upstream-main/` (E13) et `data/run7-upstream-v1.4.1/` (substituts).
