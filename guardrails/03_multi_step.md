# Multi-Step Guardrails

## Definition
The AI evaluates and corrects its own outputs in multiple steps. A typical loop: generate → check → correct → finalize. You can orchestrate the steps or ask the model to follow a checklist.

## Example Workflow
1. Generate initial code from a prompt.
2. Run checks (tests, linters, static analysis).
3. Ask model to fix issues based on error logs.
4. Repeat until passing or a max iteration count.

## Prompt Template (Text)
```
Step 1: Generate the function requested.
Step 2: Inspect the following errors and propose fixes.
Step 3: Output the corrected code only, no explanations.
```

## Python Example
```python
import subprocess
import tempfile
import textwrap

initial_code = textwrap.dedent('''
    def sum_list(xs):
        t=0
        for x in xs:
            t=t+x
        return t
''')

# Step 1: Write code to a temp file
with tempfile.NamedTemporaryFile(suffix='.py', delete=False, mode='w') as f:
    f.write(initial_code)
    path = f.name

# Step 2: Run a check (simulate tests)
proc = subprocess.run(['python', '-m', 'pyflakes', path], capture_output=True, text=True)
errors = proc.stderr + proc.stdout

if errors:
    # Step 3: Provide errors back to the model (pseudo-call) and request corrected code
    model_prompt = f"""
    The following Python code has issues. Fix them and return corrected code only.

    CODE:
    {initial_code}

    ERRORS:
    {errors}
    """
    # Pseudo: corrected_code = call_model(model_prompt)
    corrected_code = initial_code  # placeholder: in practice, replace with model output
    print(corrected_code)
else:
    print(initial_code)
```

Use guards like max iterations and schema checks on each loop to prevent infinite retries or format drift.
