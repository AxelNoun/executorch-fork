"""Alignement des segments named-data d'un .pte : offset absolu dans le fichier modulo 16 Ko / 4 Ko."""
import sys, json, collections, et_ns  # noqa: F401
from executorch.exir._serialize._program import _get_extended_header  # type: ignore
from executorch.exir._serialize._flatbuffer import _program_flatbuffer_to_json
data = open(sys.argv[1], "rb").read()
eh = _get_extended_header(data)
prog = json.loads(_program_flatbuffer_to_json(data))
segs = prog["segments"]; named = prog.get("named_data") or []
base = eh.segment_base_offset
print(f"file={len(data)} program_size={eh.program_size} segment_base_offset={base} (base%16384={base%16384}) segments={len(segs)} named_data={len(named)}")
mods16k = collections.Counter(); mods4k = collections.Counter(); sizes = []
for nd in named:
    s = segs[nd["segment_index"]]; abs_off = base + s["offset"]
    mods16k[abs_off % 16384 == 0] += 1; mods4k[abs_off % 4096 == 0] += 1; sizes.append(s["size"])
print("named blobs page-aligned (16 KiB):", dict(mods16k), " (4 KiB):", dict(mods4k))
print("delegate segments:", [ (s["offset"], s["size"]) for s in segs[:2] ], "...")
sizes.sort(); print(f"blob sizes: min={sizes[0]} median={sizes[len(sizes)//2]} max={sizes[-1]} n>32KiB={sum(x>32768 for x in sizes)} n>8MiB={sum(x>8<<20 for x in sizes)}")
for nd in named[:6]:
    s = segs[nd["segment_index"]]; print(f"  {nd['key'][:50]:50s} off={base+s['offset']} size={s['size']} off%128={(base+s['offset'])%128} off%16384={(base+s['offset'])%16384}")
