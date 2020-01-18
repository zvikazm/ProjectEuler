"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
import math
import time


class P15(object):

    @staticmethod
    def run():
        n = 40
        k = 20
        res = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
        print(res)


if __name__ == '__main__':
    start_time = time.time()
    P15.run()
    print("--- %s seconds ---" % (time.time() - start_time))
