| fichier | peak RSS (Mio) | peak footprint (Mio) | lifetime_max après load (Mio) | lifetime_max après exécution (Mio) | constantes copiées par MLX | ms 1re / régime établi | statut |
|---|---|---|---|---|---|---|---|
| e1_small_decode.txt | 213 | 216 | 212 | – | 0/533 (0.0 Mio) | – | ÉCHEC |
| e1_small_encode.txt | 113 | 107 | 106 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e1_tiny_encode.txt | 43 | 829 | 24 | 829 | 0/83 (0.0 Mio) | 3971 / 58 | OK |
| e3_fused_encoder.txt | 37 | 107 | 21 | 107 | 0/71 (0.0 Mio) | 657 / 28 | OK |
| e6_fused_encoder.txt | 38 | 108 | 21 | 107 | 0/71 (0.0 Mio) | 395 / 28 | OK |
| e6_small_encode.txt | 113 | 108 | 106 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e7_fused_encoder.txt | 37 | 107 | 21 | 107 | 0/71 (0.0 Mio) | 398 / 28 | OK |
| e7_small_encode.txt | 113 | 107 | 105 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e7_tiny_encode.txt | 47 | 831 | 24 | 830 | 0/83 (0.0 Mio) | 878 / 52 | OK |

### e2_counts.txt
```
fused encoder: SdpaNode=4 SoftmaxNode=0
reporter tiny (2 delegates): SdpaNode=8 SoftmaxNode=4
```

### e9.txt
```
device=Apple Paravirtual device architecture=air64_v27 page=16384 recommendedMaxWorkingSetSize=5010800640 hasUnifiedMemory=1
vm_allocate: ptr page-aligned, len page-multiple         ptr%page=0      len%page=0      -> buffer  contents==ptr:yes  length=1048576
vm_allocate: ptr page-aligned, len NOT page-multiple     ptr%page=0      len%page=16284  -> buffer  contents==ptr:yes  length=1048476
vm_allocate: ptr + 4096 (4 KiB, pas 16 KiB)              ptr%page=4096   len%page=12288  -> buffer  contents==ptr:yes  length=1044480
vm_allocate: ptr + 128 (offset d'un segment .pte)        ptr%page=128    len%page=16256  -> buffer  contents==ptr:yes  length=1048448
posix_memalign(16, 1179648 = 72 pages) q_proj bf16       ptr%page=0      len%page=0      -> buffer  contents==ptr:yes  length=1179648
posix_memalign(16, 2304000) embed_positions bf16         ptr%page=0      len%page=10240  -> buffer  contents==ptr:yes  length=2304000
posix_memalign(16, 1536) biais (zone small)              ptr%page=0      len%page=1536   -> buffer  contents==ptr:yes  length=1536
posix_memalign(16, 20480) > 15 KiB iOS, < 32 KiB macOS   ptr%page=0      len%page=4096   -> buffer  contents==ptr:yes  length=20480
```

### e8_small_encode_mmap.txt
```
[MLXExecutor.h:848] MLX constants: 364 loaded, 0 copied by MLX (0 bytes resident twice)
[MLXBackend.cpp:497] MLX execute failed: [scatter_add_axis] Received invalid axis for array with 3 dimensions.
[method.cpp:1530] CALL_DELEGATE execute failed at instruction 0: 0x1
[start] rss 328.4 MiB, phys_footprint 270.3 MiB, lifetime_max 270.8 MiB
[after load_program] rss 335.0 MiB, phys_footprint 276.5 MiB, lifetime_max 276.5 MiB
[after load_method] rss 434.8 MiB, phys_footprint 281.5 MiB, lifetime_max 281.5 MiB
  input 0: sizes=(480000,) scalar_type=6
```

### e8_tiny_encode_mmap.txt
```
[MLXExecutor.h:848] MLX constants: 83 loaded, 0 copied by MLX (0 bytes resident twice)
[start] rss 328.3 MiB, phys_footprint 270.1 MiB, lifetime_max 270.9 MiB
[after load_program] rss 332.5 MiB, phys_footprint 274.2 MiB, lifetime_max 274.3 MiB
[after load_method] rss 355.0 MiB, phys_footprint 275.1 MiB, lifetime_max 275.4 MiB
  input 0: sizes=(480000,) scalar_type=6
[after execute 1] rss 366.3 MiB, phys_footprint 1076.4 MiB, lifetime_max 1076.4 MiB outputs: [(1, 1500, 384)]
[after execute 2] rss 368.9 MiB, phys_footprint 1077.4 MiB, lifetime_max 1079.6 MiB outputs: [(1, 1500, 384)]
[after execute 3] rss 371.3 MiB, phys_footprint 1077.5 MiB, lifetime_max 1079.8 MiB outputs: [(1, 1500, 384)]
```
