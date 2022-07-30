from fractions import Fraction


def gen_primes(n):
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False
    for i in range(n + 1):
        if primes[i]:
            for j in range(2 * i, n + 1, i):
                primes[j] = False
    return primes


was = {}
prime = gen_primes(500)
wanted = (1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0)


def good(cur, left):
    return not prime[cur] ^ wanted[-left]


def probability(cur, left):
    x = Fraction(1 + good(cur, left), 3)
    if left == 1:
        return x
    elif (cur, left) in was:
        return was[(cur, left)]
    elif cur == 1:
        x *= probability(2, left - 1)
    elif cur == 500:
        x *= probability(499, left - 1)
    else:
        x *= Fraction(1, 2) * (probability(cur - 1, left - 1) + probability(cur + 1, left - 1))
    was[(cur, left)] = x
    return x


def res():
    return Fraction(sum([probability(i, len(wanted)) for i in range(1, 501)]), 500)
