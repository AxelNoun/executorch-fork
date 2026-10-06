| fichier | peak RSS (Mio) | peak footprint (Mio) | lifetime_max après load (Mio) | lifetime_max après exécution (Mio) | constantes copiées par MLX | ms 1re / régime établi | statut |
|---|---|---|---|---|---|---|---|
| e10_tiny_int8_decode.txt | 71 | 76 | 59 | 76 | 0/181 (0.0 Mio) | 246 / 9 | OK |
| e10_tiny_int8_encode.txt | 41 | 468 | 20 | 468 | 0/132 (0.0 Mio) | 1157 / 132 | OK |
| e1_small_decode.txt | 219 | 281 | 212 | 281 | 0/533 (0.0 Mio) | 708 / 50 | OK |
| e1_small_encode.txt | 127 | 905 | 106 | 905 | 0/364 (0.0 Mio) | 5000 / 514 | OK |
| e1_sub_small_eager.txt | 195 | 725 | 176 | 724 | 0/211 (0.0 Mio) | 967 / 292 | OK |
| e1_sub_small_none.txt | 193 | 627 | 176 | 627 | 0/199 (0.0 Mio) | 740 / 228 | OK |
| e1_tiny_decode.txt | 79 | 84 | 67 | 84 | 0/100 (0.0 Mio) | 657 / 8 | OK |
| e1_tiny_encode.txt | 45 | 828 | 24 | 828 | 0/83 (0.0 Mio) | 1912 / 171 | OK |
| e3_fused_encoder.txt | 37 | 108 | 21 | 108 | 0/71 (0.0 Mio) | 815 / 29 | OK |
| e4_small_encode_lim250.txt | 124 | 368 | 105 | 368 | 0/364 (0.0 Mio) | 1520 / 582 | OK |
| e4_small_encode_lim400.txt | 124 | 472 | 105 | 472 | 0/364 (0.0 Mio) | 1411 / 651 | OK |
| e4_small_encode_lim600.txt | 125 | 629 | 105 | 629 | 0/364 (0.0 Mio) | 1557 / 475 | OK |
| e4_sub_small_eager_lim300.txt | 202 | 353 | 176 | 353 | 0/211 (0.0 Mio) | 850 / 337 | OK |
| e4_sub_small_eager_lim450.txt | 193 | 506 | 176 | 506 | 0/211 (0.0 Mio) | 814 / 286 | OK |
| e4_sub_small_none_lim300.txt | 201 | 343 | 176 | 343 | 0/199 (0.0 Mio) | 760 / 227 | OK |
| e4_sub_small_none_lim450.txt | 193 | 470 | 176 | 470 | 0/199 (0.0 Mio) | 677 / 229 | OK |
| e4_tiny_encode_cache0.txt | 45 | 828 | 24 | 828 | 0/83 (0.0 Mio) | 912 / 122 | OK |
| e4_tiny_encode_lim100.txt | 44 | 820 | 24 | 820 | 0/83 (0.0 Mio) | 1526 / 323 | OK |
| e4_tiny_encode_lim200.txt | 44 | 824 | 24 | 824 | 0/83 (0.0 Mio) | 1217 / 331 | OK |
| e4_tiny_encode_lim400.txt | 44 | 821 | 24 | 821 | 0/83 (0.0 Mio) | 1034 / 209 | OK |
| e6_fused_encoder.txt | 41 | 122 | 21 | 122 | 0/71 (0.0 Mio) | 574 / 30 | OK |
| e6_small_encode.txt | 126 | 904 | 106 | 904 | 0/364 (0.0 Mio) | 1490 / 477 | OK |
| e6_sub_small_eager.txt | 197 | 728 | 176 | 728 | 0/211 (0.0 Mio) | 799 / 285 | OK |
| e6_sub_small_none.txt | 196 | 623 | 176 | 624 | 0/199 (0.0 Mio) | 574 / 231 | OK |
| e6_tiny_encode.txt | 45 | 828 | 24 | 828 | 0/83 (0.0 Mio) | 1161 / 139 | OK |
| e7_fused_encoder.txt | 37 | 109 | 21 | 108 | 0/71 (0.0 Mio) | 545 / 29 | OK |
| e7_small_encode.txt | 126 | 652 | 105 | 652 | 0/364 (0.0 Mio) | 1215 / 491 | OK |
| e7_sub_small_eager.txt | 197 | 429 | 176 | 429 | 0/211 (0.0 Mio) | 797 / 269 | OK |
| e7_sub_small_none.txt | 203 | 340 | 176 | 340 | 0/199 (0.0 Mio) | 625 / 224 | OK |
| e7_tiny_encode.txt | 46 | 830 | 24 | 830 | 0/83 (0.0 Mio) | 1285 / 133 | OK |
| e7b_sub_small_eager.txt | 204 | 289 | 176 | 288 | 0/211 (0.0 Mio) | 859 / 276 | OK |
| e7b_sub_small_none.txt | 199 | 255 | 176 | 255 | 0/199 (0.0 Mio) | 733 / 230 | OK |

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
[MLXBackend.cpp:259] MLX Metal cache limit set to 256MB
[MLXExecutor.h:848] MLX constants: 364 loaded, 0 copied by MLX (0 bytes resident twice)
[start] rss 327.7 MiB, phys_footprint 268.8 MiB, lifetime_max 269.5 MiB
[after load_program] rss 334.4 MiB, phys_footprint 275.1 MiB, lifetime_max 275.1 MiB
[after load_method] rss 434.4 MiB, phys_footprint 280.5 MiB, lifetime_max 280.5 MiB
  input 0: sizes=(480000,) scalar_type=6
[after execute 1] rss 445.5 MiB, phys_footprint 553.6 MiB, lifetime_max 1067.0 MiB outputs: [(1, 1500, 768)]
[after execute 2] rss 450.1 MiB, phys_footprint 552.1 MiB, lifetime_max 1078.8 MiB outputs: [(1, 1500, 768)]
[after execute 3] rss 454.8 MiB, phys_footprint 552.4 MiB, lifetime_max 1079.0 MiB outputs: [(1, 1500, 768)]
```

### e8_tiny_encode_mmap.txt
```
[MLXBackend.cpp:259] MLX Metal cache limit set to 256MB
[MLXExecutor.h:848] MLX constants: 83 loaded, 0 copied by MLX (0 bytes resident twice)
[start] rss 327.5 MiB, phys_footprint 270.7 MiB, lifetime_max 271.4 MiB
[after load_program] rss 331.8 MiB, phys_footprint 274.7 MiB, lifetime_max 274.7 MiB
[after load_method] rss 354.3 MiB, phys_footprint 275.6 MiB, lifetime_max 275.9 MiB
  input 0: sizes=(480000,) scalar_type=6
[after execute 1] rss 363.5 MiB, phys_footprint 538.3 MiB, lifetime_max 1075.3 MiB outputs: [(1, 1500, 384)]
[after execute 2] rss 366.0 MiB, phys_footprint 538.8 MiB, lifetime_max 1077.8 MiB outputs: [(1, 1500, 384)]
[after execute 3] rss 368.4 MiB, phys_footprint 539.4 MiB, lifetime_max 1078.0 MiB outputs: [(1, 1500, 384)]
```
