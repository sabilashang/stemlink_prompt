# Messy Fibonacci (no hints; for independent practice)
def fib(n):
    a = 0
    b = 1
    c = None
    if n == 0:
        return 0
    if n < 0:
        return 'no'
    if n == 1:
        return 1
    k = 2
    while k <= n:
        c = a+b
        a = b
        b = c
        k = k+1
    return c


if __name__ == "__main__":
    print('fib 8 =', fib(8))
