class P2(object):

    @staticmethod
    def run():
        a = 1
        b = 2
        even_sum = b
        while True:
            tmp = b
            b = a + b
            a = tmp
            if b > 4e6:
                break
            if b % 2 == 0:
                even_sum += b
        print(even_sum)


if __name__ == '__main__':
    P2.run()
