# Guardrail Prompting

## Definition
Force the model to only output within strict boundaries.

## Prompt Structure
```
Only output JSON in the following schema:
{ "status": string, "result": string }
```

## Example (Python)
```python
Only output JSON in the following schema:
{ "operation": string, "answer": integer }
Task: Add 2+3
```

## When to Use
Use for production-ready pipelines, API integrations, and ensuring safe/consistent responses.
