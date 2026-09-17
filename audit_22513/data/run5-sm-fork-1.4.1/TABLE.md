| fichier | peak RSS (Mio) | peak footprint (Mio) | lifetime_max après load (Mio) | lifetime_max après exécution (Mio) | constantes copiées par MLX | ms 1re / régime établi | statut |
|---|---|---|---|---|---|---|---|
| e10_tiny_int8_decode.txt | 71 | 76 | 59 | 76 | 0/181 (0.0 Mio) | 171 / 9 | OK |
| e10_tiny_int8_encode.txt | 38 | 556 | 20 | 556 | 0/132 (0.0 Mio) | 688 / 69 | OK |
| e1_small_decode.txt | 219 | 281 | 212 | 281 | 0/533 (0.0 Mio) | 477 / 48 | OK |
| e1_small_encode.txt | 127 | 905 | 105 | 905 | 0/364 (0.0 Mio) | 2721 / 457 | OK |
| e1_sub_small_eager.txt | 197 | 725 | 176 | 724 | 0/211 (0.0 Mio) | 898 / 282 | OK |
| e1_sub_small_none.txt | 195 | 627 | 176 | 627 | 0/199 (0.0 Mio) | 693 / 232 | OK |
| e1_tiny_decode.txt | 79 | 84 | 66 | 84 | 0/100 (0.0 Mio) | 504 / 7 | OK |
| e1_tiny_encode.txt | 45 | 828 | 24 | 828 | 0/83 (0.0 Mio) | 984 / 94 | OK |
| e3_fused_encoder.txt | 37 | 108 | 21 | 108 | 0/71 (0.0 Mio) | 640 / 28 | OK |
| e4_small_encode_lim250.txt | 124 | 368 | 105 | 368 | 0/364 (0.0 Mio) | 1161 / 501 | OK |
| e4_small_encode_lim400.txt | 124 | 472 | 105 | 472 | 0/364 (0.0 Mio) | 1212 / 571 | OK |
| e4_small_encode_lim600.txt | 125 | 630 | 105 | 630 | 0/364 (0.0 Mio) | 1120 / 467 | OK |
| e4_sub_small_eager_lim300.txt | 202 | 353 | 176 | 353 | 0/211 (0.0 Mio) | 791 / 273 | OK |
| e4_sub_small_eager_lim450.txt | 193 | 506 | 176 | 506 | 0/211 (0.0 Mio) | 780 / 279 | OK |
| e4_sub_small_none_lim300.txt | 201 | 343 | 176 | 343 | 0/199 (0.0 Mio) | 630 / 224 | OK |
| e4_sub_small_none_lim450.txt | 193 | 470 | 176 | 470 | 0/199 (0.0 Mio) | 621 / 227 | OK |
| e4_tiny_encode_cache0.txt | 45 | 828 | 24 | 828 | 0/83 (0.0 Mio) | 874 / 113 | OK |
| e4_tiny_encode_lim100.txt | 44 | 821 | 24 | 820 | 0/83 (0.0 Mio) | 1026 / 276 | OK |
| e4_tiny_encode_lim200.txt | 44 | 821 | 24 | 820 | 0/83 (0.0 Mio) | 998 / 249 | OK |
| e4_tiny_encode_lim400.txt | 44 | 821 | 24 | 821 | 0/83 (0.0 Mio) | 964 / 192 | OK |
| e6_fused_encoder.txt | 38 | 109 | 21 | 108 | 0/71 (0.0 Mio) | 417 / 28 | OK |
| e6_small_encode.txt | 126 | 904 | 106 | 904 | 0/364 (0.0 Mio) | 1064 / 454 | OK |
| e6_sub_small_eager.txt | 197 | 729 | 176 | 729 | 0/211 (0.0 Mio) | 787 / 279 | OK |
| e6_sub_small_none.txt | 193 | 623 | 176 | 623 | 0/199 (0.0 Mio) | 599 / 225 | OK |
| e6_tiny_encode.txt | 45 | 828 | 24 | 828 | 0/83 (0.0 Mio) | 861 / 108 | OK |
| e7_fused_encoder.txt | 37 | 109 | 21 | 108 | 0/71 (0.0 Mio) | 421 / 28 | OK |
| e7_small_encode.txt | 126 | 652 | 105 | 652 | 0/364 (0.0 Mio) | 1075 / 453 | OK |
| e7_sub_small_eager.txt | 197 | 429 | 176 | 429 | 0/211 (0.0 Mio) | 783 / 267 | OK |
| e7_sub_small_none.txt | 201 | 340 | 176 | 340 | 0/199 (0.0 Mio) | 596 / 220 | OK |
| e7_tiny_encode.txt | 46 | 831 | 24 | 831 | 0/83 (0.0 Mio) | 908 / 93 | OK |
| e7b_sub_small_eager.txt | 204 | 289 | 176 | 288 | 0/211 (0.0 Mio) | 777 / 283 | OK |
| e7b_sub_small_none.txt | 199 | 255 | 176 | 254 | 0/199 (0.0 Mio) | 598 / 223 | OK |

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
[start] rss 327.6 MiB, phys_footprint 270.0 MiB, lifetime_max 270.7 MiB
[after load_program] rss 334.3 MiB, phys_footprint 276.3 MiB, lifetime_max 276.3 MiB
[after load_method] rss 434.0 MiB, phys_footprint 281.4 MiB, lifetime_max 281.4 MiB
  input 0: sizes=(480000,) scalar_type=6
[after execute 1] rss 444.8 MiB, phys_footprint 546.7 MiB, lifetime_max 1051.3 MiB outputs: [(1, 1500, 768)]
[after execute 2] rss 449.5 MiB, phys_footprint 552.7 MiB, lifetime_max 1079.3 MiB outputs: [(1, 1500, 768)]
[after execute 3] rss 454.3 MiB, phys_footprint 550.8 MiB, lifetime_max 1079.3 MiB outputs: [(1, 1500, 768)]
```

### e8_tiny_encode_mmap.txt
```
[MLXBackend.cpp:259] MLX Metal cache limit set to 256MB
[MLXExecutor.h:848] MLX constants: 83 loaded, 0 copied by MLX (0 bytes resident twice)
[start] rss 328.0 MiB, phys_footprint 270.3 MiB, lifetime_max 271.0 MiB
[after load_program] rss 332.2 MiB, phys_footprint 274.3 MiB, lifetime_max 274.3 MiB
[after load_method] rss 354.8 MiB, phys_footprint 275.4 MiB, lifetime_max 275.6 MiB
  input 0: sizes=(480000,) scalar_type=6
[after execute 1] rss 365.4 MiB, phys_footprint 539.4 MiB, lifetime_max 1076.7 MiB outputs: [(1, 1500, 384)]
[after execute 2] rss 368.0 MiB, phys_footprint 540.3 MiB, lifetime_max 1079.7 MiB outputs: [(1, 1500, 384)]
[after execute 3] rss 370.4 MiB, phys_footprint 540.9 MiB, lifetime_max 1079.7 MiB outputs: [(1, 1500, 384)]
```
