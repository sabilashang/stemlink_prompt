"""
Problem: Output format drift and inconsistent structure.
Goal: Use prompt-based guardrails (schema + style constraints) to standardize outputs.

Issues:
- Inconsistent return types (sometimes dict, sometimes string)
- Mixed casing of keys
- Extra fields appear unpredictably
- Missing required keys in some paths
"""

import random

# The intended schema is:
# {"status": "success|error", "result": "<summary string>"}

TEMPLATES = [
    {"Status": "OK", "Result": "Done", "extra": 123},
    {"status": "success", "result": ["done"], "note": "x"},
    "success: calculation complete",
    {"status": "error"},
]


def summarize_numbers(nums):
    if not nums:
        return {"status": "success", "result": "no numbers"}
    s = sum(nums)
    avg = s/len(nums)
    if avg > 10:
        return random.choice(TEMPLATES)
    else:
        return {"STATUS": "SUCCESS", "RESULT": f"sum={s}, avg={avg}"}


if __name__ == "__main__":
    print(summarize_numbers([1, 2, 3]))
    print(summarize_numbers([100, 200, 300]))
