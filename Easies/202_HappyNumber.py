#
#   Date - 08.05.2022
#
#
# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
#     Starting with any positive integer, replace the number by the sum of the squares of its digits.
#     Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#     Those numbers for which this process ends in 1 are happy.
#
# Return true if n is a happy number, and false if not.
#
#
#
# Example 1:
#
# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
#
# Example 2:
#
# Input: n = 2
# Output: false
#
#
#
# Constraints:
#
#     1 <= n <= 231 - 1
#


import timeit
from math import prod
from typing import List, Optional, Set


def isHappy(n: int) -> bool:
    # solution 1
    nset: set = {n}
    while 1 != n:
        n = sum([int(d) ** 2 for d in str(n)])
        # n = sum(map(lambda d: int(d) ** 2, str(n)))
        if n in nset:
            return False
        nset.add(n)
    return True


def testing():
    result = isHappy(n=19)
    # print(f"result: {result}")
    assert (True == result)

    result = isHappy(n=2)
    # print(f"result: {result}")
    assert (False == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
