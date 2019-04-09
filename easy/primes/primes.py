"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""


def primes(count):
    """Return count number of prime numbers, starting at 2."""

    prime_num = []

    for i in range(2, 100):
        if is_prime(i) and len(prime_num) < count:
            prime_num.append(i)
    
    return prime_num


def is_prime(num):

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GREAT WORK!\n")
