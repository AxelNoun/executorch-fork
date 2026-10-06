| fichier | peak RSS (Mio) | peak footprint (Mio) | lifetime_max après load (Mio) | lifetime_max après exécution (Mio) | constantes copiées par MLX | ms 1re / régime établi | statut |
|---|---|---|---|---|---|---|---|
| e10_tiny_int8_decode.txt | 67 | 61 | 59 | – | 0/181 (0.0 Mio) | – | ÉCHEC |
| e10_tiny_int8_encode.txt | 30 | 22 | 20 | – | 0/132 (0.0 Mio) | – | ÉCHEC |
| e1_small_decode.txt | 213 | 216 | 212 | – | 0/533 (0.0 Mio) | – | ÉCHEC |
| e1_small_encode.txt | 113 | 107 | 106 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e1_sub_small_eager.txt | 204 | 725 | 176 | 725 | 0/211 (0.0 Mio) | 944 / 267 | OK |
| e1_sub_small_none.txt | 194 | 627 | 176 | 627 | 0/199 (0.0 Mio) | 667 / 222 | OK |
| e1_tiny_decode.txt | 80 | 84 | 66 | 84 | 0/100 (0.0 Mio) | 728 / 8 | OK |
| e1_tiny_encode.txt | 43 | 830 | 24 | 830 | 0/83 (0.0 Mio) | 4190 / 61 | OK |
| e3_device_encoder_eager_bf16_L12_fp32in.txt | 205 | 726 | 176 | 726 | 0/211 (0.0 Mio) | 830 / 265 | OK |
| e3_device_encoder_eager_bf16_L4_tiny_fp32in.txt | 38 | 216 | 21 | 216 | 0/75 (0.0 Mio) | 575 / 35 | OK |
| e3_device_encoder_none_bf16_L12_fp32in.txt | 195 | 629 | 176 | 629 | 0/199 (0.0 Mio) | 711 / 220 | OK |
| e3_device_encoder_none_bf16_L4_tiny_fp32in.txt | 38 | 108 | 21 | 108 | 0/71 (0.0 Mio) | 461 / 28 | OK |
| e3_fused_encoder.txt | 37 | 107 | 21 | 107 | 0/71 (0.0 Mio) | 747 / 28 | OK |
| e4_small_encode_lim250.txt | 113 | 107 | 105 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e4_small_encode_lim400.txt | 113 | 107 | 105 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e4_small_encode_lim600.txt | 113 | 107 | 105 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e4_sub_small_eager_lim300.txt | 202 | 353 | 176 | 353 | 0/211 (0.0 Mio) | 843 / 276 | OK |
| e4_sub_small_eager_lim450.txt | 198 | 506 | 176 | 506 | 0/211 (0.0 Mio) | 788 / 275 | OK |
| e4_sub_small_none_lim300.txt | 201 | 343 | 176 | 343 | 0/199 (0.0 Mio) | 608 / 226 | OK |
| e4_sub_small_none_lim450.txt | 202 | 470 | 176 | 470 | 0/199 (0.0 Mio) | 739 / 231 | OK |
| e4_tiny_encode_cache0.txt | 45 | 822 | 24 | 822 | 0/83 (0.0 Mio) | 915 / 149 | OK |
| e4_tiny_encode_lim100.txt | 47 | 821 | 24 | 820 | 0/83 (0.0 Mio) | 1174 / 279 | OK |
| e4_tiny_encode_lim200.txt | 47 | 821 | 24 | 820 | 0/83 (0.0 Mio) | 1007 / 253 | OK |
| e4_tiny_encode_lim400.txt | 47 | 821 | 24 | 821 | 0/83 (0.0 Mio) | 970 / 204 | OK |
| e6_fused_encoder.txt | 38 | 107 | 21 | 107 | 0/71 (0.0 Mio) | 424 / 28 | OK |
| e6_small_encode.txt | 113 | 108 | 106 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e6_sub_small_eager.txt | 204 | 729 | 176 | 729 | 0/211 (0.0 Mio) | 820 / 268 | OK |
| e6_sub_small_none.txt | 203 | 624 | 176 | 624 | 0/199 (0.0 Mio) | 615 / 218 | OK |
| e6_tiny_encode.txt | 45 | 829 | 24 | 829 | 0/83 (0.0 Mio) | 919 / 51 | OK |
| e7_fused_encoder.txt | 37 | 108 | 21 | 107 | 0/71 (0.0 Mio) | 429 / 28 | OK |
| e7_small_encode.txt | 113 | 107 | 105 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e7_sub_small_eager.txt | 204 | 429 | 176 | 429 | 0/211 (0.0 Mio) | 832 / 278 | OK |
| e7_sub_small_none.txt | 201 | 340 | 176 | 340 | 0/199 (0.0 Mio) | 584 / 221 | OK |
| e7_tiny_encode.txt | 47 | 831 | 24 | 830 | 0/83 (0.0 Mio) | 824 / 51 | OK |
| e7b_sub_small_eager.txt | 199 | 289 | 176 | 288 | 0/211 (0.0 Mio) | 833 / 274 | OK |
| e7b_sub_small_none.txt | 199 | 254 | 176 | 254 | 0/199 (0.0 Mio) | 595 / 224 | OK |

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
[MLXExecutor.h:848] MLX constants: 364 loaded, 0 copied by MLX (0 bytes resident twice)
[MLXBackend.cpp:511] MLX execute failed: [scatter_add_axis] Received invalid axis for array with 3 dimensions.
[method.cpp:1530] CALL_DELEGATE execute failed at instruction 0: 0x1
[start] rss 328.8 MiB, phys_footprint 270.5 MiB, lifetime_max 271.1 MiB
[after load_program] rss 335.4 MiB, phys_footprint 276.7 MiB, lifetime_max 276.7 MiB
[after load_method] rss 435.0 MiB, phys_footprint 281.3 MiB, lifetime_max 281.3 MiB
  input 0: sizes=(480000,) scalar_type=6
```

### e8_tiny_encode_mmap.txt
```
[MLXExecutor.h:848] MLX constants: 83 loaded, 0 copied by MLX (0 bytes resident twice)
[start] rss 328.5 MiB, phys_footprint 271.6 MiB, lifetime_max 272.3 MiB
[after load_program] rss 332.7 MiB, phys_footprint 275.6 MiB, lifetime_max 275.6 MiB
[after load_method] rss 355.1 MiB, phys_footprint 276.4 MiB, lifetime_max 276.8 MiB
  input 0: sizes=(480000,) scalar_type=6
[after execute 1] rss 366.5 MiB, phys_footprint 1077.1 MiB, lifetime_max 1077.1 MiB outputs: [(1, 1500, 384)]
[after execute 2] rss 369.1 MiB, phys_footprint 1078.8 MiB, lifetime_max 1081.0 MiB outputs: [(1, 1500, 384)]
[after execute 3] rss 371.4 MiB, phys_footprint 1078.9 MiB, lifetime_max 1081.1 MiB outputs: [(1, 1500, 384)]
```
