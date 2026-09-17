# audit_22513 — matériel de reproduction

Compagnon de `../AUDIT_22513.md`. Tout a été produit sous Windows 11, CPU seul, sans installation d'ExecuTorch : le paquet `executorch` est un module-espace de noms synthétique pointant sur un worktree git (`scripts/et_ns.py`).

## Contenu

| dossier | fichiers | rôle |
|---|---|---|
| `scripts/` | `et_ns.py` | module `executorch` synthétique (`ET_ROOT`) + `torchao` en worktree (`AO_ROOT`) ; à importer avant tout `import executorch` |
| | `exp_41_attn.py` | 4.1.1 / 4.1.3 — `torch.export` de l'encodeur HF Whisper (config small, poids aléatoires) pour `attn_implementation` ∈ {absent, sdpa, eager} ; compte les nœuds aten |
| | `exp_41_lower.py` | 4.1.3 — même encodeur lowering MLX complet à ET@1.4.1 (`to_edge_transform_and_lower` + `MLXPartitioner`), écrit un `.pte` |
| | `run_inspector.py` | lance `backends/mlx/pte_inspector.py` depuis le worktree |
| | `hist.py` | histogramme des ops par délégué / chaîne d'une sortie `--mlx-instructions` |
| | `optypes.py` | entiers `op_type` bruts par chaîne (indépendant de la table de noms) |
| | `plans.py` | ordre des `execution_plan` (méthodes) et de leurs délégués |
| | `seg_align.py` | alignement (16 Kio / 4 Kio) des segments named-data d'un `.pte` |
| | `exp_42_sizes.py` | 4.2.1 — taille de chaque intermédiaire (shape, dtype, octets) de l'encodeur HF, sdpa vs eager |
| | `sim_cbuf.py` | 4.2 — simulation du découpage en command buffers MLX et de la fenêtre `MAX_ACTIVE_TASKS` |
| `patches/` | `P1-…`, `P2-…`, `P3-…`, `P4-…`, `P2-smfork-…` | diffs unifiés contre `origin/main` (`026ca3fff3`) ; `git apply --check` passe aussi sur `v1.4.1` ; `P2-smfork` = P2 rebasé sur le `MLXBackend.cpp` du fork SM ; **tous compilés et exécutés sur les runners** (runs 4 et 5) |
| `data/` | `whisper_*_mlx_*.instr.txt` | sortie brute de `pte_inspector --mlx-instructions` sur les deux fichiers du rapporteur (table de noms ET@1.4.1 : op_type 122 = `QuantizedMatmulNode` dans le schéma du fork, affiché `ScatterAddNode`) |
| | `encoder_{none,eager}_bf16_L12.instr.txt` | idem sur mes exports de substitution (défaut = sdpa, eager) |
| | `hist_*.txt` | histogrammes correspondants |
| | `sim_cbuf.txt` | sortie de `sim_cbuf.py` |
| | `hf_pte_sha256.txt` | empreintes des deux `.pte` téléchargés |
| | `whisper_tiny_mlx_int8.instr.txt`, `hist_whisper_tiny_mlx_int8.txt` | idem pour le tiny int8 (5-6 slots temporaires, chaînes d'init : builder récent, contrairement au tiny bf16) |
| | `run3-upstream-v1.4.1/`, `run4-*`, `run5-*` | artefacts bruts des runs GitHub Actions 35187550634, 35189553833 et 35212705210 (`e*.txt`, sorties `pte_inspector`) + `TABLE.md` produit par `ci/parse_artifacts.py` ; lus dans AUDIT_22513.md § 5 bis |

## Recette (Windows, Git Bash)

```bash
# 1. worktrees en lecture seule (aucune modification du dépôt principal)
git worktree add --detach et-main origin/main          # 026ca3fff3
git worktree add --detach et-141  v1.4.1               # e4d02f41f7
git -C backends/mlx/third-party/mlx worktree add --detach mlx-141  7a1d4f5c12ac82f4b4d0a6e71538d89ca0605247
git -C backends/mlx/third-party/mlx worktree add --detach mlx-head 1f8e74e3f12f31365464a6867c6579f0e9b29d85
git -C third-party/ao worktree add --detach ao-141 $(git ls-tree v1.4.1 third-party/ao | awk '{print $3}')   # 5f2baf9d

# 2. environnement Python (torch = pin de v1.4.1 non disponible en CPU ici ; 2.14.0 = pin de main)
uv venv --python 3.12 venv
uv pip install --python venv/Scripts/python.exe torch==2.14.0 --index-url https://download.pytorch.org/whl/cpu
uv pip install --python venv/Scripts/python.exe "transformers==5.0.0rc1" safetensors numpy flatbuffers pyyaml \
    ruamel.yaml sympy tabulate pandas hydra-core omegaconf expecttest pytest pip huggingface_hub
# flatc 25.12.19 doit être dans le PATH (winget Google.flatbuffers) : exir/_serialize le cherche via FLATC_EXECUTABLE ou `flatc`

# 3. fichiers générés absents d'un checkout nu (dans le worktree et-141)
venv/Scripts/python.exe et-141/backends/mlx/serialization/generate.py       # _generated/, _generated_serializers.py, _generated_inspector.py, MLXLoader.*
cp et-141/schema/program.fbs et-141/schema/scalar_type.fbs et-141/exir/_serialize/

# 4. exécution (PYTHONIOENCODING=utf-8 évite l'erreur cp1252 sur « ≥ »)
export ET_ROOT=$PWD/et-141 AO_ROOT=$PWD/ao-141 PYTHONIOENCODING=utf-8
venv/Scripts/python.exe scripts/exp_41_attn.py 2
venv/Scripts/python.exe scripts/exp_41_lower.py none 12 bf16 out141      # puis eager 12 bf16
venv/Scripts/python.exe scripts/run_inspector.py out141/encoder_none_bf16_L12.pte --mlx-instructions > out.txt
venv/Scripts/python.exe scripts/hist.py out.txt
venv/Scripts/python.exe scripts/exp_42_sizes.py sdpa 12                  # puis eager 12
venv/Scripts/python.exe scripts/sim_cbuf.py

# 5. fichiers du rapporteur (Hugging Face, tag v0.10.0)
curl -L -o whisper_small_mlx_int8.pte https://huggingface.co/software-mansion/react-native-executorch-whisper-small/resolve/v0.10.0/mlx/whisper_small_mlx_int8.pte
curl -L -o whisper_tiny_mlx_bf16.pte  https://huggingface.co/software-mansion/react-native-executorch-whisper-tiny/resolve/v0.10.0/mlx/whisper_tiny_mlx_bf16.pte
sha256sum -c data/hf_pte_sha256.txt
venv/Scripts/python.exe scripts/run_inspector.py whisper_small_mlx_int8.pte --mlx-instructions > small.txt
venv/Scripts/python.exe scripts/hist.py small.txt ; venv/Scripts/python.exe scripts/optypes.py whisper_small_mlx_int8.pte
venv/Scripts/python.exe scripts/plans.py whisper_small_mlx_int8.pte ; venv/Scripts/python.exe scripts/seg_align.py whisper_small_mlx_int8.pte
```

Pièges rencontrés : `transformers` doit être importé **avant** que `torchao` (worktree sans métadonnées `dist-info`) soit sur `sys.path`, sinon `is_torchao_available()` échoue sur `importlib.metadata` ; `exp_41_lower.py` respecte cet ordre. Les exports utilisent des poids aléatoires (graine 0) : formes et ops de whisper-small, pas ses valeurs.

## Ce que ces scripts ne font pas

Aucune mesure mémoire en local (Windows). Les mesures viennent des runs GitHub Actions ci-dessous (`data/run*`) ; l'iPhone n'a pas été mesuré.

## `ci/` — lancer E1, E3, E6, E7, E8, E9 sans Mac : GitHub Actions

Les runners GitHub `macos-26` (arm64, macOS 26.6.2, Xcode) exposent un device Metal (« Apple Paravirtual device », géré par MLX `allocator.cpp:66-70`). ExecuTorch y exécute déjà whisper-tiny sur MLX (`.github/workflows/mlx.yml`, job `test-mlx-whisper`, `macos-14-xlarge`, ~11-12 min) et MLX y fait tourner sa suite Metal (`ml-explore/mlx`, `build_and_test.yml`, `macos-26-xlarge`).

| fichier | rôle |
|---|---|
| `ci/audit-22513-macos.yml` | workflow `workflow_dispatch` : patches P1 + P3, `install_executorch.py`, `executor_runner` avec MLX (`ET_MIN_LOG_LEVEL=Info`), téléchargement des `.pte` publics, E1 / E6 / E7 (`/usr/bin/time -l` + P1), E8 (bras mmap via `executorch.runtime`), E3 (export fusionné `export_whisper.py`, tiny par défaut), E9 (Metal), artefacts `e*.txt` |
| `ci/e8_mmap_runtime.py` | charge un `.pte` par les pybindings (`MmapDataLoader` + mlock, `pybindings.cpp:190-191`), exécute une méthode, imprime rss / footprint (offsets `rusage_info_v4` vérifiés dans `bsd/sys/resource.h`) ; avec P3, le log « MLX constants: … copied » |
| `ci/e9_nocopy.mm` | `newBufferWithBytesNoCopy` sur pointeur aligné / non aligné, longueur multiple / non multiple de page, blocs `posix_memalign(16, …)` de la taille des poids |

Ce qui a tourné : branche `audit/22513-macos` de `AxelNoun/executorch-fork` (= `v1.4.1` + `audit_22513/` + le workflow dans `.github/workflows/`), déclenchée par push (`workflow_dispatch` exige le fichier sur la branche par défaut). Runs : 35185675672 et 35186187588 (échecs de configuration : nom de répertoire `executorch` imposé par `CMakeLists.txt:456`, puis extensions `EVALUE_UTIL`/`RUNNER_UTIL` requises par `executor_runner`), **35187550634** (upstream, vert, 20 min), **35189553833** (matrice upstream + fork SM, vert, ~30 min) et **35212705210** (P2 + P4 compilés, E4, tiny int8, vert). Durées sur le runner standard : install 15 min, build `executor_runner` 3 min, mesures 1-2 min. `ci/parse_artifacts.py <dossier>` produit le tableau.

Pour relancer : pousser sur `audit/22513-*` (ajouter `[skip ci]` au message pour pousser sans relancer).

Limites : VM (GPU « Apple Paravirtual device », `air64_v27`, `recommendedMaxWorkingSetSize` 4,67 Gio, cadence GPU différente d'un iPhone) — on y valide les **mécanismes** (RSS aveugle, règles de coupe, `MLX_MAX_*`, alignement, loaders), pas les valeurs absolues de l'appareil ; E3 / E4 sur l'iPhone restent au rapporteur ; E4 sur macOS passe par P4 (`--mlx_memory_limit_mb`), qui transmet une `LoadBackendOptionsMap` à `load_method`. Le `whisper_small_mlx_int8.pte` du rapporteur ne s'exécute que sur le runtime de son fork (schéma MLX décalé) : d'où le job `sm-fork-1.4.1`.
