| fichier | peak RSS (Mio) | peak footprint (Mio) | lifetime_max après load (Mio) | lifetime_max après exécution (Mio) | constantes copiées par MLX | ms 1re / régime établi | statut |
|---|---|---|---|---|---|---|---|
| e1_small_decode.txt | 213 | 216 | 212 | – | 0/533 (0.0 Mio) | – | ÉCHEC |
| e1_small_encode.txt | 113 | 107 | 105 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e1_sub_small_eager.txt | 204 | 724 | 176 | 724 | 0/211 (0.0 Mio) | 1046 / 274 | OK |
| e1_sub_small_none.txt | 194 | 627 | 176 | 627 | 0/199 (0.0 Mio) | 717 / 223 | OK |
| e1_tiny_decode.txt | 80 | 84 | 67 | 84 | 0/100 (0.0 Mio) | 919 / 11 | OK |
| e1_tiny_encode.txt | 46 | 829 | 24 | 829 | 0/83 (0.0 Mio) | 4163 / 60 | OK |
| e3_fused_encoder.txt | 37 | 107 | 21 | 107 | 0/71 (0.0 Mio) | 822 / 30 | OK |
| e6_fused_encoder.txt | 38 | 107 | 21 | 107 | 0/71 (0.0 Mio) | 502 / 29 | OK |
| e6_small_encode.txt | 113 | 108 | 106 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e6_sub_small_eager.txt | 204 | 729 | 176 | 729 | 0/211 (0.0 Mio) | 905 / 271 | OK |
| e6_sub_small_none.txt | 203 | 624 | 176 | 624 | 0/199 (0.0 Mio) | 702 / 227 | OK |
| e6_tiny_encode.txt | 45 | 829 | 24 | 829 | 0/83 (0.0 Mio) | 1141 / 55 | OK |
| e7_fused_encoder.txt | 37 | 107 | 21 | 107 | 0/71 (0.0 Mio) | 528 / 30 | OK |
| e7_small_encode.txt | 113 | 107 | 105 | – | 0/364 (0.0 Mio) | – | ÉCHEC |
| e7_sub_small_eager.txt | 204 | 429 | 176 | 429 | 0/211 (0.0 Mio) | 892 / 273 | OK |
| e7_sub_small_none.txt | 204 | 340 | 176 | 340 | 0/199 (0.0 Mio) | 690 / 225 | OK |
| e7_tiny_encode.txt | 47 | 831 | 24 | 831 | 0/83 (0.0 Mio) | 988 / 56 | OK |
| e7b_sub_small_eager.txt | 199 | 288 | 176 | 288 | 0/211 (0.0 Mio) | 890 / 280 | OK |
| e7b_sub_small_none.txt | 201 | 254 | 176 | 254 | 0/199 (0.0 Mio) | 703 / 230 | OK |

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
[MLXBackend.cpp:497] MLX execute failed: [scatter_add_axis] Received invalid axis for array with 3 dimensions.
[method.cpp:1530] CALL_DELEGATE execute failed at instruction 0: 0x1
[start] rss 326.6 MiB, phys_footprint 269.5 MiB, lifetime_max 270.0 MiB
[after load_program] rss 333.2 MiB, phys_footprint 275.7 MiB, lifetime_max 275.7 MiB
[after load_method] rss 432.9 MiB, phys_footprint 280.7 MiB, lifetime_max 280.7 MiB
  input 0: sizes=(480000,) scalar_type=6
```

### e8_tiny_encode_mmap.txt
```
[MLXExecutor.h:848] MLX constants: 83 loaded, 0 copied by MLX (0 bytes resident twice)
[start] rss 330.5 MiB, phys_footprint 272.8 MiB, lifetime_max 273.6 MiB
[after load_program] rss 334.7 MiB, phys_footprint 276.9 MiB, lifetime_max 276.9 MiB
[after load_method] rss 357.1 MiB, phys_footprint 277.7 MiB, lifetime_max 278.1 MiB
  input 0: sizes=(480000,) scalar_type=6
[after execute 1] rss 368.0 MiB, phys_footprint 1078.4 MiB, lifetime_max 1078.4 MiB outputs: [(1, 1500, 384)]
[after execute 2] rss 368.5 MiB, phys_footprint 1077.4 MiB, lifetime_max 1079.6 MiB outputs: [(1, 1500, 384)]
[after execute 3] rss 368.6 MiB, phys_footprint 1077.3 MiB, lifetime_max 1079.6 MiB outputs: [(1, 1500, 384)]
```
