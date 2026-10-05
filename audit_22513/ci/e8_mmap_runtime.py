"""
E8, bras mmap : charge un .pte par executorch.runtime (chemin -> _load_program ->
MmapDataLoader avec MlockConfig::UseMlockIgnoreErrors, extension/pybindings/pybindings.cpp:190-191),
charge une méthode et l'exécute une fois avec des entrées de uns.

Consomme : <pte> <méthode>. Produit : footprint (proc_pid_rusage, mêmes offsets que
backends/mlx/_memprofile.py) après load_program, après load_method, après execute ;
avec le patch P3, le log « MLX constants: N loaded, M copied by MLX » dit combien de
blobs MLX a copiés faute d'alignement page.
Hypothèse : macOS, pybindings construits avec EXECUTORCH_BUILD_MLX=ON.
"""
import ctypes
import ctypes.util
import os
import sys

import torch
from executorch.runtime import Runtime, Verification

_RUSAGE_INFO_V4 = 4
_OFF_PHYS_FOOTPRINT = 72
_OFF_LIFETIME_MAX_PHYS_FOOTPRINT = 240
_OFF_RESIDENT_SIZE = 64  # ri_resident_size précède ri_phys_footprint (bsd/sys/resource.h)

# ScalarType d'ExecuTorch -> torch (runtime/core/portable_type/scalar_type.h)
_DTYPES = {0: torch.uint8, 1: torch.int8, 3: torch.int32, 4: torch.int64, 5: torch.float16,
           6: torch.float32, 7: torch.float64, 11: torch.bool, 15: torch.bfloat16}


def counters():
    libc = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)
    buf = (ctypes.c_uint8 * 512)()
    if libc.proc_pid_rusage(os.getpid(), _RUSAGE_INFO_V4, ctypes.byref(buf)) != 0:
        return None
    raw = bytes(buf)
    f = lambda off: int.from_bytes(raw[off:off + 8], "little") / 2**20  # noqa: E731
    return f"rss {f(_OFF_RESIDENT_SIZE):.1f} MiB, phys_footprint {f(_OFF_PHYS_FOOTPRINT):.1f} MiB, lifetime_max {f(_OFF_LIFETIME_MAX_PHYS_FOOTPRINT):.1f} MiB"


def main():
    path, method_name = sys.argv[1], sys.argv[2]
    print("[start]", counters())
    rt = Runtime.get()
    program = rt.load_program(path, verification=Verification.Minimal)
    print("[after load_program]", counters())
    method = program.load_method(method_name)
    print("[after load_method]", counters())
    meta = method.metadata
    inputs = []
    for i in range(meta.num_inputs()):
        t = meta.input_tensor_meta(i)
        inputs.append(torch.ones(tuple(t.sizes()), dtype=_DTYPES[t.dtype()]))
        print(f"  input {i}: sizes={tuple(t.sizes())} scalar_type={t.dtype()}")
    for k in range(3):
        outs = method.execute(inputs)
        print(f"[after execute {k + 1}]", counters(), "outputs:", [tuple(o.shape) for o in outs if hasattr(o, 'shape')])


if __name__ == "__main__":
    main()
