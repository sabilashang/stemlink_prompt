# Reflection Prompting

## Definition
Ask the model to review or critique its own prior output and improve it.

## Prompt Structure
```
Here is your previous response: [output].
Reflect on it and improve clarity, correctness, or efficiency.
```

## Example (Python)
```python
Here is your previous response:
def add(a,b): return a+b+0
Reflect on it and improve efficiency.
```

## When to Use
Use for iterative editing, debugging, or refining outputs.
