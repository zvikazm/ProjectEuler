"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import math
import time


class P14(object):

    @staticmethod
    def next_num(n):
        if n % 2 == 0:
            return int(n / 2)
        else:
            return 3 * n + 1

    @staticmethod
    def run():
        d = {}
        max_counter = 0
        num_res = 0
        for i in range(1, 1000000):
            n = i
            counter = 1
            # print(n, end=",")
            while n != 1:
                if 1:
                    if n in d:
                        counter += d[n] - 1
                        break
                n = P14.next_num(n)
                # print(n, end=",")
                counter += 1
            d[i] = counter
            # print("")
            if counter > max_counter:
                max_counter = counter
                num_res = i
        print(num_res, max_counter)


if __name__ == '__main__':
    start_time = time.time()
    P14.run()
    print("--- %s seconds ---" % (time.time() - start_time))
