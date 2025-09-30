# Style/Format Constrained Prompting

## Definition
Force the output into a specific format, tone, or length.

## Prompt Structure
```
Answer in [format/style]: [instruction]
```

## Example (Python)
```python
# Instruction to the model
Answer in JSON format:
{ "result": 42 }
```

## When to Use
Use for APIs, structured outputs, or enforcing business rules.
