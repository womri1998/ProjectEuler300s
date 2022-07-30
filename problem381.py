def gen_primes(n):
    done = 0
    primes = []
    while n != 0:
        if n < 10 ** 6:
            suspects = [True] * n
            n = 0
        else:
            suspects = [True] * 10 ** 6
            n -= 10 ** 6
        if done == 0:
            suspects[0], suspects[1] = False, False
        for p in primes:
            r = 0 if done % p == 0 else p - done % p
            for i in range(r, len(suspects), p):
                suspects[i] = False
        for i in range(len(suspects)):
            if suspects[i]:
                for j in range(2 * i + done, len(suspects), i + done):
                    suspects[j] = False
        primes += [i + done for i in range(len(suspects)) if suspects[i]]
        done += 10 ** 6
        print(done)
    return primes


primes = gen_primes(10 ** 8)


def euclid(n, m):
    if n < m:
        n, m = m, n
    x, y = (n, 1, 0), (m, 0, 1)
    while y[0] != 0:
        k = x[0] // y[0]
        x, y = y, (x[0] % y[0], x[1] - k * y[1], x[2] - k * y[2])
    return x


def s(p):
    cur = -1
    res = -1
    for i in range(1, 5):
        cur = (cur * euclid(p, p - i)[2]) % p
        res += cur
    return res % p


def total(n):
    tot = 0
    for p in primes[2:]:
        if p >= n:
            break
        tot += s(p)
    return tot
