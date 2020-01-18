"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""
import math
import time


class P17(object):
    nums_20 = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty"
    }
    tens_dict = {
        1: "ten",
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"
    }

    @staticmethod
    def num_to_string(num):
        if num <= 20:
            return P17.nums_20[num]
        elif num < 100:
            res = P17.tens_dict[num // 10]
            units = num % 10
            if units == 0:
                return res
            else:
                return res + P17.nums_20[units]
        elif num < 1000:
            res = ""
            hundreds = str(P17.nums_20[num // 100]) + "hundred"
            tens = num % 100
            if tens == 0:
                return hundreds
            else:
                return hundreds + "and" + P17.num_to_string(tens)
        elif num == 1000:
            return "onethousand"

    @staticmethod
    def run():
        res = 0

        for i in range(1, 1001):
            res += len(P17.num_to_string(i))
        print(res)


if __name__ == '__main__':
    start_time = time.time()
    P17.run()
    print("--- %s seconds ---" % (time.time() - start_time))
