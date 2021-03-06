import math
import functools


def even_numbers(upper_bound: int) -> list:
    """
    generates all even numbers less than the upper bound inclusive
    :param upper_bound: upper bound of the list, exclusive
    :return: list of positive even numbers less than the upper bound
    """
    # ret = []
    # for i in range(1, upper_bound):
    #     if i % 2 == 0:
    #         ret.append(i)
    # return ret
    return [i for i in range(0, upper_bound + 1) if i % 2 == 0]


def odd_numbers(upper_bound: int) -> list:
    """
    generates all odd numbers less than the upper bound inclusive
    :param upper_bound: upper bound of the list, exclusive
    :return: list of odd numbers less than the upper bound
    """
    return [i for i in range(1, upper_bound + 1) if i % 2 != 0]


def smaller_prime_numbers(upper_bound: int) -> list:
    """
    generates all prime numbers less than the upper bound exclusive
    """
    if upper_bound <= 2:
        return []

    numbers = [2]
    for i in range(3, upper_bound, 2):
        if is_prime(i):
            numbers.append(i)
    return numbers


def is_prime(num: int) -> bool:
    if num < 2:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    sqrt = int(math.sqrt(num)) + 1
    for i in range(3, sqrt, 2):
        # non prime rule: can be divided and divisor less than the target
        if num % i == 0:
            return False

    return True


def sieve_of_eratosthenes(upper_bound: int) -> list:
    numbers = [0] * (upper_bound + 1)

    for k in range(2, int(math.sqrt(upper_bound)) + 1):
        if numbers[k] == 1:
            continue

        index = [k * i for i in range(2, upper_bound // k + 1)]
        for i in index:
            numbers[i] = 1

    primes = [i for i, val in enumerate(numbers) if val == 0]
    primes = primes[2:]
    return primes


def sieve_of_eratosthenes1(upper_bound: int) -> list:
    numbers = [0] * (upper_bound + 1)

    for k in range(2, int(math.sqrt(upper_bound)) + 1):
        if numbers[k] == 1:
            continue

        numbers[2 * k::k] = [1] * (upper_bound // k - 1)

    primes = [i for i, val in enumerate(numbers) if val == 0]
    primes = primes[2:]
    return primes


def prime_factors(a: int) -> dict:
    prime_counts = {}
    while a > 1 and a % 2 == 0:
        x = prime_counts.get(2, 0)
        prime_counts[2] = x + 1

        a = a // 2

    for i in range(3, math.ceil(math.sqrt(a)) + 1, 2):
        if a == 1:
            break

        while a > 1 and a % i == 0:
            x = prime_counts.get(i, 0)
            prime_counts[i] = x + 1

            a = a // i

    if is_prime(a):
        x = prime_counts.get(a, 0)
        prime_counts[a] = x + 1

    return prime_counts


def gcd(a: int, b: int) -> int:
    """
    greatest common divisor, based on tail recursion
    """
    x = abs(a)
    y = abs(b)

    x, y = max(x, y), min(x, y)

    if y == 0:
        # https://en.wikipedia.org/wiki/Greatest_common_divisor
        return x

    remainder = x % y
    if remainder == 0:
        return y

    return gcd(y, remainder)


def gcd1(a: int, b: int) -> int:
    """
    greatest common divisor, based on loop
    """
    x = abs(a)
    y = abs(b)

    x, y = max(x, y), min(x, y)

    while y > 0:
        x, y = y, x % y

    return x


def gcdm(a: list) -> int:
    x = gcd1(a[0], a[1])
    for i in a[2:]:
        x = gcd1(x, i)

    return x


def gcdm1(a: list) -> int:
    return functools.reduce(gcd1, a)


def lcm(a: int, b: int):
    """
    least common multiple
    """
    if a == 0 and b == 0:
        return 0

    return abs(a * b) / gcd(a, b)


def euclidean_tuple(a, b):
    """
    This is the extended Euclidean algorithm. Instead of returning only the
    GCD, it returns a tuple, (x, y, d) such that
        a * x + b * y = d
    The necessary and sufficient conditions for d = gcd(a, b) are:
        a and b can be divided by d
        ax + by = d for some x and y
    This is because if a factor f divides both a and b then from 2 f has to
    divide d. So d is gcd.

    https://thilinaatsympy.wordpress.com/2013/06/21/solving-linear-diophantine-equation/
    """
    if b == 0:
        return 1, 0, a
    else:
        # Here we have a = kb + r, where r = a % b.
        # The returned x and y satisfies bx + ry = d. This is true for all
        # recursions. Replace r with a - kb:
        #     bx + (a - kb)y = d
        #     ay + b(x -ky) = d
        # So the new x is y and the new y is x - ky, where k = a / b (integer quotient)
        x, y, gcdv = euclidean_tuple(b, a % b)

        new_x = y
        new_y = x - (a // b) * y
        return new_x, new_y, gcdv
