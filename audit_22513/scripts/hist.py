"""Histogramme des ops MLX par délégué et par chaîne, à partir de la sortie --mlx-instructions."""
import sys, re, collections
cur = None; chain = None; hist = collections.defaultdict(collections.Counter); ninstr = {}
for line in open(sys.argv[1], encoding="utf-8", errors="replace"):
    m = re.match(r"^MLX DELEGATE (\d+)", line)
    if m: cur = int(m.group(1)); continue
    if line.startswith("MLX Graph Summary"): cur = 0; continue
    if line.startswith("Named Slots:") or line.startswith("Inputs:"): chain = None; continue
    m = re.match(r"^Chain (\d+)(.*)\((\d+) instructions\)", line)
    if m: chain = f"D{cur} chain{m.group(1)}{m.group(2).strip()}"; ninstr[chain] = int(m.group(3)); continue
    m = re.match(r"^  \[\d+\] (\S+)", line)
    if m and chain: hist[chain][m.group(1)] += 1
for chain, c in hist.items():
    print(f"\n{chain} ({ninstr[chain]} instr): " + ", ".join(f"{k}={v}" for k, v in c.most_common()))
