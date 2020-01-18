"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
import math
import time


class P16(object):

    @staticmethod
    def run():
        print(sum([int(c) for c in str(2**1000)]))


if __name__ == '__main__':
    start_time = time.time()
    P16.run()
    print("--- %s seconds ---" % (time.time() - start_time))
