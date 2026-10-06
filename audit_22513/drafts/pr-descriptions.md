# Brouillons de descriptions de PR (§ 7.2 de AUDIT_22513.md)

Deux PR indépendantes contre `pytorch/executorch@main`, à ouvrir dans cet ordre. Aucune ne revendique
de mesure sur appareil. Les diffs sont dans `audit_22513/patches/` ; ils s'appliquent sur `c77d0ee6fe`.

---

## PR 1 — `P1-main-executor-runner-phys-footprint.diff`

**Titre** : `executor_runner: report the process memory counters on Apple platforms`

**Corps** :

`executor_runner` prints timings but no memory counter, so the one number that matters for a GPU
backend on Apple platforms — physical footprint — cannot be obtained from the repo's own runner.

(Measured example of why it matters: on `main`, `whisper_tiny_mlx_bf16.pte` `encode` peaks at 571 MiB of
footprint in a process whose max RSS is 50 MiB.)

That gap is what made pytorch/executorch#22513 hard to read: the report compared whole-process RSS on
macOS against `phys_footprint` on iOS. RSS counts the pages the CPU touched; `phys_footprint` adds the
IOKit mappings, which is where Metal buffers live (`xnu/osfmk/kern/task.c`, `ledger_phys_footprint`),
and it is what jetsam charges. The backend's own export-side profiler already documents the same
distinction (`backends/mlx/_memprofile.py`: a 16 GB export peaked at 65 GB footprint against 37 GB RSS).

This adds, under `#ifdef __APPLE__`, one `proc_pid_rusage(RUSAGE_INFO_V4)` helper and two call sites —
after `load_method` and after the execution loop — logging `resident_size`, `phys_footprint` and
`lifetime_max_phys_footprint`. Nothing changes on other platforms (the helper compiles to a no-op) and
nothing changes when the log level hides `Info`.

Measured on a GitHub `macos-26` runner with the MLX delegate, whisper-small `encode`: `maximum resident
set size` 127 MiB, `peak memory footprint` 905 MiB, same process. The new log line gives the second
number without `/usr/bin/time -l`, and gives it per phase.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

---

## PR 2 — `P6-main-executor-runner-mlx-eval-threshold.diff`

**Titre** : `executor_runner: let the MLX eval threshold and cache interval be set`

**Corps** :

#22932 added `eval_threshold_bytes` to the MLX backend: past N bytes of accumulated intermediates, the
interpreter evaluates the live per-execution tensors, which bounds the peak of a lazily built method.
It is a per-model runtime spec and it defaults to 0 (disabled), so it only does anything when a caller
sets it through a `LoadBackendOptionsMap`.

No runner in the repo sets it. The result is that the fix cannot be measured, tuned, or regression-tested
with the repo's own tools — the numbers in #22932 and #22513 all come from out-of-tree harnesses.

This adds two flags to `executor_runner`, both routed through `LoadBackendOptionsMap` and both leaving
the backend default when absent:

- `--mlx_eval_threshold_bytes` (`eval_threshold_bytes`)
- `--mlx_clear_cache_interval` (`clear_cache_interval`, which several example runners set in code but which no runner exposes as a flag)

With P1's counters this makes the whole curve reproducible from the repo:

```
executor_runner --model_path encoder.pte --method_name encode --num_executions 5 \
    --mlx_eval_threshold_bytes 536870912
```

🤖 Generated with [Claude Code](https://claude.com/claude-code)

---

## Avant d'ouvrir

- Le test reste à écrire pour la PR 2. La lecture de la clé est déjà couverte en amont par
  `backends/mlx/test/mlx_eval_threshold_test.cpp` (sa ligne 152 vérifie le défaut 0) ; ce qui ne l'est pas,
  c'est le chemin `executor_runner` → `LoadBackendOptionsMap` → `init()`, et c'est lui que le test doit couvrir.
- Vérifier que les deux diffs s'appliquent encore sur le `main` du jour (`git apply --check`).
- Les deux PR touchent `examples/portable/executor_runner/executor_runner.cpp` : la seconde sera à
  rebaser sur la première si elles ne sont pas mergées dans l'ordre.
