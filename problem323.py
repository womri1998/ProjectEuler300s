from math import factorial


def pnk(p, n, k): # binomial distribution
    return factorial(n) // factorial(k) // factorial(n - k) * p ** k * (1 - p) ** (n - k)


was = [0]


def next_bit(n):
    return (sum([pnk(0.5, n, i) * was[i] for i in range(n)]) + 1) / (1 - 1 / 2 ** n)


def build(n):
    for i in range(n):
        was.append(next_bit(i + 1))
    return was
