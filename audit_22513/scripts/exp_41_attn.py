"""
Expérience 4.1 — l'encodeur Whisper (HF transformers) émet-il aten.scaled_dot_product_attention
sous torch.export + run_decompositions({}) ?

Consomme : rien (poids aléatoires, config whisper-small, graine fixe).
Produit  : comptage d'ops par configuration d'attention sur stdout.
Hypothèse : le chemin d'export du dépôt (export_whisper.py) = torch.export strict + run_decompositions({}).
"""
import collections, sys, torch, transformers
from transformers import WhisperConfig, WhisperForConditionalGeneration

torch.manual_seed(0)
print("torch", torch.__version__, "transformers", transformers.__version__)

# config whisper-small (openai/whisper-small config.json) — d_model 768, 12 heads, 12 enc layers,
# 3000 frames -> 1500 positions ; réduite en couches pour le temps d'export mais mêmes dims d'attention.
cfg = WhisperConfig(
    d_model=768, encoder_attention_heads=12, encoder_layers=int(sys.argv[1]) if len(sys.argv) > 1 else 2,
    encoder_ffn_dim=3072, decoder_layers=1, decoder_attention_heads=12, decoder_ffn_dim=3072,
    num_mel_bins=80, max_source_positions=1500, vocab_size=51865,
)

class Enc(torch.nn.Module):
    def __init__(self, enc): super().__init__(); self.encoder = enc
    def forward(self, input_features):
        return self.encoder(input_features=input_features).last_hidden_state

def count(ep):
    c = collections.Counter()
    for n in ep.graph.nodes:
        if n.op == "call_function":
            c[str(n.target)] += 1
    return c

KEYS = ("scaled_dot_product_attention", "bmm", "matmul", "_softmax", "softmax", "mm.default", "linear", "baddbmm")
for attn in (None, "sdpa", "eager"):
    kw = {} if attn is None else {"attn_implementation": attn}
    m = WhisperForConditionalGeneration(cfg, **kw) if attn is None else WhisperForConditionalGeneration._from_config(cfg, attn_implementation=attn)
    m.eval()
    print(f"\n=== attn_implementation passé = {attn!r} -> config._attn_implementation = {m.config._attn_implementation!r}")
    enc = Enc(m.get_encoder()).eval()
    x = torch.zeros(1, 80, 3000)
    with torch.no_grad():
        ep = torch.export.export(enc, (x,), dynamic_shapes=None, strict=True)
        c0 = count(ep)
        ep = ep.run_decompositions({})
        c1 = count(ep)
    for label, c in (("torch.export (pré run_decompositions)", c0), ("après run_decompositions({})", c1)):
        sel = {k: v for k, v in c.items() if any(s in k for s in KEYS)}
        print(f"  [{label}] total call_function={sum(c.values())}  {sel}")
