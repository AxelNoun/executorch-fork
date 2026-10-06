| fichier | peak RSS (Mio) | peak footprint (Mio) | lifetime_max après load (Mio) | lifetime_max après exécution (Mio) | constantes copiées par MLX | ms 1re / régime établi | statut |
|---|---|---|---|---|---|---|---|
| e0_machine.txt | – | – | – | – | – | – | ? |
| e10_tiny_int8_decode.txt | 71 | 76 | – | – | 0/181 (0.0 Mio) | 206 / 10 | OK |
| e10_tiny_int8_encode.txt | 38 | 358 | – | – | 0/132 (0.0 Mio) | 776 / 83 | OK |
| e12_small_decode_lim250.txt | 7 | 2 | – | – | – | – | ? |
| e12_small_encode_cacheenv0.txt | 124 | 474 | – | – | 0/364 (0.0 Mio) | 2120 / 871 | OK |
| e12_small_encode_cacheenv4096.txt | 133 | 395 | – | – | 0/364 (0.0 Mio) | 1175 / 464 | OK |
| e12_small_encode_mb2.txt | 134 | 390 | – | – | 0/364 (0.0 Mio) | 1697 / 523 | OK |
| e12_tiny_encode_mb2.txt | 46 | 830 | – | – | 0/83 (0.0 Mio) | 1834 / 189 | OK |
| e1_small_decode.txt | 219 | 281 | – | – | 0/533 (0.0 Mio) | 523 / 49 | OK |
| e1_small_encode.txt | 124 | 396 | – | – | 0/364 (0.0 Mio) | 3159 / 492 | OK |
| e1_sub_small_eager.txt | 197 | 477 | – | – | 0/211 (0.0 Mio) | 1573 / 303 | OK |
| e1_sub_small_none.txt | 201 | 434 | – | – | 0/199 (0.0 Mio) | 1128 / 234 | OK |
| e1_tiny_decode.txt | 80 | 84 | – | – | 0/100 (0.0 Mio) | 563 / 8 | OK |
| e1_tiny_encode.txt | 45 | 827 | – | – | 0/83 (0.0 Mio) | 1236 / 145 | OK |
| e3_fused_encoder.txt | 37 | 108 | – | – | 0/71 (0.0 Mio) | 1146 / 30 | OK |
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
| e6_fused_encoder.txt | 39 | 109 | – | – | 0/71 (0.0 Mio) | 656 / 30 | OK |
| e6_small_encode.txt | 124 | 396 | – | – | 0/364 (0.0 Mio) | 1272 / 514 | OK |
| e6_sub_small_eager.txt | 201 | 476 | – | – | 0/211 (0.0 Mio) | 1273 / 324 | OK |
| e6_sub_small_none.txt | 202 | 412 | – | – | 0/199 (0.0 Mio) | 870 / 232 | OK |
| e6_tiny_encode.txt | 45 | 828 | – | – | 0/83 (0.0 Mio) | 1219 / 167 | OK |
| e7_fused_encoder.txt | 38 | 109 | – | – | 0/71 (0.0 Mio) | 677 / 31 | OK |
| e7_small_encode.txt | 124 | 396 | – | – | 0/364 (0.0 Mio) | 1178 / 497 | OK |
| e7_sub_small_eager.txt | 200 | 478 | – | – | 0/211 (0.0 Mio) | 1377 / 303 | OK |
| e7_sub_small_none.txt | 201 | 340 | – | – | 0/199 (0.0 Mio) | 913 / 234 | OK |
| e7_tiny_encode.txt | 45 | 829 | – | – | 0/83 (0.0 Mio) | 1130 / 148 | OK |
| e7b_sub_small_eager.txt | 203 | 339 | – | – | 0/211 (0.0 Mio) | 1564 / 322 | OK |
| e7b_sub_small_none.txt | 201 | 254 | – | – | 0/199 (0.0 Mio) | 908 / 237 | OK |

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
[start] rss 328.1 MiB, phys_footprint 272.3 MiB, lifetime_max 273.0 MiB
[after load_program] rss 334.8 MiB, phys_footprint 278.5 MiB, lifetime_max 278.5 MiB
[after load_method] rss 434.2 MiB, phys_footprint 283.4 MiB, lifetime_max 283.4 MiB
  input 0: sizes=(480000,) scalar_type=6
[after execute 1] rss 445.8 MiB, phys_footprint 548.0 MiB, lifetime_max 571.3 MiB outputs: [(1, 1500, 768)]
[after execute 2] rss 450.2 MiB, phys_footprint 548.1 MiB, lifetime_max 575.8 MiB outputs: [(1, 1500, 768)]
[after execute 3] rss 450.3 MiB, phys_footprint 543.7 MiB, lifetime_max 575.8 MiB outputs: [(1, 1500, 768)]
```

### e8_tiny_encode_mmap.txt
```
[MLXBackend.cpp:264] MLX Metal cache limit set to 256MB
[MLXExecutor.h:848] MLX constants: 83 loaded, 0 copied by MLX (0 bytes resident twice)
[start] rss 327.4 MiB, phys_footprint 269.6 MiB, lifetime_max 270.4 MiB
[after load_program] rss 331.7 MiB, phys_footprint 273.6 MiB, lifetime_max 273.7 MiB
[after load_method] rss 353.9 MiB, phys_footprint 274.3 MiB, lifetime_max 274.8 MiB
  input 0: sizes=(480000,) scalar_type=6
[after execute 1] rss 365.0 MiB, phys_footprint 538.5 MiB, lifetime_max 1074.7 MiB outputs: [(1, 1500, 384)]
[after execute 2] rss 367.4 MiB, phys_footprint 539.1 MiB, lifetime_max 1077.5 MiB outputs: [(1, 1500, 384)]
[after execute 3] rss 367.5 MiB, phys_footprint 537.0 MiB, lifetime_max 1077.6 MiB outputs: [(1, 1500, 384)]
```
