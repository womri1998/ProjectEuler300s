def repunits_below(n, base):
    res = set({})
    x = 1 + base + base ** 2
    i = 3
    while x < n:
        res.add(x)
        x += base ** i
        i += 1
    return res


def sum_below(n):
    b = 2
    res = {1}
    while 1 + b + b ** 2 < n:
        if b % 10000 == 0:
            print(1 + b + b ** 2)
        if res.intersection(repunits_below(n, b)) != set({}):
            print(res.intersection(repunits_below(n, b)))
        res = res.union(repunits_below(n, b))
        b += 1
    return sum(res)


def repunits_below2(n, base):
    res = 0
    x = 1 + base + base ** 2
    i = 3
    while x < n:
        res += x
        x += base ** i
        i += 1
    return res


def sum_below2(n):
    b = 2
    res = 1
    while 1 + b + b ** 2 < n:
        res += repunits_below2(n, b)
        b += 1
    return res
