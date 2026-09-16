"""
Simulation du découpage en command buffers MLX (v0.32.0) pour la chaîne encode du fichier du rapporteur
(whisper-small, bf16 + LN/softmax fp32, attention non fusionnée), et pour la variante SDPA fusionnée.
Règles (device.cpp:343-349, 405-419, 512-515) : commit quand buffer_ops_ > max_ops OU (buffer_sizes_ >> 20) > max_mb ;
buffer_sizes_ = somme des data_size() (ÉLÉMENTS, pas octets) des tableaux liés, dédupliqués par pointeur de buffer.
Hypothèse : 1 dispatch par op ; poids liés une fois par op (dédup dans le même command buffer si réutilisés).
"""
import sys
L, D, H, F = 1500, 768, 12, 3072
T = L * D            # 1 152 000 éléments (hidden)
S = H * L * L        # 27 000 000 éléments (scores)
W = D * D            # poids d'une projection (éléments logiques ; int8 packé = D*D/4 uint32 mais on garde D*D)
Wf = D * F
def layer_unfused():
    # (nom, entrées[(id, elems)], sortie(id, elems), octets_sortie)
    ops = [
        ("astype32", [("x",T)], ("x32",T), 4*T),
        ("layernorm", [("x32",T),("g",D),("b",D)], ("ln32",T), 4*T),
        ("astype16", [("ln32",T)], ("ln",T), 2*T),
        ("qmm_q", [("ln",T),("Wq",W)], ("q",T), 2*T), ("add_bq", [("q",T),("bq",D)], ("q2",T), 2*T),
        ("qmm_k", [("ln",T),("Wk",W)], ("k",T), 2*T),
        ("qmm_v", [("ln",T),("Wv",W)], ("v",T), 2*T), ("add_bv", [("v",T),("bv",D)], ("v2",T), 2*T),
        ("mul_q", [("q2",T)], ("qs",T), 2*T), ("mul_k", [("k",T)], ("ks",T), 2*T),
        ("addmm_qk", [("qs",T),("ks",T)], ("qk",S), 2*S),
        ("astype_qk32", [("qk",S)], ("qk32",S), 4*S),
        ("softmax", [("qk32",S)], ("w32",S), 4*S),
        ("astype_w16", [("w32",S)], ("w",S), 2*S),
        ("addmm_wv", [("w",S),("v2",T)], ("o",T), 2*T),
        ("copy_o", [("o",T)], ("oc",T), 2*T),
        ("qmm_o", [("oc",T),("Wo",W)], ("p",T), 2*T), ("add_bo", [("p",T),("bo",D)], ("p2",T), 2*T),
        ("add_res", [("x",T),("p2",T)], ("y",T), 2*T),
        ("astype32b", [("y",T)], ("y32",T), 4*T), ("layernorm2", [("y32",T),("g2",D),("b2",D)], ("ln2_32",T), 4*T),
        ("astype16b", [("ln2_32",T)], ("ln2",T), 2*T),
        ("qmm_fc1", [("ln2",T),("W1",Wf)], ("h",L*F), 2*L*F), ("add_b1", [("h",L*F),("b1",F)], ("h2",L*F), 2*L*F),
        ("gelu", [("h2",L*F)], ("h3",L*F), 2*L*F),
        ("qmm_fc2", [("h3",L*F),("W2",Wf)], ("z",T), 2*T), ("add_b2", [("z",T),("b2f",D)], ("z2",T), 2*T),
        ("add_res2", [("y",T),("z2",T)], ("x_next",T), 2*T),
    ]
    return ops
def layer_fused():
    ops = [o for o in layer_unfused() if o[0] not in ("mul_q","mul_k","addmm_qk","astype_qk32","softmax","astype_w16","addmm_wv")]
    i = [k for k,o in enumerate(ops) if o[0]=="add_bv"][0]
    ops.insert(i+1, ("sdpa", [("q2",T),("k",T),("v2",T)], ("o",T), 2*T))
    return ops
def simulate(layers, mk, max_ops, max_mb, label):
    cbufs = []; ops_in = 0; elems = 0; bytes_in = 0; seen = set()
    for l in range(layers):
        for name, ins, out, ob in mk():
            for bid, n in ins:
                key = (l, bid) if not bid[0].isupper() and bid not in ("g","b","g2","b2","bq","bv","bo","b1","b2f") else (l, bid)
                if key not in seen: seen.add(key); elems += n
            key = (l, out[0])
            if key not in seen: seen.add(key); elems += out[1]
            ops_in += 1; bytes_in += ob
            if ops_in > max_ops or (elems >> 20) > max_mb:
                cbufs.append((ops_in, elems, bytes_in)); ops_in = 0; elems = 0; bytes_in = 0; seen = set()
    if ops_in: cbufs.append((ops_in, elems, bytes_in))
    tot = sum(b for _,_,b in cbufs)
    win = 11  # MAX_ACTIVE_TASKS=10 -> jusqu'à 11 command buffers commis non terminés (+ celui en cours)
    worst = max(sum(b for _,_,b in cbufs[i:i+win]) for i in range(len(cbufs))) if cbufs else 0
    print(f"{label}: {len(cbufs)} command buffers pour {layers} couches ; volume alloué total {tot/1e6:.0f} MB ; "
          f"fenêtre de {win} cbufs max = {worst/1e6:.0f} MB ; médiane ops/cbuf={sorted(o for o,_,_ in cbufs)[len(cbufs)//2]}")
for (mo, mm, dev) in ((20, 40, "phone 'p'"), (40, 40, "base/pro 'g'"), (50, 50, "max/ultra 's'/'d'")):
    simulate(12, layer_unfused, mo, mm, f"non fusionné {dev:18s}")
for (mo, mm, dev) in ((20, 40, "phone 'p'"), (40, 40, "base/pro 'g'")):
    simulate(12, layer_fused, mo, mm, f"SDPA fusionné {dev:16s}")
