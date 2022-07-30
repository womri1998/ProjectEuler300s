def square(n):
    i = 0
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
        i += 1
    #print(n, x, i)
    return x ** 2 == n


def possibilities(x, y, z):
    x_zero, y_zero, z_zero = (x == 0), (y == 0), (z == 0)



def stations(r):
    s = set()
    for x in range(int(r / 3 ** 0.5), r + 1):
        for y in range(int(((r ** 2 - x ** 2) / 2) ** 0.5), min(int((r ** 2 - x ** 2) ** 0.5) + 1, x + 1)):
            z = r ** 2 - x ** 2 - y ** 2
            if z <= y and square(z):
                s.add(possibilities(x, y, z))
    return s
