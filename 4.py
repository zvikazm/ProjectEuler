"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


class P4(object):

    @staticmethod
    def run():
        max_n = 0
        for i in range(999, 100, -1):
            for j in range(999, 100, -1):
                m = i * j
                if P4.is_palindrome(str(m)):
                    if m > max_n:
                        max_n = m
        print(max_n)

    @staticmethod
    def is_palindrome(s):
        if s == s[::-1]:
            return True
        return False


if __name__ == '__main__':
    P4.run()
