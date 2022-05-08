#
#   Date - 07.05.2022
#
#
# Given an integer number n, return
#   the difference between the
#   product of its digits and the
#   sum of its digits.
#
#
#
# Example 1:
#
# Input: n = 234
# Output: 15
# Explanation:
# Product of digits = 2 * 3 * 4 = 24
# Sum of digits = 2 + 3 + 4 = 9
# Result = 24 - 9 = 15
#
# Example 2:
#
# Input: n = 4421
# Output: 21
# Explanation:
# Product of digits = 4 * 4 * 2 * 1 = 32
# Sum of digits = 4 + 4 + 2 + 1 = 11
# Result = 32 - 11 = 21
#
#
#
# Constraints:
#
#     1 <= n <= 10^5
#


import timeit
from math import prod
from typing import List, Optional, Set


def subtractProductAndSum(n: int) -> int:
    """
    The best way to get ahead is to get starting..?
    """
    # # algebraic
    s, p = 0, 1
    while n:
        n, digit = divmod(n, 10)
        p *= digit
        s += digit
    return p-s

    # # pythonic
    # digits = list(map(int, str(n)))
    # return prod(digits)-sum(digits)


def testing():
    result = subtractProductAndSum(n=234)
    # print(f"result: {result}")
    assert (15 == result)

    result = subtractProductAndSum(n=4421)
    # print(f"result: {result}")
    assert (21 == result)



if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
