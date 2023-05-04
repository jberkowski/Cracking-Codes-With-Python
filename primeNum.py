'''Prime Number Sieve - functions to check if number is prime and to
find a (large) prime numbers.
https://www.nostarch.com/crackingcodes/ (BSD Licensed).'''

import math, random


def isPrimeTrialDiv(num):
    '''Check if number is prime by dividing it by integers up to and
    including its square root. Returns True if num is prime.'''

    # If num is less than 2, it is not prime:
    if num < 2:
        return False

    # See if num is divisible by any number up to its square root:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def primeSieve(sieveSize):
    '''Returns a list of prime numbers up to sieveSize. Uses the Sieve of
    Eratosthenes algorithm.'''
    sieve = [True] * sieveSize
    sieve[0] = False  # 0 is not a prime number.
    sieve[1] = False  # 1 is not a prime number.

    for i in range(2, int(math.sqrt(sieveSize)) + 1):
        pointer = i * 2
        while pointer < sieveSize:
            sieve[pointer] = False
            pointer += i

    # Compile the list of primes:
    primes = []
    for i in range(sieveSize):
        if sieve[i] == True:
            primes.append(i)

    return primes


def rabinMiller(num):
    '''Returns True if num is a prime number (with high probability...).'''
    if num % 2 == 0 or num < 2:
        return False  # Rabin-Miller doesn't work on even integers.
    if num == 3:
        return True
    s = num - 1
    t = 0
    while s % 2 == 0:
        # Keep halving s until it is odd (use t to count
        # how many times we halve s):
        s = s // 2
        t += 1
    for trials in range(5):  # Try to falsify num's primality 5 times.
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:  # This test does not apply if v is 1.
            i = 0
            while v != (num -1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True


# Most of the time we can quickly determine if num is not prime
# by dividing by the first few dozen prime numbers. This is quicker
# than rabinMiller() but does not detect all composites.
LOW_PRIMES = primeSieve(100)


def isPrime(num):
    '''Return True if num is a prime number. This function does a quicker
    prime number check before calling rabinMiller().'''
    if num < 2:
        return False  # All numbers lower than 2 are not prime.
    for prime in LOW_PRIMES:
        if num == prime:
            return True
        if num % prime == 0:
            return False

    # If all else fails, call rabinMiller():
    return rabinMiller(num)


def generateLargePrime(keysize = 1024):
    # Return a random prime number that is keysize bits in size:
    while True:
        num = random.randrange(2 ** (keysize - 1), 2 ** keysize)
        if isPrime(num):
            return num