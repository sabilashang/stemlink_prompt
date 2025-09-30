# Post-Processing Guardrails

## Definition
Validate or correct AI outputs programmatically after generation. Treat model output as untrusted input: parse, validate, repair, and re-run if needed.

## Typical Steps
1. Generate the output (e.g., text/JSON/code) from the model.
2. Parse and validate against schemas or rules.
3. If invalid, correct it automatically or request regeneration with error hints.

## Python: Validate JSON Output
```python
import json
from typing import Any, Dict

ALLOWED_KEYS = {"status", "result"}
ALLOWED_STATUS = {"success", "error"}

def validate_payload(raw: str) -> Dict[str, Any]:
    # Attempt to parse JSON; if parsing fails, wrap as error
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        return {"status": "error", "result": f"Invalid JSON: {exc}"}

    # Validate keys
    extra = set(data.keys()) - ALLOWED_KEYS
    if extra:
        return {"status": "error", "result": f"Unexpected keys: {sorted(extra)}"}

    # Validate status
    if data.get("status") not in ALLOWED_STATUS:
        return {"status": "error", "result": "Invalid status value"}

    # Validate result
    if not isinstance(data.get("result"), str):
        return {"status": "error", "result": "`result` must be a string"}

    return data
```

## Example: Correct Messy AI Output
Suppose the model returned this (not strictly valid):
```json
{"state": "ok", "result": [1,2,3], "extra": true}
```
We can coerce it using post-processing:
```python
raw = '{"state": "ok", "result": [1,2,3], "extra": true}'
# Attempt a repair strategy
repaired = {
    "status": "success" if '"state": "ok"' in raw else "error",
    "result": "[1, 2, 3]"  # coerce to string for schema
}
validated = validate_payload(json.dumps(repaired))
print(validated)
# => {"status": "success", "result": "[1, 2, 3]"}
```

## Coding Example with Code Output
If the model emits Python code with a missing function or syntax error, you can run a static check and auto-fix simple issues.
```python
bad_code = "def add(a,b):\n return a+b+\n"

# Simple correction heuristic: remove trailing '+' at line end
fixed_code = "\n".join(
    line.rstrip('+') if line.strip().endswith('+') else line
    for line in bad_code.splitlines()
)

# Optionally run `ast.parse` for syntax validation
import ast
try:
    ast.parse(fixed_code)
    print("Code is syntactically valid after repair.")
except SyntaxError as e:
    print("Still invalid:", e)
```
