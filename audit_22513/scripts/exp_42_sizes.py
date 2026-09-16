"""
4.2.1 — tailles des intermédiaires de l'encodeur Whisper-small (bf16) par nœud aten, export torch.export
strict + run_decompositions({}) (même IR que ce que le builder MLX consomme). Poids aléatoires, graine 0.
Usage : python exp_42_sizes.py <attn:sdpa|eager> <layers>
"""
import sys, torch, collections
from transformers import WhisperConfig, WhisperForConditionalGeneration
attn, layers = sys.argv[1], int(sys.argv[2])
torch.manual_seed(0)
cfg = WhisperConfig(d_model=768, encoder_attention_heads=12, encoder_layers=layers, encoder_ffn_dim=3072,
                    decoder_layers=1, decoder_attention_heads=12, decoder_ffn_dim=3072, num_mel_bins=80,
                    max_source_positions=1500, vocab_size=51865)
m = WhisperForConditionalGeneration._from_config(cfg, dtype=torch.bfloat16, attn_implementation=attn).eval()
class Enc(torch.nn.Module):
    def __init__(self, e): super().__init__(); self.encoder = e
    def forward(self, x): return self.encoder(input_features=x).last_hidden_state
with torch.no_grad():
    ep = torch.export.export(Enc(m.get_encoder()).eval(), (torch.zeros(1, 80, 3000, dtype=torch.bfloat16),), strict=True).run_decompositions({})
VIEWS = {"aten.view.default", "aten.permute.default", "aten.transpose.int", "aten.t.default", "aten.reshape.default", "aten.unsqueeze.default", "aten.squeeze.dim", "aten.expand.default", "aten.slice.Tensor", "aten.alias.default", "aten.detach.default", "aten.view_copy.default", "aten.permute_copy.default"}
rows = []; total = 0; mat_total = 0
for n in ep.graph.nodes:
    if n.op != "call_function": continue
    v = n.meta.get("val")
    if not isinstance(v, torch.Tensor): continue
    nb = v.numel() * v.element_size(); tgt = str(n.target)
    materialized = tgt not in VIEWS and v.numel() > 1
    rows.append((n.name, tgt, tuple(v.shape), str(v.dtype).replace("torch.", ""), nb, materialized))
    if materialized: mat_total += nb
    total += nb
print(f"attn={attn} layers={layers} nodes={len(rows)} somme(tous)={total/2**20:.1f} MiB somme(matérialisés, hors vues)={mat_total/2**20:.1f} MiB")
# top des plus gros nœuds matérialisés + tableau d'une couche (nœuds ≥ 1 MiB)
big = collections.Counter()
for name, tgt, shape, dt, nb, mat in rows:
    if mat: big[(tgt, shape, dt, nb)] += 1
print("\nnœuds matérialisés ≥ 1 MiB (op, shape, dtype, MiB, occurrences, total MiB):")
for (tgt, shape, dt, nb), c in sorted(big.items(), key=lambda kv: -kv[0][3] * kv[1]):
    if nb >= 2**20: print(f"  {tgt:40s} {str(shape):26s} {dt:9s} {nb/2**20:8.2f}  x{c:3d}  = {c*nb/2**20:9.1f}")
print("\nséquence de la 1re couche (nœuds matérialisés ≥ 1 MiB, ordre du graphe) :")
seen = 0
for name, tgt, shape, dt, nb, mat in rows:
    if mat and nb >= 2**20:
        print(f"  {name:28s} {tgt:38s} {str(shape):26s} {dt:9s} {nb/2**20:8.2f} MiB"); seen += 1
    if seen >= (17 if attn == "eager" else 14): break
