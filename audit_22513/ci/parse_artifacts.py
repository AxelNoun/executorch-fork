"""
Dépouille les artefacts e*.txt du workflow audit-22513-macos en un tableau Markdown.

Consomme : un répertoire d'artefacts (sorties de /usr/bin/time -l + logs P1/P3, e8_*.txt, e9.txt, e2_counts.txt).
Produit  : tableau Markdown sur stdout (Mio, 1 Mio = 2^20 octets ; /usr/bin/time -l donne des octets).
Hypothèse : format de /usr/bin/time -l de macOS 26 (« maximum resident set size », « peak memory footprint »).
"""
import re
import sys
from pathlib import Path

MIB = 2**20


def grab(text, label):
    m = re.search(r"^\s*(\d+)\s+" + re.escape(label), text, re.M)
    return int(m.group(1)) / MIB if m else None


def p1(text, stage):
    m = re.search(r"\[" + re.escape(stage) + r"\] rss ([\d.]+) MiB, phys_footprint ([\d.]+) MiB, lifetime_max_phys_footprint ([\d.]+) MiB", text)
    return tuple(float(x) for x in m.groups()) if m else None


def p3(text):
    m = re.search(r"MLX constants: (\d+) loaded, (\d+) copied by MLX \((\d+) bytes resident twice\)", text)
    return (int(m.group(1)), int(m.group(2)), int(m.group(3)) / MIB) if m else None


def fmt(x):
    return "–" if x is None else f"{x:.0f}"


def main(d):
    d = Path(d)
    rows = []
    for f in sorted(d.glob("e*.txt")):
        if f.name.startswith(("e8_", "e9", "e2_", "e3_inspector")) or f.name.endswith(".instr.txt"):
            continue
        t = f.read_text(errors="replace")
        rss = grab(t, "maximum resident set size")
        fp = grab(t, "peak memory footprint")
        after_load = p1(t, "after load_method")
        after_exec = p1(t, "after execute loop")
        cst = p3(t)
        iters = [float(x) for x in re.findall(r"Iteration \d+ of \d+: ([\d.]+) ms", t)]
        # 1re itération = compilation des noyaux Metal ; régime établi = médiane des suivantes
        steady = sorted(iters[1:])[len(iters[1:]) // 2] if len(iters) > 1 else None
        ms = f"{iters[0]:.0f} / {steady:.0f}" if steady is not None else ("–" if not iters else f"{iters[0]:.0f} / –")
        err = "OK" if "Model executed successfully" in t else ("ÉCHEC" if re.search(r"failed|Error|error", t) else "?")
        rows.append((f.name, rss, fp,
                     after_load[2] if after_load else None, after_exec[2] if after_exec else None,
                     f"{cst[1]}/{cst[0]} ({cst[2]:.1f} Mio)" if cst else "–", ms, err))
    print("| fichier | peak RSS (Mio) | peak footprint (Mio) | lifetime_max après load (Mio) | lifetime_max après exécution (Mio) | constantes copiées par MLX | ms 1re / régime établi | statut |")
    print("|---|---|---|---|---|---|---|---|")
    for r in rows:
        print("| " + " | ".join([r[0], fmt(r[1]), fmt(r[2]), fmt(r[3]), fmt(r[4]), r[5], r[6], r[7]]) + " |")
    for name in ("e2_counts.txt", "e9.txt"):
        f = d / name
        if f.exists():
            print(f"\n### {name}\n```\n{f.read_text(errors='replace').strip()}\n```")
    for f in sorted(d.glob("e8_*.txt")):
        t = f.read_text(errors="replace")
        keep = [l for l in t.splitlines() if l.startswith("[") or "MLX constants" in l or "input " in l]
        print(f"\n### {f.name}\n```\n" + "\n".join(keep) + "\n```")


if __name__ == "__main__":
    main(sys.argv[1])
