from fractions import Fraction
from math import factorial


def prob(n, k, p):
    return factorial(n) // factorial(k) // factorial(n - k) * p ** k * (1 - p) ** (n - k)


def d_distribution(d):
