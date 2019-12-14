"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import math


class P10(object):

    @staticmethod
    def run():
        sum_primes = 2
        for i in range(3, 2000000, 2):
            if P10.is_prime(i):
                sum_primes += i
        print(sum_primes)

    @staticmethod
    def is_prime(n):
        if n == 1:
            return False
        if n < 4:
            return True  # 2 and 3 are prime
        if n % 2 == 0:
            return False
        if n < 9:
            return True  # we have already excluded 4,6 and 8.
        if n % 3 == 0:
            return False

        # any number n can have only one prime factor > sqrt(n).
        # Thus, we can limit the check to sqrt(n): if we cannot find a number <= sqrt(n) that divides n,
        # n must be a prime, because the only prime factor of n is n itself.
        limit = math.floor(math.sqrt(n))
        # the following code based on the fact that all primes > 3 are of the form 6k+/-1
        f = 5
        while f <= limit:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f = f + 6
        return True


if __name__ == '__main__':
    P10.run()
