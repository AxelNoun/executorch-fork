| fichier | peak RSS (Mio) | peak footprint (Mio) | lifetime_max après load (Mio) | lifetime_max après exécution (Mio) | constantes copiées par MLX | ms 1re / régime établi | statut |
|---|---|---|---|---|---|---|---|
| e0_machine.txt | – | – | – | – | – | – | ? |
| e10_tiny_int8_decode.txt | 67 | 61 | 59 | – | 0/181 (0.0 Mio) | – | ÉCHEC |
| e10_tiny_int8_encode.txt | 30 | 22 | 20 | – | 0/132 (0.0 Mio) | – | ÉCHEC |
| e11_dev_tiny_eager_lim100.txt | 37 | 128 | 22 | 128 | 0/75 (0.0 Mio) | 663 / 43 | OK |
| e11_dev_tiny_eager_lim60.txt | 41 | 105 | 22 | 105 | 0/75 (0.0 Mio) | 686 / 65 | OK |
| e11_dev_tiny_eager_mb10.txt | 44 | 171 | 22 | 171 | 0/75 (0.0 Mio) | 652 / 38 | OK |
| e11_dev_tiny_none_lim100.txt | 39 | 108 | 22 | 108 | 0/71 (0.0 Mio) | 571 / 30 | OK |
| e11_dev_tiny_none_lim60.txt | 38 | 89 | 22 | 89 | 0/71 (0.0 Mio) | 673 / 49 | OK |
| e11_dev_tiny_none_mb10.txt | 40 | 109 | 22 | 109 | 0/71 (0.0 Mio) | 642 / 30 | OK |
| e12_small_decode_lim250.txt | 213 | 216 | 212 | – | 0/533 (0.0 Mio) | – | ÉCHEC |
| e12_small_encode_cacheenv0.txt | 113 | 107 | 105 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e12_small_encode_cacheenv4096.txt | 113 | 107 | 105 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e12_small_encode_mb2.txt | 113 | 107 | 105 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e12_tiny_encode_mb2.txt | 47 | 830 | 24 | 830 | 0/83 (0.0 Mio) | 1081 / 55 | OK |
| e1_small_decode.txt | 213 | 216 | 212 | – | 0/533 (0.0 Mio) | – | ÉCHEC |
| e1_small_encode.txt | 113 | 108 | 106 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e1_sub_small_eager.txt | 204 | 725 | 176 | 725 | 0/211 (0.0 Mio) | 1172 / 277 | OK |
| e1_sub_small_none.txt | 196 | 627 | 176 | 627 | 0/199 (0.0 Mio) | 822 / 223 | OK |
| e1_tiny_decode.txt | 79 | 84 | 67 | 84 | 0/100 (0.0 Mio) | 998 / 8 | OK |
| e1_tiny_encode.txt | 43 | 830 | 24 | 830 | 0/83 (0.0 Mio) | 5090 / 60 | OK |
| e3_device_encoder_eager_bf16_L12_fp32in.txt | 205 | 726 | 176 | 726 | 0/211 (0.0 Mio) | 941 / 275 | OK |
| e3_device_encoder_eager_bf16_L4_tiny_fp32in.txt | 39 | 216 | 22 | 216 | 0/75 (0.0 Mio) | 778 / 38 | OK |
| e3_device_encoder_none_bf16_L12_fp32in.txt | 197 | 629 | 176 | 628 | 0/199 (0.0 Mio) | 688 / 227 | OK |
| e3_device_encoder_none_bf16_L4_tiny_fp32in.txt | 39 | 108 | 21 | 108 | 0/71 (0.0 Mio) | 551 / 29 | OK |
| e3_fused_encoder.txt | 37 | 107 | 21 | 107 | 0/71 (0.0 Mio) | 953 / 29 | OK |
| e4_small_encode_lim250.txt | 113 | 107 | 105 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e4_small_encode_lim400.txt | 113 | 107 | 105 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e4_small_encode_lim600.txt | 113 | 107 | 105 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e4_sub_small_eager_lim300.txt | 202 | 353 | 176 | 353 | 0/211 (0.0 Mio) | 1035 / 298 | OK |
| e4_sub_small_eager_lim450.txt | 196 | 515 | 176 | 515 | 0/211 (0.0 Mio) | 1075 / 298 | OK |
| e4_sub_small_none_lim300.txt | 201 | 332 | 176 | 332 | 0/199 (0.0 Mio) | 815 / 226 | OK |
| e4_sub_small_none_lim450.txt | 202 | 470 | 176 | 470 | 0/199 (0.0 Mio) | 758 / 229 | OK |
| e4_tiny_encode_cache0.txt | 45 | 822 | 24 | 822 | 0/83 (0.0 Mio) | 1058 / 180 | OK |
| e4_tiny_encode_lim100.txt | 46 | 820 | 24 | 820 | 0/83 (0.0 Mio) | 1338 / 350 | OK |
| e4_tiny_encode_lim200.txt | 46 | 820 | 24 | 820 | 0/83 (0.0 Mio) | 1477 / 284 | OK |
| e4_tiny_encode_lim400.txt | 47 | 821 | 24 | 821 | 0/83 (0.0 Mio) | 1142 / 233 | OK |
| e6_fused_encoder.txt | 38 | 107 | 21 | 107 | 0/71 (0.0 Mio) | 660 / 29 | OK |
| e6_small_encode.txt | 113 | 108 | 106 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e6_sub_small_eager.txt | 204 | 729 | 176 | 729 | 0/211 (0.0 Mio) | 970 / 277 | OK |
| e6_sub_small_none.txt | 203 | 624 | 176 | 624 | 0/199 (0.0 Mio) | 858 / 224 | OK |
| e6_tiny_encode.txt | 45 | 829 | 24 | 829 | 0/83 (0.0 Mio) | 1328 / 56 | OK |
| e7_fused_encoder.txt | 37 | 108 | 21 | 107 | 0/71 (0.0 Mio) | 674 / 29 | OK |
| e7_small_encode.txt | 113 | 107 | 105 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e7_sub_small_eager.txt | 204 | 429 | 176 | 429 | 0/211 (0.0 Mio) | 1315 / 296 | OK |
| e7_sub_small_none.txt | 201 | 340 | 176 | 340 | 0/199 (0.0 Mio) | 842 / 226 | OK |
| e7_tiny_encode.txt | 47 | 831 | 24 | 830 | 0/83 (0.0 Mio) | 1297 / 58 | OK |
| e7b_sub_small_eager.txt | 199 | 289 | 176 | 289 | 0/211 (0.0 Mio) | 1081 / 291 | OK |
| e7b_sub_small_none.txt | 197 | 257 | 176 | 257 | 0/199 (0.0 Mio) | 828 / 228 | OK |

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
[start] rss 328.8 MiB, phys_footprint 271.6 MiB, lifetime_max 272.3 MiB
[after load_program] rss 335.4 MiB, phys_footprint 277.9 MiB, lifetime_max 277.9 MiB
[after load_method] rss 435.2 MiB, phys_footprint 283.0 MiB, lifetime_max 283.0 MiB
  input 0: sizes=(480000,) scalar_type=6
```

### e8_tiny_encode_mmap.txt
```
[MLXExecutor.h:848] MLX constants: 83 loaded, 0 copied by MLX (0 bytes resident twice)
[start] rss 329.4 MiB, phys_footprint 272.4 MiB, lifetime_max 273.1 MiB
[after load_program] rss 333.6 MiB, phys_footprint 276.4 MiB, lifetime_max 276.4 MiB
[after load_method] rss 356.0 MiB, phys_footprint 277.2 MiB, lifetime_max 277.6 MiB
  input 0: sizes=(480000,) scalar_type=6
[after execute 1] rss 369.6 MiB, phys_footprint 1080.7 MiB, lifetime_max 1080.7 MiB outputs: [(1, 1500, 384)]
[after execute 2] rss 372.2 MiB, phys_footprint 1081.8 MiB, lifetime_max 1084.1 MiB outputs: [(1, 1500, 384)]
[after execute 3] rss 374.5 MiB, phys_footprint 1081.9 MiB, lifetime_max 1084.1 MiB outputs: [(1, 1500, 384)]
```
