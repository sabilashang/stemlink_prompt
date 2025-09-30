# Prompt-Based Guardrails

## Definition
Guardrails embedded directly in the prompt to enforce rules, constraints, or output format. You specify the allowed schema, style, or prohibitions so the model responds within safe, predictable boundaries.

## Prompt Structure
```
System/Instruction:
- Follow these constraints strictly.
- Only output in the requested format.
- Do not include prohibited content.

Task: [what the model should do]
Format: [e.g., JSON schema, bullet list, fixed template]
Prohibitions: [e.g., no PII, no shell commands, no external links]
```

## Example Usage

### JSON Output Constraint
```
Only output JSON using this schema exactly (no extra keys):
{
  "status": "success|error",
  "result": "string"
}
Task: Summarize this function in one sentence.
```

### Fixed Style Constraint
```
Answer in exactly three bullet points, each under 12 words.
Task: Explain what this code does.
```

### Prohibited Content Constraint
```
Do not include: file paths, credentials, or hyperlinks.
Task: Describe how the function validates input.
```

## Python Coding Example
Suppose we have a function that reverses strings. We want a docstring in a specific style and a JSON-only response.

### Prompt Template
```
You are a Python style enforcer. Follow the constraints strictly.
- Only output JSON with keys: {"docstring", "notes"}; no extra keys.
- Use Google-style docstrings.
- Do not include file paths or links.

Task: Write a docstring for the function below and one note about edge cases.

"""
def reverse_text(text):
    r = ''
    for i in range(len(text)-1, -1, -1):
        r += text[i]
    return r
"""
```

### Expected Model Output
```json
{
  "docstring": """Reverse the input text.

Args:
    text (str): Input string.

Returns:
    str: Text reversed character by character.
""",
  "notes": "Handle empty strings and non-ASCII characters."
}
```
