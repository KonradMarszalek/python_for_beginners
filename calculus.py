data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Expected result
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [2, 4, 6, 8, 10, 12, 14, 16, 18]
# [3, 6, 9, 12, 15, 18, 21, 24, 27]
# [4, 8, 12, 16, 20, 24, 28, 32, 36]
# [5, 10, 15, 20, 25, 30, 35, 40, 45]
# [6, 12, 18, 24, 30, 36, 42, 48, 54]
# [7, 14, 21, 28, 35, 42, 49, 56, 63]
# [8, 16, 24, 32, 40, 48, 56, 64, 72]
# [9, 18, 27, 36, 45, 54, 63, 72, 81]

from pprint import pprint


def calculus(data):
    for multiplicand in data:
        result_line = []
        for multiplier in data:
            result_line.append(multiplicand*multiplier)
        pprint(result_line)




def calculus_ewa(data):
    for el in range(1):
        for el2 in range(1, 10):
            print([el2 * 1, el2 * 2, el2 * 3, el2 * 4, el2 * 5, el2 * 6, el2 * 7, el2 * 8, el2 * 9])


def calculus_darek():
    n = 11
    m = list(list(range(1 * i, (n + 1) * i, i)) for i in range(1, n + 1))
    pprint(m)




# calculus(data)
#calculus_ewa(data)
calculus_darek()


