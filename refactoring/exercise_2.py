# Messy prime checker (no hints; for independent practice)
def pr1me(x):
    if x == 2:
        return True
    if x < 2:
        return False
    d = 2
    while d < x:
        if x % d == 0:
            return False
        d = d+1
    return True


if __name__ == "__main__":
    print('is 29 prime?', pr1me(29))
