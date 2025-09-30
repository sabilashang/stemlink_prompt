# Few-Shot Prompting

## Definition
Provide multiple examples to demonstrate the task before asking the model to continue.

## Prompt Structure
```
Input: [example 1]
Output: [solution 1]

Input: [example 2]
Output: [solution 2]

Now complete the next one:
Input: [new task]
Output:
```

## Example (Python)
```python
Input: "2+3"
Output: 5

Input: "4+7"
Output: 11

Now complete the next one:
Input: "6+8"
Output:
```

## When to Use
Use when you need consistency across multiple samples or formats.
