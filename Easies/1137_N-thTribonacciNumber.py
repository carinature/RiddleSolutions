#
#   Date - 11.06.22
#
#
# 1137. N-th Tribonacci Number
# Easy
#
# The Tribonacci sequence Tn is defined as follows:
#
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
#
# Given n, return the value of Tn.
#
#
#
# Example 1:
#
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
#
# Example 2:
#
# Input: n = 25
# Output: 1389537
#
#
#
# Constraints:
#
#     0 <= n <= 37
#     The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
#


from math import prod
import timeit
from typing import List, Optional, Set, Dict
# from collections import defaultdict
import collections


class Solution:
    def tribonacci(self, n: Optional[int] = int) -> Optional[int]:
        """
        The best way to get ahead is to get starting..?
        """

        # # # # Solution 1 - DP - O(n)
        # if not n:
        #     return 0
        # if n < 3:
        #     return 1
        # tbl = [0] * (n + 1)
        # tbl[1] = tbl[2] = 1
        #
        # for i in range(3, n + 1):
        #     tbl[i] = tbl[i - 1] + tbl[i - 2] + tbl[i - 3]
        #
        # return tbl[n]

        # # # # Solution 2 - slightly better
        if not n:
            return 0
        if n < 3:
            return 1
        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c


def testing():
    sol = Solution()

    result = sol.tribonacci(n=4)
    # print(f"result: {result}")
    assert (4 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=10000)))
