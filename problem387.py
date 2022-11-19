from queue import Queue


def generate_primes(n: int) -> list[int]:
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False
    for i in range(n + 1):
        if primes[i]:
            for j in range(2 * i, n + 1, i):
                primes[j] = False
    return [i for i, is_prime in enumerate(primes) if is_prime]


def is_prime(n: int, primes: list[int]) -> bool:
    """
    :param n: number to check
    :param primes: list of primes, assuming max(primes) >= sqrt(n) && primes is sorted
    :return: boolean answer of n's primality
    """
    if n < 2:
        return False
    if n == 2:
        return True
    for prime in primes:
        if n % prime == 0:
            return False
        if prime ** 2 >= n:
            return True


def get_digits_sum(n: int) -> int:
    m = n
    digits_sum = 0
    while m != 0:
        digits_sum += m % 10
        m //= 10
    return digits_sum


def is_harshad(n: int) -> bool:
    return n % get_digits_sum(n) == 0


def generate_right_harshads(n: int) -> set[int]:
    right_harshads = {i for i in range(1, 10)}
    queue = Queue()
    for i in range(1, 10):
        queue.put_nowait(i)
    while not queue.empty():
        right_harshad = queue.get_nowait()
        if right_harshad * 10 < n:
            for i in range(10):
                suspect = right_harshad * 10 + i
                if is_harshad(suspect):
                    right_harshads.add(suspect)
                    queue.put_nowait(suspect)
    return right_harshads


def generate_strong_right_harshads(right_harshads: set[int], primes: list[int]) -> set[int]:
    return {right_harshad for right_harshad in right_harshads if
            is_prime(right_harshad // get_digits_sum(right_harshad), primes)}


def generate_prime_strong_right_harshads(strong_right_harshads: set[int], primes: list[int]) -> set[int]:
    prime_strong_right_harshads = set()
    for strong_right_harshad in strong_right_harshads:
        for i in range(10):
            suspect = strong_right_harshad * 10 + i
            if is_prime(suspect, primes):
                prime_strong_right_harshads.add(suspect)
    return prime_strong_right_harshads


def main():
    primes = generate_primes(int(1e7))
    right_harshads = generate_right_harshads(int(1e13))
    strong_right_harshads = generate_strong_right_harshads(right_harshads, primes)
    prime_strong_right_harshads = generate_prime_strong_right_harshads(strong_right_harshads, primes)
    print(sum(prime_strong_right_harshads))


if __name__ == "__main__":
    main()
