# Chain-of-Thought Prompting

## Definition
Encourages the model to explain its reasoning steps before answering.

## Prompt Structure
```
Let's reason step by step: [problem statement]
```

## Example (Python)
```python
# Prompt
"""
Let's reason step by step: How can we calculate the factorial of 6 in Python?
"""
# Expected behavior: model explains reasoning then provides code.
```

## When to Use
Use for math, logic, or debugging tasks that benefit from transparent reasoning.
