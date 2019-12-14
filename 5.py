"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


class P5(object):

    @staticmethod
    def run():
        res = 1
        for i in range(1,21):
            res = P5.lcm(res,i)
        print(res)

    @staticmethod
    def gcd(a, b):
        if b == 0:
            return a
        return P5.gcd(b, a % b)

    @staticmethod
    def lcm(a, b):
        return (a * b) / P5.gcd(a, b)


if __name__ == '__main__':
    P5.run()
