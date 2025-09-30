"""
Programmatic Prompting with Variables:
Task: Refactor the following function.
Variable: {input_value}
Instruction: Ensure input validation and type hints; keep output identical for
valid inputs. Optimize for readability and maintainability.
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
    print('fact 6 =', factORial(6))
