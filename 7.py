"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import math


class P7(object):

    @staticmethod
    def run():
        primes = []
        i = 2
        while len(primes) < 10001:
            if P7.is_prime(i):
                primes.append(i)
            i += 1
        print(primes[-1])

    @staticmethod
    def is_prime(n):
        for i in range(2, round(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


if __name__ == '__main__':
    P7.run()
