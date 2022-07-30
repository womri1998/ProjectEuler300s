def set(n):
    hotel = []
    for i in range(1, n):
        j = 0
        done = False
        while not done:
            if len(hotel) == j:
                hotel.append([i])
                done = True
            elif (hotel[j][-1] + i) ** 0.5 % 1 == 0:
                hotel[j].append(i)
                done = True
            else:
                j += 1
    return hotel


def print_hotel(hotel):
    for i in range(len(hotel)):
        print("floor " + str(i + 1) + ": " + str(hotel[i]))


def divisors(n):
    res = {}
    i = 2
    while n != 1:
        if n % i == 0:
            res[i] = 0
        while n % i == 0:
            res[i] += 1
            n //= i
        i += 1
    return res
