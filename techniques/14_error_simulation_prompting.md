# Error Simulation Prompting

## Definition
Introduce mistakes intentionally and ask the model to correct them.

## Prompt Structure
```
Here’s a buggy version of code: [insert]. Correct it.
```

## Example (Python)
```python
Here’s a buggy version of code:
def add(a,b): return a-b
Correct it.
```

## When to Use
Use for debugging, teaching, or resilience training.
