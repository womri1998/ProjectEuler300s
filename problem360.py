from math import floor


def square(n):
    i = 0
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
        i += 1
        if i > 100:
            print(n, x, i)
    #print(n, x, i)
    return x, x ** 2 == n


d = {(1, 1): 6, (2, 0): 24, (2, 1): 12, (3, 0): 48, (3, 1): 24, (3, 2): 8}


def duplicates(x, y, z):
    same, positive = (x == y) + (y == z), (x > 0) + (y > 0) + (z > 0)
    return d[(positive, same)]


def s(r):
    total = 0
    i = floor((r ** 2 / 3) ** 0.5)
    for x in range(floor((r ** 2 / 3) ** 0.5), r + 1):
        if x > i:
            print(r - i, i, total)
            i += 10 ** 4
        for y in range(floor(((r ** 2 - x ** 2) / 2) ** 0.5), x + 1):
            z, good = square(r ** 2 - x ** 2 - y ** 2)
            if good:
                total += (x + y + z) * duplicates(x, y, z)
    return total


if __name__ == "__main__":
    print(s(45))
    print(s(10 ** 10))
