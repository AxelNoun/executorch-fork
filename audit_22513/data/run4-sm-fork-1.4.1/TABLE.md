| fichier | peak RSS (Mio) | peak footprint (Mio) | lifetime_max après load (Mio) | lifetime_max après exécution (Mio) | constantes copiées par MLX | ms 1re / régime établi | statut |
|---|---|---|---|---|---|---|---|
| e1_small_decode.txt | 219 | 281 | 212 | 281 | 0/533 (0.0 Mio) | 440 / 46 | OK |
| e1_small_encode.txt | 127 | 905 | 105 | 905 | 0/364 (0.0 Mio) | 2883 / 454 | OK |
| e1_sub_small_eager.txt | 197 | 724 | 176 | 724 | 0/211 (0.0 Mio) | 990 / 277 | OK |
| e1_sub_small_none.txt | 193 | 627 | 176 | 627 | 0/199 (0.0 Mio) | 689 / 230 | OK |
| e1_tiny_decode.txt | 79 | 84 | 67 | 84 | 0/100 (0.0 Mio) | 485 / 7 | OK |
| e1_tiny_encode.txt | 45 | 828 | 24 | 828 | 0/83 (0.0 Mio) | 1088 / 98 | OK |
| e3_fused_encoder.txt | 37 | 108 | 21 | 108 | 0/71 (0.0 Mio) | 689 / 28 | OK |
| e6_fused_encoder.txt | 38 | 109 | 21 | 108 | 0/71 (0.0 Mio) | 476 / 28 | OK |
| e6_small_encode.txt | 126 | 904 | 106 | 904 | 0/364 (0.0 Mio) | 1091 / 457 | OK |
| e6_sub_small_eager.txt | 197 | 729 | 176 | 728 | 0/211 (0.0 Mio) | 806 / 284 | OK |
| e6_sub_small_none.txt | 193 | 623 | 176 | 623 | 0/199 (0.0 Mio) | 638 / 225 | OK |
| e6_tiny_encode.txt | 45 | 828 | 24 | 828 | 0/83 (0.0 Mio) | 874 / 107 | OK |
| e7_fused_encoder.txt | 37 | 108 | 21 | 108 | 0/71 (0.0 Mio) | 422 / 29 | OK |
| e7_small_encode.txt | 126 | 652 | 105 | 652 | 0/364 (0.0 Mio) | 1122 / 455 | OK |
| e7_sub_small_eager.txt | 197 | 429 | 176 | 429 | 0/211 (0.0 Mio) | 781 / 266 | OK |
| e7_sub_small_none.txt | 204 | 340 | 176 | 340 | 0/199 (0.0 Mio) | 596 / 221 | OK |
| e7_tiny_encode.txt | 45 | 830 | 24 | 830 | 0/83 (0.0 Mio) | 885 / 121 | OK |
| e7b_sub_small_eager.txt | 204 | 289 | 176 | 288 | 0/211 (0.0 Mio) | 782 / 271 | OK |
| e7b_sub_small_none.txt | 199 | 254 | 176 | 254 | 0/199 (0.0 Mio) | 589 / 223 | OK |

### e2_counts.txt
```
fused tiny encoder: SdpaNode=4 SoftmaxNode=0
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
[MLXBackend.cpp:245] MLX Metal cache limit set to 256MB
[MLXExecutor.h:848] MLX constants: 364 loaded, 0 copied by MLX (0 bytes resident twice)
[start] rss 326.6 MiB, phys_footprint 270.0 MiB, lifetime_max 270.8 MiB
[after load_program] rss 333.3 MiB, phys_footprint 276.3 MiB, lifetime_max 276.3 MiB
[after load_method] rss 432.9 MiB, phys_footprint 281.3 MiB, lifetime_max 281.3 MiB
  input 0: sizes=(480000,) scalar_type=6
[after execute 1] rss 445.5 MiB, phys_footprint 548.4 MiB, lifetime_max 1053.0 MiB outputs: [(1, 1500, 768)]
[after execute 2] rss 450.2 MiB, phys_footprint 554.4 MiB, lifetime_max 1081.1 MiB outputs: [(1, 1500, 768)]
[after execute 3] rss 454.7 MiB, phys_footprint 554.4 MiB, lifetime_max 1081.1 MiB outputs: [(1, 1500, 768)]
```

### e8_tiny_encode_mmap.txt
```
[MLXBackend.cpp:245] MLX Metal cache limit set to 256MB
[MLXExecutor.h:848] MLX constants: 83 loaded, 0 copied by MLX (0 bytes resident twice)
[start] rss 328.9 MiB, phys_footprint 272.3 MiB, lifetime_max 273.1 MiB
[after load_program] rss 333.1 MiB, phys_footprint 276.4 MiB, lifetime_max 276.4 MiB
[after load_method] rss 355.4 MiB, phys_footprint 277.3 MiB, lifetime_max 277.6 MiB
  input 0: sizes=(480000,) scalar_type=6
[after execute 1] rss 365.0 MiB, phys_footprint 540.5 MiB, lifetime_max 1077.2 MiB outputs: [(1, 1500, 384)]
[after execute 2] rss 367.6 MiB, phys_footprint 541.5 MiB, lifetime_max 1080.3 MiB outputs: [(1, 1500, 384)]
[after execute 3] rss 367.7 MiB, phys_footprint 539.5 MiB, lifetime_max 1080.3 MiB outputs: [(1, 1500, 384)]
```
