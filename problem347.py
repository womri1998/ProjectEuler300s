def gen_primes(n):
    done = 0
    primes = []
    generating = []
    while n != 0:
        if n < 10 ** 6:
            suspects = [True] * n
            suspects2 = [True] * n
            n = 0
        else:
            suspects = [True] * 10 ** 6
            suspects2 = [True] * 10 ** 6
            n -= 10 ** 6
        if done == 0:
            suspects[0], suspects[1] = False, False
        for p in primes:
            r = 0 if done % p == 0 else p - done % p
            for i in range(r, len(suspects), p):
                suspects[i] = False
                x = p + (i + done) // p
                if x not in primes or (x >= done and not suspects[x - done]):
                    suspects2[i] = False
        for i in range(len(suspects)):
            if suspects[i]:
                for j in range(2 * i + done, len(suspects), i + done):
                    suspects[j] = False
                    x = (i + done) + (j + done) // (i + done)
                    if x not in primes or (x >= done and not suspects[x - done]):
                        suspects2[j] = False
        primes += [i + done for i in range(len(suspects)) if suspects[i]]
        generating += [i + done for i in range(len(suspects2)) if suspects2[i]]
        done += 10 ** 6
        print(done)
    return generating, sum(generating)
