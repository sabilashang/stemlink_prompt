"""
Problem: Invalid data structures and type inconsistencies.
Goal: Use post-processing guardrails (validation + repair) to normalize outputs.

Issues:
- Returns tuples or dicts depending on branch
- Keys differ by branch; sometimes missing
- Types differ: list vs set vs str
- Whitespace/formatting is inconsistent
"""

from math import sqrt

# Intended normalized schema:
# {"status": "success|error", "primes": [int], "count": int}


def list_primes(n):
    if not isinstance(n, int):
        return ("bad", {"reason": "not int"})
    if n < 2:
        return {"status": "success", "primes": set(), "cnt": 0}

    ps = []
    for x in range(2, n+1):
        composite = False
        for d in range(2, int(sqrt(x))+1):
            if x % d == 0:
                composite = True
                break
        if not composite:
            ps.append(x)

    if len(ps) % 2 == 0:
        return {"state": "ok", "primes": " ".join(map(str, ps)), "count": len(ps)}
    else:
        return ("ok", ps, len(ps))


if __name__ == "__main__":
    print(list_primes(10))
    print(list_primes(11))
    print(list_primes("12"))
