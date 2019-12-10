"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math


class P3(object):

    @staticmethod
    def run():
        number = 600851475143
        number_sqrt = round(math.sqrt(number) + 1)
        for i in range(number_sqrt, 0, -1):
            if number % i == 0:
                if P3.is_prime(i):
                    print(i)  # answer is 6857
                    return

    @staticmethod
    def is_prime(n):
        for i in range(2, round(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


if __name__ == '__main__':
    P3.run()
