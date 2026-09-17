// MemProbe — harnais iOS pour AUDIT_22513.md (E1, E3, E6, E7, E4 sur l'appareil).
//
// Un seul fichier. Projet Xcode « App » SwiftUI vierge + dépendance SwiftPM
// https://github.com/pytorch/executorch.git, branche swiftpm-1.6.0.20260917
// (produits « executorch » et « backend_mlx »), + « -all_load » dans Other Linker Flags.
// Les .pte sont ajoutés au bundle de l'app (voir README-ios.md).
//
// Mesure : task_info(TASK_VM_INFO) — phys_footprint, ledger_phys_footprint_peak, resident_size.
// C'est la métrique du jetsam ; resident_size est ce que le rapporteur appelait RSS.
//
// Deux familles de réglages :
// - variables d'environnement MLX (MLX_MAX_MB_PER_BUFFER, MLX_MAX_OPS_PER_BUFFER) : lues une
//   fois à la création du device Metal, donc posées AU LANCEMENT depuis UserDefaults ;
//   changer de réglage = relancer l'app (bouton « Quitter »).
// - options de backend (memory_limit_mb, cache_limit_mb) : transmises à load(method, options:) ;
//   effectives seulement si le runtime contient le patch P2 (pas dans le nightly SwiftPM).

import SwiftUI
import ExecuTorch
import Darwin

// MARK: - Mémoire

struct MemStats {
  let footprint: UInt64   // phys_footprint (Mio)
  let peak: UInt64        // ledger_phys_footprint_peak (Mio)
  let resident: UInt64    // resident_size (Mio)

  static func now() -> MemStats {
    var info = task_vm_info_data_t()
    var count = mach_msg_type_number_t(MemoryLayout<task_vm_info_data_t>.size / MemoryLayout<natural_t>.size)
    let kr = withUnsafeMutablePointer(to: &info) {
      $0.withMemoryRebound(to: integer_t.self, capacity: Int(count)) {
        task_info(mach_task_self_, task_flavor_t(TASK_VM_INFO), $0, &count)
      }
    }
    guard kr == KERN_SUCCESS else { return MemStats(footprint: 0, peak: 0, resident: 0) }
    let mib: UInt64 = 1 << 20
    return MemStats(
      footprint: UInt64(info.phys_footprint) / mib,
      peak: UInt64(max(0, info.ledger_phys_footprint_peak)) / mib,
      resident: UInt64(info.resident_size) / mib)
  }

  var line: String { "footprint \(footprint) Mio, peak \(peak), rss \(resident)" }
}

// MARK: - Cas de mesure

struct ProbeCase: Identifiable, Hashable {
  let id: String
  let file: String          // nom du .pte dans le bundle, sans extension
  let method: String
  let kind: InputKind
  enum InputKind: Hashable { case audio480k, mel3000, decodeTiny, decodeSmall }

  func inputs() -> [ValueConvertible] {
    switch kind {
    case .audio480k:
      return [Tensor<Float>([Float](repeating: 1, count: 480_000), shape: [480_000])]
    case .mel3000:
      return [Tensor<Float>([Float](repeating: 0.1, count: 80 * 3000), shape: [1, 80, 3000])]
    case .decodeTiny:
      return [Tensor<Int64>([0], shape: [1, 1]), Tensor<Int64>([0], shape: [1]),
              Tensor<Float>([Float](repeating: 0.1, count: 1500 * 384), shape: [1, 1500, 384])]
    case .decodeSmall:
      return [Tensor<Int64>([0], shape: [1, 1]), Tensor<Int64>([0], shape: [1]),
              Tensor<Float>([Float](repeating: 0.1, count: 1500 * 768), shape: [1, 1500, 768])]
    }
  }
}

// Fichiers attendus dans le bundle (ceux qui manquent sont ignorés).
let allCases: [ProbeCase] = [
  // fichiers publics du rapporteur (runtime upstream : tiny bf16 seulement ; small/int8 exigent son fork)
  ProbeCase(id: "tiny bf16 rapporteur — encode (non fusionné, 235 slots)", file: "whisper_tiny_mlx_bf16", method: "encode", kind: .audio480k),
  ProbeCase(id: "tiny bf16 rapporteur — decode", file: "whisper_tiny_mlx_bf16", method: "decode", kind: .decodeTiny),
  // exports de substitution du workflow (poids aléatoires, entrée fp32, mel [1,80,3000])
  ProbeCase(id: "tiny fusionné (substitution) — forward", file: "encoder_none_bf16_L4_tiny_fp32in", method: "forward", kind: .mel3000),
  ProbeCase(id: "tiny eager (substitution) — forward", file: "encoder_eager_bf16_L4_tiny_fp32in", method: "forward", kind: .mel3000),
  ProbeCase(id: "small fusionné (substitution) — forward", file: "encoder_none_bf16_L12_fp32in", method: "forward", kind: .mel3000),
  ProbeCase(id: "small eager (substitution) — forward", file: "encoder_eager_bf16_L12_fp32in", method: "forward", kind: .mel3000),
]

// MARK: - Exécution d'un cas

func runCase(_ c: ProbeCase, iterations: Int, memoryLimitMb: Int, cacheLimitMb: Int) -> String {
  guard let path = Bundle.main.path(forResource: c.file, ofType: "pte") else {
    return "\(c.id)\n  fichier \(c.file).pte absent du bundle"
  }
  var out = "\(c.id)\n"
  let module = Module(filePath: path)   // FileDataLoader par défaut, comme executor_runner
  let before = MemStats.now()
  do {
    var options: [BackendOption] = []
    if memoryLimitMb >= 0 { options.append(BackendOption("memory_limit_mb", memoryLimitMb)) }
    if cacheLimitMb >= 0 { options.append(BackendOption("cache_limit_mb", cacheLimitMb)) }
    if options.isEmpty {
      try module.load(c.method)
    } else {
      // Sans P2 dans le runtime, ces clés sont ignorées silencieusement.
      let map = try BackendOptionsMap(options: ["MLXBackend": options])
      try module.load(c.method, options: map)
    }
    let afterLoad = MemStats.now()
    out += "  avant load: \(before.line)\n  après load: \(afterLoad.line)\n"
    var times: [Double] = []
    for _ in 0..<iterations {
      let t0 = Date()
      let inputs = c.inputs()
      _ = try module.execute(c.method, inputs)
      times.append(Date().timeIntervalSince(t0) * 1000)
    }
    let afterExec = MemStats.now()
    let steady = times.count > 1 ? times[1...].sorted()[(times.count - 1) / 2] : times[0]
    out += "  après \(iterations) exécutions: \(afterExec.line)\n"
    out += String(format: "  delta footprint (pic − après load): %d Mio ; 1re exécution %.0f ms, régime établi %.0f ms\n",
                  Int(afterExec.peak) - Int(afterLoad.footprint), times[0], steady)
  } catch {
    out += "  ERREUR: \(error)\n"
  }
  return out
}

// MARK: - Interface

@main
struct MemProbeApp: App {
  init() {
    // Variables MLX : à poser avant toute utilisation de Metal par MLX (lues une fois).
    let d = UserDefaults.standard
    for key in ["MLX_MAX_MB_PER_BUFFER", "MLX_MAX_OPS_PER_BUFFER"] {
      if let v = d.string(forKey: key), !v.isEmpty { setenv(key, v, 1) } else { unsetenv(key) }
    }
  }
  var body: some Scene { WindowGroup { ContentView() } }
}

struct ContentView: View {
  @AppStorage("MLX_MAX_MB_PER_BUFFER") private var maxMb = ""
  @AppStorage("MLX_MAX_OPS_PER_BUFFER") private var maxOps = ""
  @AppStorage("memory_limit_mb") private var memoryLimit = -1
  @AppStorage("cache_limit_mb") private var cacheLimit = -1
  @State private var log = "Réglages MLX actifs (au lancement) : MLX_MAX_MB_PER_BUFFER=\(getenv("MLX_MAX_MB_PER_BUFFER").map { String(cString: $0) } ?? "-") MLX_MAX_OPS_PER_BUFFER=\(getenv("MLX_MAX_OPS_PER_BUFFER").map { String(cString: $0) } ?? "-")\n"
  @State private var running = false

  var body: some View {
    NavigationStack {
      VStack(alignment: .leading, spacing: 8) {
        Group {
          HStack { Text("MLX_MAX_MB_PER_BUFFER"); TextField("défaut", text: $maxMb).keyboardType(.numberPad) }
          HStack { Text("MLX_MAX_OPS_PER_BUFFER"); TextField("défaut", text: $maxOps).keyboardType(.numberPad) }
          Text("(variables lues au lancement : modifier puis « Quitter » et relancer)").font(.caption)
          HStack { Text("memory_limit_mb (P2)"); TextField("-1", value: $memoryLimit, format: .number).keyboardType(.numberPad) }
          HStack { Text("cache_limit_mb (P2)"); TextField("-1", value: $cacheLimit, format: .number).keyboardType(.numberPad) }
        }.font(.footnote)
        HStack {
          Button(running ? "En cours…" : "Lancer tous les cas") { runAll() }.disabled(running)
          Button("Quitter") { exit(0) }
          Button("Copier") { UIPasteboard.general.string = log }
        }
        ScrollView { Text(log).font(.system(size: 11, design: .monospaced)).frame(maxWidth: .infinity, alignment: .leading) }
      }
      .padding()
      .navigationTitle("MemProbe #22513")
    }
  }

  func runAll() {
    running = true
    let memLim = memoryLimit, cacheLim = cacheLimit
    DispatchQueue.global(qos: .userInitiated).async {
      var text = ""
      for c in allCases {
        let r = runCase(c, iterations: 5, memoryLimitMb: memLim, cacheLimitMb: cacheLim)
        print(r)          // console Xcode
        text += r + "\n"
        DispatchQueue.main.async { log += r + "\n" }
      }
      DispatchQueue.main.async { running = false }
      _ = text
    }
  }
}
