# Multi-Turn Prompting

## Definition
Build context step by step across multiple back-and-forth turns.

## Prompt Structure
```
Step 1: [ask model a subtask]
Step 2: [follow-up question building on context]
```

## Example (Python)
```python
# Step 1
"Summarize the code."
# Step 2
"Now optimize the algorithm."
```

## When to Use
Use for complex workflows that cannot fit in a single prompt.
