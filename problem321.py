def pel(x):
    return 3 * x[0] + 8 * x[1], x[0] + 3 * x[1]


def res():
    count, res = 1, 1
    x, y = (1, 1), (5, 2)
    while count < 40:
        x, y = pel(x), pel(y)
        res += x[1] - 1
        count += 1
        if count == 40:
            break
        res += y[1] - 1
        count += 1
    return res
