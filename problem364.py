was = {}


def t(a):
    if len(a) == 0:
        return 1
    if tuple(a) in was:
        return was[tuple(a)]
    total = 0
    if a[0][0] == 1:
        if a[0] > (1, False, False):
            total += t(a[1:])
            if len(a) > 1 and a[1] > (1, False, False):
                total += t(a[:1] + a[2:])
        else:
            total += len(a) * t(a[1:])
        was[tuple(a)] = total
        return total
    elif a[0][0] == 2:
        if a[0] > (2, False, False):
            total += t(a[1:])
            if a[1] > (2, False, False):
                total += t(a[:1] + a[2:])
        else:
            for i in range(len(a)):
                if a[i] > (1, False, False):
                    total += 2 * t(a[:i] + a[i + 1:])
        #else:
        #    for i in range(len(a)):
        #        if a[i][0] == 2:
        #            total += t(a[:i] + a[i + 1:])
        was[tuple(a)] = total
        return total
    else:
        for i in range(len(a)):
            if a[i][0] == 1:
                break
            else:
                if a[i][1]:
                    total += t(sorted(a[:i] + a[i + 1:] + [(a[i][0] - 1, False, a[i][2])], reverse=True))
                if a[i][2]:
                    total += t(sorted(a[:i] + a[i + 1:] + [(a[i][0] - 1, a[i][1], False)], reverse=True))
                for j in range(1, a[i][0] - 1):
                    total += t(sorted(a[:i] + a[i + 1:] + [(j, a[i][1], False), (a[i][0] - j - 1, False, a[i][2])], reverse=True))
        was[tuple(a)] = total
        return total
