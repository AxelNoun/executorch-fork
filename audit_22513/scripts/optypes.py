"""Compte les op_type bruts (entiers du union OpNode) par délégué/chaîne d'un .pte MLX."""
import sys, collections, et_ns  # noqa: F401
from executorch.backends.mlx import pte_inspector as pi
data = open(sys.argv[1], "rb").read()
dels = pi._find_mlx_delegates(data)
for idx, _ in enumerate(dels):
    mlx = pi._load_mlx_payload(data, delegate_index=idx)
    g = pi.parse_mlx_flatbuffer(mlx.fb_data)
    for ch in g["instruction_chains"]:
        c = collections.Counter((i["op_type"], i.get("op_name")) for i in ch["instructions"])
        print(f"D{idx} chain{ch['chain_index']}: " + ", ".join(f"{t}:{n}={v}" for (t, n), v in sorted(c.items())))
