"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


class P9(object):

    @staticmethod
    def run():
        for i in range(1, 1000):
            for j in range(i + 1, 1000):
                for k in range(j + 1, 1000):
                    if i ** 2 + j ** 2 == k ** 2 and i + j + k == 1000:
                        print(i, j, k)
        pass


if __name__ == '__main__':
    P9.run()
