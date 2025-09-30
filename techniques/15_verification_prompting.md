# Verification Prompting

## Definition
Ask the model to verify correctness of an output before finalizing.

## Prompt Structure
```
Here is the solution: [output].
Verify if it is correct. If not, correct it.
```

## Example (Python)
```python
Here is the solution: factorial(5) = 100.
Verify if it is correct. If not, correct it.
```

## When to Use
Use for guardrails, accuracy checks, and double-layer outputs.
