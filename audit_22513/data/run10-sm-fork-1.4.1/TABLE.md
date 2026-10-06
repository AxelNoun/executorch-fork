| fichier | peak RSS (Mio) | peak footprint (Mio) | lifetime_max après load (Mio) | lifetime_max après exécution (Mio) | constantes copiées par MLX | ms 1re / régime établi | statut |
|---|---|---|---|---|---|---|---|
| e0_machine.txt | – | – | – | – | – | – | ? |
| e10_tiny_int8_decode.txt | 71 | 76 | 59 | 76 | 0/181 (0.0 Mio) | 271 / 10 | OK |
| e10_tiny_int8_encode.txt | 38 | 358 | 20 | 358 | 0/132 (0.0 Mio) | 997 / 90 | OK |
| e12_small_decode_lim250.txt | 7 | 2 | – | – | – | – | ? |
| e12_small_encode_cacheenv0.txt | 124 | 473 | 105 | 473 | 0/364 (0.0 Mio) | 1969 / 1391 | OK |
| e12_small_encode_cacheenv4096.txt | 132 | 552 | 105 | 552 | 0/364 (0.0 Mio) | 1500 / 470 | OK |
| e12_small_encode_mb2.txt | 134 | 390 | 105 | 390 | 0/364 (0.0 Mio) | 1453 / 512 | OK |
| e12_tiny_encode_mb2.txt | 46 | 830 | 24 | 830 | 0/83 (0.0 Mio) | 1324 / 184 | OK |
| e1_small_decode.txt | 219 | 281 | 212 | 281 | 0/533 (0.0 Mio) | 852 / 50 | OK |
| e1_small_encode.txt | 124 | 396 | 106 | 396 | 0/364 (0.0 Mio) | 4195 / 509 | OK |
| e1_sub_small_eager.txt | 201 | 425 | 176 | 425 | 0/211 (0.0 Mio) | 1779 / 296 | OK |
| e1_sub_small_none.txt | 201 | 412 | 176 | 412 | 0/199 (0.0 Mio) | 953 / 230 | OK |
| e1_tiny_decode.txt | 80 | 84 | 67 | 84 | 0/100 (0.0 Mio) | 870 / 9 | OK |
| e1_tiny_encode.txt | 45 | 827 | 24 | 827 | 0/83 (0.0 Mio) | 1818 / 158 | OK |
| e3_fused_encoder.txt | 38 | 108 | 21 | 108 | 0/71 (0.0 Mio) | 1532 / 31 | OK |
| e4_small_encode_lim250.txt | 7 | 2 | – | – | – | – | ? |
| e4_small_encode_lim400.txt | 7 | 2 | – | – | – | – | ? |
| e4_small_encode_lim600.txt | 7 | 2 | – | – | – | – | ? |
| e4_sub_small_eager_lim300.txt | 7 | 2 | – | – | – | – | ? |
| e4_sub_small_eager_lim450.txt | 7 | 2 | – | – | – | – | ? |
| e4_sub_small_none_lim300.txt | 7 | 2 | – | – | – | – | ? |
| e4_sub_small_none_lim450.txt | 7 | 2 | – | – | – | – | ? |
| e4_tiny_encode_cache0.txt | 7 | 2 | – | – | – | – | ? |
| e4_tiny_encode_lim100.txt | 7 | 2 | – | – | – | – | ? |
| e4_tiny_encode_lim200.txt | 7 | 2 | – | – | – | – | ? |
| e4_tiny_encode_lim400.txt | 7 | 2 | – | – | – | – | ? |
| e6_fused_encoder.txt | 39 | 109 | 21 | 108 | 0/71 (0.0 Mio) | 724 / 32 | OK |
| e6_small_encode.txt | 124 | 525 | 106 | 525 | 0/364 (0.0 Mio) | 1850 / 503 | OK |
| e6_sub_small_eager.txt | 201 | 481 | 176 | 481 | 0/211 (0.0 Mio) | 1321 / 315 | OK |
| e6_sub_small_none.txt | 202 | 412 | 176 | 412 | 0/199 (0.0 Mio) | 1055 / 231 | OK |
| e6_tiny_encode.txt | 45 | 828 | 24 | 828 | 0/83 (0.0 Mio) | 1768 / 149 | OK |
| e7_fused_encoder.txt | 38 | 109 | 21 | 108 | 0/71 (0.0 Mio) | 893 / 30 | OK |
| e7_small_encode.txt | 124 | 396 | 105 | 396 | 0/364 (0.0 Mio) | 1940 / 520 | OK |
| e7_sub_small_eager.txt | 195 | 478 | 176 | 478 | 0/211 (0.0 Mio) | 1109 / 287 | OK |
| e7_sub_small_none.txt | 201 | 340 | 176 | 340 | 0/199 (0.0 Mio) | 841 / 231 | OK |
| e7_tiny_encode.txt | 45 | 829 | 24 | 829 | 0/83 (0.0 Mio) | 1671 / 151 | OK |
| e7b_sub_small_eager.txt | 203 | 339 | 176 | 339 | 0/211 (0.0 Mio) | 901 / 293 | OK |
| e7b_sub_small_none.txt | 199 | 254 | 176 | 254 | 0/199 (0.0 Mio) | 800 / 240 | OK |

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
[MLXBackend.cpp:264] MLX Metal cache limit set to 256MB
[MLXExecutor.h:848] MLX constants: 364 loaded, 0 copied by MLX (0 bytes resident twice)
[start] rss 329.7 MiB, phys_footprint 271.9 MiB, lifetime_max 272.5 MiB
[after load_program] rss 336.4 MiB, phys_footprint 278.1 MiB, lifetime_max 278.2 MiB
[after load_method] rss 435.8 MiB, phys_footprint 282.9 MiB, lifetime_max 282.9 MiB
  input 0: sizes=(480000,) scalar_type=6
[after execute 1] rss 446.6 MiB, phys_footprint 546.8 MiB, lifetime_max 570.0 MiB outputs: [(1, 1500, 768)]
[after execute 2] rss 451.1 MiB, phys_footprint 546.9 MiB, lifetime_max 574.6 MiB outputs: [(1, 1500, 768)]
[after execute 3] rss 455.5 MiB, phys_footprint 546.9 MiB, lifetime_max 574.6 MiB outputs: [(1, 1500, 768)]
```

### e8_tiny_encode_mmap.txt
```
[MLXBackend.cpp:264] MLX Metal cache limit set to 256MB
[MLXExecutor.h:848] MLX constants: 83 loaded, 0 copied by MLX (0 bytes resident twice)
[start] rss 329.1 MiB, phys_footprint 271.1 MiB, lifetime_max 271.8 MiB
[after load_program] rss 333.5 MiB, phys_footprint 275.2 MiB, lifetime_max 275.2 MiB
[after load_method] rss 355.8 MiB, phys_footprint 276.0 MiB, lifetime_max 276.4 MiB
  input 0: sizes=(480000,) scalar_type=6
[after execute 1] rss 364.8 MiB, phys_footprint 538.0 MiB, lifetime_max 1074.3 MiB outputs: [(1, 1500, 384)]
[after execute 2] rss 365.2 MiB, phys_footprint 536.7 MiB, lifetime_max 1077.1 MiB outputs: [(1, 1500, 384)]
[after execute 3] rss 365.3 MiB, phys_footprint 536.5 MiB, lifetime_max 1077.1 MiB outputs: [(1, 1500, 384)]
```
