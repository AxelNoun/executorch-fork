"""
Expérience 4.1 (suite) — lowering MLX d'un encodeur Whisper (poids aléatoires) avec le pipeline du dépôt.

Consomme : rien (config whisper-tiny ou whisper-small, graine 0). Produit : <out>/encoder_<attn>_<dtype>_L<layers>[_<cfg>][_fp32in].pte
+ comptage d'ops. Hypothèse : même pipeline que backends/mlx/examples/whisper/export_whisper.py::_save_to_pte.
Usage : python exp_41_lower.py <attn:none|sdpa|eager> <layers> <dtype:bf16|fp32> <outdir> [--config small|tiny] [--fp32-input]
  --fp32-input : l'entrée du .pte est fp32 (cast bf16 dans le graphe), comme le fichier du rapporteur ; nécessaire
                 pour alimenter le modèle depuis Swift (pas de Tensor<BFloat16>) — harnais iOS audit_22513/ios/.
"""
import argparse, os, sys, collections, time, torch
from transformers import WhisperConfig, WhisperForConditionalGeneration  # avant et_ns : sinon transformers voit torchao sans métadonnées
import et_ns  # noqa: F401
import executorch.exir as exir
from executorch.backends.mlx import MLXPartitioner
from executorch.backends.mlx.passes import get_default_passes
from executorch.exir import EdgeCompileConfig
from executorch.exir.capture._config import ExecutorchBackendConfig

ap = argparse.ArgumentParser()
ap.add_argument("attn"); ap.add_argument("layers", type=int); ap.add_argument("dtype"); ap.add_argument("outdir")
ap.add_argument("--config", default="small", choices=["small", "tiny"])
ap.add_argument("--fp32-input", action="store_true")
a = ap.parse_args()
attn, layers, dtype, outdir = a.attn, a.layers, a.dtype, a.outdir
torch.manual_seed(0)
tdt = {"bf16": torch.bfloat16, "fp32": torch.float32}[dtype]
CFG = {  # openai/whisper-{small,tiny} config.json
    "small": dict(d_model=768, encoder_attention_heads=12, encoder_ffn_dim=3072, decoder_attention_heads=12, decoder_ffn_dim=3072),
    "tiny": dict(d_model=384, encoder_attention_heads=6, encoder_ffn_dim=1536, decoder_attention_heads=6, decoder_ffn_dim=1536),
}[a.config]
cfg = WhisperConfig(encoder_layers=layers, decoder_layers=1, num_mel_bins=80, max_source_positions=1500, vocab_size=51865, **CFG)
kw = {} if attn == "none" else {"attn_implementation": attn}
model = WhisperForConditionalGeneration._from_config(cfg, torch_dtype=tdt, **kw).eval()
print("config._attn_implementation =", model.config._attn_implementation)

class Enc(torch.nn.Module):
    def __init__(self, enc, cast_to):
        super().__init__(); self.encoder = enc; self.cast_to = cast_to
    def forward(self, input_features):
        if self.cast_to is not None:
            input_features = input_features.to(self.cast_to)
        return self.encoder(input_features=input_features).last_hidden_state

enc = Enc(model.get_encoder(), tdt if a.fp32_input else None).eval()
x = torch.zeros(1, 80, 3000, dtype=torch.float32 if a.fp32_input else tdt)
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
suffix = ("" if a.config == "small" else f"_{a.config}") + ("_fp32in" if a.fp32_input else "")
path = os.path.join(outdir, f"encoder_{attn}_{dtype}_L{layers}{suffix}.pte")
with open(path, "wb") as f: f.write(prog.buffer)
print(f"écrit {path} ({len(prog.buffer)/1e6:.1f} MB) en {time.time()-t0:.0f}s")
g = edge.exported_program().graph
rest = collections.Counter(str(n.target) for n in g.nodes if n.op == "call_function" and "executorch_call_delegate" not in str(n.target))
print("hors délégué:", dict(rest))
