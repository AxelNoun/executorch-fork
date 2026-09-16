"""
Expérience 4.1 (suite) — lowering MLX de l'encodeur Whisper-small (poids aléatoires) à ET v1.4.1.

Consomme : rien (config whisper-small, graine 0). Produit : <out>/encoder_<attn>_<dtype>.pte + comptage d'ops MLX.
Hypothèse : même pipeline que backends/mlx/examples/whisper/export_whisper.py::_save_to_pte (v1.4.1).
Usage : python exp_41_lower.py <attn:none|sdpa|eager> <layers> <dtype:bf16|fp32> <outdir>
"""
import os, sys, collections, time, torch
from transformers import WhisperConfig, WhisperForConditionalGeneration  # avant et_ns : sinon transformers voit torchao sans métadonnées
import et_ns  # noqa: F401
import executorch.exir as exir
from executorch.backends.mlx import MLXPartitioner
from executorch.backends.mlx.passes import get_default_passes
from executorch.exir import EdgeCompileConfig
from executorch.exir.capture._config import ExecutorchBackendConfig

attn, layers, dtype, outdir = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
torch.manual_seed(0)
tdt = {"bf16": torch.bfloat16, "fp32": torch.float32}[dtype]
cfg = WhisperConfig(d_model=768, encoder_attention_heads=12, encoder_layers=layers, encoder_ffn_dim=3072,
                    decoder_layers=1, decoder_attention_heads=12, decoder_ffn_dim=3072, num_mel_bins=80,
                    max_source_positions=1500, vocab_size=51865)
kw = {} if attn == "none" else {"attn_implementation": attn}
model = WhisperForConditionalGeneration._from_config(cfg, torch_dtype=tdt, **kw).eval()
print("config._attn_implementation =", model.config._attn_implementation)

class Enc(torch.nn.Module):
    def __init__(self, enc): super().__init__(); self.encoder = enc
    def forward(self, input_features):
        return self.encoder(input_features=input_features).last_hidden_state

enc = Enc(model.get_encoder()).eval()
x = torch.zeros(1, 80, 3000, dtype=tdt)
t0 = time.time()
with torch.no_grad():
    ep = torch.export.export(enc, (x,), dynamic_shapes=None, strict=True)
    ep = ep.run_decompositions({})
c = collections.Counter(str(n.target) for n in ep.graph.nodes if n.op == "call_function")
print("aten ops (sélection):", {k: v for k, v in c.items() if any(s in k for s in ("scaled_dot", "matmul", "bmm", "softmax", "linear"))})

edge = exir.to_edge_transform_and_lower(ep, transform_passes=get_default_passes(), partitioner=[MLXPartitioner()],
                                        compile_config=EdgeCompileConfig(_check_ir_validity=False, _skip_dim_order=True))
prog = edge.to_executorch(config=ExecutorchBackendConfig(extract_delegate_segments=True))
os.makedirs(outdir, exist_ok=True)
path = os.path.join(outdir, f"encoder_{attn}_{dtype}_L{layers}.pte")
with open(path, "wb") as f: f.write(prog.buffer)
print(f"écrit {path} ({len(prog.buffer)/1e6:.1f} MB) en {time.time()-t0:.0f}s")
# nœuds restant hors délégué (portable)
g = edge.exported_program().graph
rest = collections.Counter(str(n.target) for n in g.nodes if n.op == "call_function" and "executorch_call_delegate" not in str(n.target))
print("hors délégué:", dict(rest))
