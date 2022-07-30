def fibonacci(n):
    x, y = 1, 1
    for i in range(n):
        x, y = x + y, x
    return y


def nimx(x):
    return x ^ (2 * x) ^ (3 * x) == 0


def total(n):
    return sum([nimx(i) for i in range(2 ** n)])
