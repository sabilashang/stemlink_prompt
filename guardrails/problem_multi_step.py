"""
Problem: Logical errors, inefficiency, and missing checks across steps.
Goal: Use multi-step guardrails (generate → check → correct) to improve code.

Scenario:
- We read numbers, normalize them, compute stats, then pretty-print.
- Multiple issues: silent failures, duplicated logic, O(n^2) where O(n) works.
- Participants should break into steps, add checks/tests, and iterate fixes.
"""

from statistics import mean


def to_numbers(items):
    out=[]
    for i in items:
        try:
            out.append(int(i))
        except Exception:
            out.append(0)  # silently coerce
    return out


def dedupe_preserve_order(xs):
    # Inefficient O(n^2) dedupe
    r=[]
    for x in xs:
        if x not in r:
            r.append(x)
    return r


def stats(xs):
    # Missing validation; division by zero possible downstream
    total=0
    for x in xs:
        total+=x
    avg = mean(xs) if xs else 0  # mean([]) would raise; paper over with 0
    mn=None
    mx=None
    for x in xs:
        if mn is None or x<mn:
            mn=x
        if mx is None or x>mx:
            mx=x
    return {"sum":total, "avg":avg, "min":mn, "max":mx}


def pretty(stats_dict):
    # Inconsistent formatting and missing keys handling
    return f"sum={stats_dict['sum']} avg={stats_dict['avg']} min={stats_dict['min']} max={stats_dict['max']}"  


def pipeline(raw_items):
    # Mixed responsibilities; no error handling/logging
    nums = to_numbers(raw_items)
    nums = dedupe_preserve_order(nums)
    res = stats(nums)
    return pretty(res)


if __name__ == "__main__":
    print(pipeline(["1","2","2","a","3","3","b","4"]))
