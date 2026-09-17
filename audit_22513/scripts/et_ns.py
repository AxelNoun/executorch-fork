# Module 'executorch' synthétique pointant sur un worktree (aucune installation) ; torchao via worktree.
import os, sys, types
ET = os.environ.get("ET_ROOT"); AO = os.environ.get("AO_ROOT")
if AO and AO not in sys.path: sys.path.insert(0, AO)
if ET:  # sans ET_ROOT, on laisse le paquet executorch installé (cas du runner CI)
    m = types.ModuleType("executorch"); m.__path__ = [ET]; sys.modules["executorch"] = m
if AO:
    import torchao
    if getattr(torchao, "__version__", "unknown") == "unknown":
        # worktree git sans métadonnées : transformers.is_torchao_available() exige une version PEP 440
        torchao.__version__ = open(os.path.join(AO, "version.txt")).read().strip()
