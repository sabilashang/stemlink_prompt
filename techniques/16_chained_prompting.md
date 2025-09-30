# Chained Prompting (Multi-Prompt Pipelines)

## Definition
Break a big task into multiple smaller prompts in sequence.

## Prompt Structure
```
Task Part 1: [subtask]
Task Part 2: [subtask]
Task Part 3: [subtask]
```

## Example (Python)
```python
Task Part 1: Extract functions from messy code.
Task Part 2: Optimize each function.
Task Part 3: Document code clearly.
```

## When to Use
Use for complex tasks that need modular handling.
