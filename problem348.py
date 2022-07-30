was = {}


def palindrome(n):
    return str(n) == str(n)[::-1]


def occurences(n):
    was.clear()
    for i in range(2, int(n ** 0.5)):
        for j in range(2, int((n - i ** 2) ** (1 / 3))):
            m = i ** 2 + j ** 3
            if palindrome(m):
                if m in was:
                    was[m] += 1
                else:
                    was[m] = 1
    return [p for p in was if was[p] == 4]
