"""
Role Prompting:
You are a senior Python engineer. Your task is to refactor the function below
for clarity, correctness, and performance. Add a docstring, type hints, and
raise informative errors for invalid inputs. Keep behavior equivalent.
"""

# intentionally messy factorial implementation


def factORial(N):
    z = 1
    if N == 0:
        return 1
    if N < 0:
        return None  # bad behavior, should raise
    i = 1
    while True:
        if i > N:
            break
        z = z * i
        i = i+1
    return z


if __name__ == "__main__":
    # quick demo
    print('fact 5 =', factORial(5))
