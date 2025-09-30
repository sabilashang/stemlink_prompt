# Role Prompting

## Definition
Instruct the model to assume a role or persona to shape style, tone, or expertise.

## Prompt Structure
```
You are a [role]. Your task is [objective].
```

## Example (Python)
```python
You are a Python tutor. Refactor this function to be more efficient:
def reverse_string(s):
    x = ''
    for i in range(len(s)-1, -1, -1):
        x += s[i]
    return x
```

## When to Use
Use it to control tone, enforce expertise, or align outputs with domain knowledge.
