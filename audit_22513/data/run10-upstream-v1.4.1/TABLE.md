| fichier | peak RSS (Mio) | peak footprint (Mio) | lifetime_max après load (Mio) | lifetime_max après exécution (Mio) | constantes copiées par MLX | ms 1re / régime établi | statut |
|---|---|---|---|---|---|---|---|
| e0_machine.txt | – | – | – | – | – | – | ? |
| e10_tiny_int8_decode.txt | 67 | 61 | 59 | – | 0/181 (0.0 Mio) | – | ÉCHEC |
| e10_tiny_int8_encode.txt | 30 | 22 | 20 | – | 0/132 (0.0 Mio) | – | ÉCHEC |
| e11_dev_tiny_eager_lim100.txt | 37 | 138 | 22 | 138 | 0/75 (0.0 Mio) | 702 / 54 | OK |
| e11_dev_tiny_eager_lim60.txt | 40 | 162 | 21 | 162 | 0/75 (0.0 Mio) | 779 / 90 | OK |
| e11_dev_tiny_eager_mb10.txt | 44 | 171 | 22 | 171 | 0/75 (0.0 Mio) | 744 / 38 | OK |
| e11_dev_tiny_none_lim100.txt | 37 | 108 | 21 | 108 | 0/71 (0.0 Mio) | 535 / 29 | OK |
| e11_dev_tiny_none_lim60.txt | 38 | 83 | 22 | 82 | 0/71 (0.0 Mio) | 612 / 46 | OK |
| e11_dev_tiny_none_mb10.txt | 38 | 109 | 22 | 109 | 0/71 (0.0 Mio) | 609 / 30 | OK |
| e12_small_decode_lim250.txt | 213 | 216 | 212 | – | 0/533 (0.0 Mio) | – | ÉCHEC |
| e12_small_encode_cacheenv0.txt | 113 | 107 | 105 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e12_small_encode_cacheenv4096.txt | 113 | 107 | 105 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e12_small_encode_mb2.txt | 113 | 107 | 105 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e12_tiny_encode_mb2.txt | 46 | 830 | 24 | 830 | 0/83 (0.0 Mio) | 1355 / 61 | OK |
| e1_small_decode.txt | 213 | 216 | 212 | – | 0/533 (0.0 Mio) | – | ÉCHEC |
| e1_small_encode.txt | 113 | 107 | 105 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e1_sub_small_eager.txt | 204 | 725 | 176 | 725 | 0/211 (0.0 Mio) | 1385 / 286 | OK |
| e1_sub_small_none.txt | 198 | 627 | 176 | 627 | 0/199 (0.0 Mio) | 1016 / 227 | OK |
| e1_tiny_decode.txt | 79 | 84 | 67 | 84 | 0/100 (0.0 Mio) | 1269 / 8 | OK |
| e1_tiny_encode.txt | 43 | 829 | 24 | 829 | 0/83 (0.0 Mio) | 6555 / 67 | OK |
| e3_device_encoder_eager_bf16_L12_fp32in.txt | 205 | 726 | 176 | 726 | 0/211 (0.0 Mio) | 1126 / 282 | OK |
| e3_device_encoder_eager_bf16_L4_tiny_fp32in.txt | 38 | 216 | 22 | 216 | 0/75 (0.0 Mio) | 771 / 38 | OK |
| e3_device_encoder_none_bf16_L12_fp32in.txt | 199 | 629 | 176 | 629 | 0/199 (0.0 Mio) | 825 / 223 | OK |
| e3_device_encoder_none_bf16_L4_tiny_fp32in.txt | 39 | 108 | 21 | 108 | 0/71 (0.0 Mio) | 564 / 29 | OK |
| e3_fused_encoder.txt | 37 | 107 | 21 | 107 | 0/71 (0.0 Mio) | 1182 / 32 | OK |
| e4_small_encode_lim250.txt | 113 | 107 | 105 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e4_small_encode_lim400.txt | 113 | 107 | 105 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e4_small_encode_lim600.txt | 113 | 107 | 105 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e4_sub_small_eager_lim300.txt | 202 | 353 | 176 | 353 | 0/211 (0.0 Mio) | 997 / 301 | OK |
| e4_sub_small_eager_lim450.txt | 198 | 515 | 176 | 515 | 0/211 (0.0 Mio) | 1152 / 295 | OK |
| e4_sub_small_none_lim300.txt | 201 | 332 | 176 | 332 | 0/199 (0.0 Mio) | 853 / 233 | OK |
| e4_sub_small_none_lim450.txt | 202 | 470 | 176 | 470 | 0/199 (0.0 Mio) | 849 / 233 | OK |
| e4_tiny_encode_cache0.txt | 45 | 822 | 24 | 822 | 0/83 (0.0 Mio) | 1147 / 199 | OK |
| e4_tiny_encode_lim100.txt | 47 | 821 | 24 | 820 | 0/83 (0.0 Mio) | 1414 / 320 | OK |
| e4_tiny_encode_lim200.txt | 47 | 821 | 24 | 820 | 0/83 (0.0 Mio) | 1209 / 338 | OK |
| e4_tiny_encode_lim400.txt | 47 | 821 | 24 | 821 | 0/83 (0.0 Mio) | 1379 / 238 | OK |
| e6_fused_encoder.txt | 38 | 107 | 21 | 107 | 0/71 (0.0 Mio) | 675 / 42 | OK |
| e6_small_encode.txt | 113 | 108 | 106 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e6_sub_small_eager.txt | 204 | 729 | 176 | 729 | 0/211 (0.0 Mio) | 1117 / 282 | OK |
| e6_sub_small_none.txt | 203 | 624 | 176 | 624 | 0/199 (0.0 Mio) | 895 / 226 | OK |
| e6_tiny_encode.txt | 45 | 829 | 24 | 829 | 0/83 (0.0 Mio) | 1256 / 56 | OK |
| e7_fused_encoder.txt | 37 | 107 | 21 | 107 | 0/71 (0.0 Mio) | 731 / 30 | OK |
| e7_small_encode.txt | 113 | 107 | 105 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e7_sub_small_eager.txt | 204 | 429 | 176 | 429 | 0/211 (0.0 Mio) | 1121 / 288 | OK |
| e7_sub_small_none.txt | 201 | 341 | 176 | 340 | 0/199 (0.0 Mio) | 799 / 227 | OK |
| e7_tiny_encode.txt | 47 | 831 | 24 | 830 | 0/83 (0.0 Mio) | 1227 / 56 | OK |
| e7b_sub_small_eager.txt | 199 | 289 | 176 | 288 | 0/211 (0.0 Mio) | 1182 / 290 | OK |
| e7b_sub_small_none.txt | 201 | 255 | 176 | 254 | 0/199 (0.0 Mio) | 857 / 232 | OK |

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
[start] rss 327.3 MiB, phys_footprint 270.0 MiB, lifetime_max 270.6 MiB
[after load_program] rss 334.0 MiB, phys_footprint 276.2 MiB, lifetime_max 276.2 MiB
[after load_method] rss 433.9 MiB, phys_footprint 281.5 MiB, lifetime_max 281.5 MiB
  input 0: sizes=(480000,) scalar_type=6
```

### e8_tiny_encode_mmap.txt
```
[MLXExecutor.h:848] MLX constants: 83 loaded, 0 copied by MLX (0 bytes resident twice)
[start] rss 329.0 MiB, phys_footprint 270.6 MiB, lifetime_max 271.4 MiB
[after load_program] rss 333.3 MiB, phys_footprint 274.6 MiB, lifetime_max 274.6 MiB
[after load_method] rss 355.7 MiB, phys_footprint 275.5 MiB, lifetime_max 275.9 MiB
  input 0: sizes=(480000,) scalar_type=6
[after execute 1] rss 367.6 MiB, phys_footprint 1076.8 MiB, lifetime_max 1076.8 MiB outputs: [(1, 1500, 384)]
[after execute 2] rss 370.3 MiB, phys_footprint 1078.5 MiB, lifetime_max 1080.7 MiB outputs: [(1, 1500, 384)]
[after execute 3] rss 370.6 MiB, phys_footprint 1076.6 MiB, lifetime_max 1080.7 MiB outputs: [(1, 1500, 384)]
```
