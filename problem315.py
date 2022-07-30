import math
from typing import Iterable, Generator


DIGITAL_REPRESENTATION = {
    ' ': (0, 0, 0, 0, 0, 0, 0),
    '0': (1, 0, 1, 1, 1, 1, 1),
    '1': (0, 0, 0, 0, 1, 0, 1),
    '2': (1, 1, 1, 0, 1, 1, 0),
    '3': (1, 1, 1, 0, 1, 0, 1),
    '4': (0, 1, 0, 1, 1, 0, 1),
    '5': (1, 1, 1, 1, 0, 0, 1),
    '6': (1, 1, 1, 1, 0, 1, 1),
    '7': (1, 0, 0, 1, 1, 0, 1),
    '8': (1, 1, 1, 1, 1, 1, 1),
    '9': (1, 1, 1, 1, 1, 0, 1)
}


def gen_primes(n) -> Generator[int, None, None]:
    primes = [True] * n
    primes[0], primes[1] = False, False
    for i in range(math.ceil(n ** 0.5)):
        if primes[i]:
            for j in range(2 * i, n, i):
                primes[j] = False
    return (i for i in range(n) if primes[i])


def digits_diff(first_digit: str, second_digit: str) -> int:
    return sum((first_light ^ second_light for first_light, second_light in
                zip(DIGITAL_REPRESENTATION[first_digit], DIGITAL_REPRESENTATION[second_digit])))


def number_string(number: int, length: int) -> str:
    if number == 0:
        return "".rjust(length)
    else:
        return str(number).rjust(length)


def numbers_diff(first_number: int, second_number: int) -> int:
    length = max((len(str(first_number)), len(str(second_number))))
    first_str = number_string(first_number, length)
    second_str = number_string(second_number, length)
    return sum((digits_diff(first_digit, second_digit) for first_digit, second_digit in zip(first_str, second_str)))


def next_number(number: int) -> int:
    return sum((int(digit) for digit in str(number)))


def sam_transitions(number: int) -> int:
    total_transitions = numbers_diff(0, number)
    while number >= 10:
        number = next_number(number)
        total_transitions += numbers_diff(0, number)
    return total_transitions * 2


def max_transitions(number: int) -> int:
    total_transitions = numbers_diff(0, number)
    while number >= 10:
        previous_number = number
        number = next_number(number)
        total_transitions += numbers_diff(previous_number, number)
    total_transitions += numbers_diff(number, 0)
    return total_transitions


def clocks_diff(numbers: Iterable) -> int:
    return sum((sam_transitions(number) - max_transitions(number) for number in numbers))


if __name__ == "__main__":
    input_primes = (prime for prime in gen_primes(2 * 10 ** 7) if prime > 10 ** 7)
    print("done with primes")
    print(clocks_diff(input_primes))
