"""
Chain-of-Thought Prompting:
Let's reason step by step about how to refactor the factorial function below.
Consider: input validation, base cases, loop structure, naming, type hints,
and error handling. Then produce the improved implementation.
"""

# same messy factorial implementation as v1


def factORial(N):
    z = 1
    if N == 0:
        return 1
    if N < 0:
        return None
    i = 1
    while True:
        if i > N:
            break
        z = z * i
        i = i+1
    return z


if __name__ == "__main__":
    print('fact 7 =', factORial(7))
