# Programmatic Prompting with Variables

## Definition
Embed variables into prompts dynamically to scale across inputs.

## Prompt Structure
```
Task: [task description]
Variable: {input_variable}
Instruction: [what to do with variable]
```

## Example (Python)
```python
Task: Write a Python function.
Variable: {number_list}
Instruction: Sort the list in ascending order.
```

## When to Use
Use for automation, batch tasks, or API-driven prompting.
