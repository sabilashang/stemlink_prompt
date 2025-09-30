# Delimiting Prompting

## Definition
Use clear boundaries (like triple quotes) to isolate task-relevant text.

## Prompt Structure
```
Process only the text between triple quotes:
""" [text] """
```

## Example (Python)
```python
Process only the text between triple quotes:
""" def add(a, b): return a+b """
```

## When to Use
Use to prevent the model from using unintended input context.
