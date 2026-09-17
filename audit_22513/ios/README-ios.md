# Mesurer sur ton iPhone (E1, E3, E6, E7 — E4 avec P2)

## Ce qu'il faut

- **Un Mac avec Xcode 26** (SDK iOS 26). Sans Mac : voir « Repli sans Mac » en bas.
- Un **Apple ID** (gratuit) : Xcode signe l'app pour ton propre appareil, valable 7 jours, sans compte développeur payant.
- L'iPhone : **Réglages → Confidentialité et sécurité → Mode développeur** activé, branché en USB, « Se fier à cet ordinateur ».
- Les `.pte` :
  - `whisper_tiny_mlx_bf16.pte` (public, 76 Mo) — `curl -L -o whisper_tiny_mlx_bf16.pte https://huggingface.co/software-mansion/react-native-executorch-whisper-tiny/resolve/v0.10.0/mlx/whisper_tiny_mlx_bf16.pte`
  - les exports de substitution à entrée fp32 : artefact **`device-ptes`** du dernier run du workflow (`AxelNoun/executorch-fork` → Actions → audit-22513-macos → run → Artifacts) : `encoder_{none,eager}_bf16_L4_tiny_fp32in.pte` (16 Mo chacun) et `encoder_{none,eager}_bf16_L12_fp32in.pte` (176 Mo chacun). `none` = attention fusionnée (SDPA), `eager` = matérialisée.
  - Le `whisper_small_mlx_int8.pte` et le `tiny_int8` du rapporteur **ne tournent pas** sur le runtime upstream (op_type 122, § 1.10 du rapport) : il faudrait le framework de son fork. Hors périmètre ici.

## Étapes (≈ 20 min)

1. Xcode → **File → New → Project → iOS → App**, nom `MemProbe`, interface SwiftUI, langage Swift. Choisis ton équipe (ton Apple ID, « Personal Team ») dans *Signing & Capabilities* ; Xcode génère un profil.
2. Remplace le contenu de `MemProbeApp.swift` par `audit_22513/ios/MemProbe/MemProbeApp.swift` et **supprime** `ContentView.swift` généré (le fichier fourni contient sa propre `ContentView`).
3. **File → Add Package Dependencies…** → URL `https://github.com/pytorch/executorch.git` → *Dependency Rule* : **Branch** `swiftpm-1.6.0.20260917` (nightly qui contient `backend_mlx` ; la liste des nightlies est sur https://ossci-ios.s3.amazonaws.com/list.html). Ajoute à la cible les produits **`executorch`** et **`backend_mlx`** (le bundle `backend_mlx_resources` avec les metallibs vient avec `backend_mlx`).
4. Cible → *Build Settings* → **Other Linker Flags** : ajoute `-all_load` (sinon le backend n'est pas enregistré : « unregistered backend », cf. `docs/source/using-executorch-ios.md`).
5. Glisse les `.pte` dans le projet (cocher *Copy items if needed* et la cible `MemProbe`). Ceux qui manquent sont simplement ignorés par l'app.
6. Sélectionne ton iPhone comme destination, **⌘R**. Au premier lancement l'iPhone demande de faire confiance au développeur (Réglages → Général → VPN et gestion de l'appareil).
7. Dans l'app : **« Lancer tous les cas »**. Chaque cas charge la méthode, l'exécute 5 fois et affiche `footprint / peak / rss` avant chargement, après chargement, après exécutions, plus les temps. Le même texte sort dans la console Xcode ; « Copier » le met dans le presse-papiers.

## Lire les résultats

- `peak` = `ledger_phys_footprint_peak` (ce que jetsam compte) ; `rss` = `resident_size` (ce que le rapporteur appelait RSS dans #22016). Le rapport prédit `rss` ≈ poids + baseline et `peak` ≫ `rss` (E1).
- `delta footprint` = pic − footprint après chargement : c'est le « +930 / +680 Mo » de l'issue, comparable entre cas.
- E3 : `tiny bf16 rapporteur — encode` (non fusionné, 235 slots) contre `tiny fusionné (substitution)` ; sur le runner macOS : 829 contre 107 Mio. `small eager` contre `small fusionné` : 724 contre 627 sur le runner (pics voisins par deux mécanismes, § 3.2).
- E7 : mets `MLX_MAX_MB_PER_BUFFER = 10` (puis `2`), **Quitter**, relancer, relancer les cas. Attendu (runner) : small fusionné 627 → 340 → 254 Mio, small eager 724 → 429 → 288, tiny bf16 rapporteur inchangé (slots, § 3.5).
- E6 : `MLX_MAX_OPS_PER_BUFFER = 20` : attendu sans effet. Sur un A18 le suffixe d'architecture est `'p'` (20 ops) par défaut — ici c'est le défaut de la machine, la variable sert surtout à mettre 40 pour comparer.
- E4 : `memory_limit_mb` n'agit que si le runtime contient P2 ; le nightly SwiftPM ne l'a pas. Pour E4 sur l'appareil, il faut des frameworks construits avec P2 (`scripts/build_apple_frameworks.sh` sur la branche `audit/22513-macos` + `git apply audit_22513/patches/P2-…`), puis un package local à la place du nightly — dis-le si tu veux ce job dans le workflow (≈ 1 h de runner).

## Ce que ça mesure, ce que ça ne mesure pas

- Le runtime est celui d'ExecuTorch **main** (1.6.0 nightly), pas 1.4.1 : le code mémoire de `MLXBackend.cpp` est identique (diff relu dans le rapport), le pin MLX diffère de 279 commits sans changement des seuils, du throttle ni du cache.
- Les entrées sont des constantes (uns / 0,1) : mémoire et temps ne dépendent pas des valeurs, le contenu des sorties n'a aucun sens.
- Le harnais n'est **pas compilé ici** (pas de Xcode sous Windows). Points où une erreur de compilation est possible et se corrige en une ligne : `BackendOptionsMap(options:)` (le doc-comment d'ExecuTorch écrit `BackendOptionsMap([...])` sans étiquette), et `task_info` / `TASK_VM_INFO` si Xcode réclame `import Darwin.Mach`.

## Repli sans Mac

AltServer (Windows, https://altstore.io) installe sur l'iPhone un `.ipa` signé avec un Apple ID gratuit, à condition qu'iTunes et iCloud (versions Apple, pas Microsoft Store) soient installés. Il faut alors un `.ipa` construit ailleurs : le workflow peut le produire sur un runner macOS (`xcodebuild -sdk iphoneos CODE_SIGNING_ALLOWED=NO`, puis `Payload/MemProbe.app` zippé). C'est plus fragile (versions d'iTunes, pairing) et je ne l'ai pas testé ; à faire seulement si aucun Mac n'est accessible.
