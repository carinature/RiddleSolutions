#
#   Date - 11.06.22
#
#
# 509. Fibonacci Number
# Easy
#
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
#
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
#
# Given n, calculate F(n).
#
#
#
# Example 1:
#
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
#
# Example 2:
#
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
#
# Example 3:
#
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
#
#
#
# Constraints:
#
#     0 <= n <= 30
#


from math import prod
import timeit
from typing import List, Optional, Set, Dict
# from collections import defaultdict
import collections


class Solution:
    def fib(self, n: int) -> Optional[int]:
        """
        The best way to get ahead is to get starting..?
        """
        # print(f'nums: {n}')
        if n < 2:
            return n
        tbl = [0]*(n+1)
        tbl[1] = 1
        for i in range(2, n+1):
            tbl[i] = tbl[i-1]+tbl[i-2]
        return tbl[n]



def testing():
    sol = Solution()

    result = sol.fib(n=2)
    # print(f"result: {result}")
    assert (1 == result)

    result = sol.fib(n=3)
    # print(f"result: {result}")
    assert (2 == result)

    result = sol.fib(n=4)
    # print(f"result: {result}")
    assert (3 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
