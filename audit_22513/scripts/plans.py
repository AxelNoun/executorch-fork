"""Ordre des execution_plan (méthodes) et de leurs délégués dans un .pte."""
import sys, json, et_ns  # noqa: F401
from executorch.exir._serialize._flatbuffer import _program_flatbuffer_to_json
prog = json.loads(_program_flatbuffer_to_json(open(sys.argv[1], "rb").read()))
for i, plan in enumerate(prog["execution_plan"]):
    dels = [d.get("id") for d in plan.get("delegates", [])]
    ins = plan.get("inputs", []); outs = plan.get("outputs", [])
    print(f"plan {i}: name={plan['name']!r} inputs={len(ins)} outputs={len(outs)} delegates={dels} instructions={sum(len(c.get('instructions', [])) for c in plan.get('chains', []))}")
