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
    def climbStairs(self, n: int) -> int:
        # # # # # Solution 1  - recursive with memoization
        # def withMemo(n, memo={0: 0, 1: 1, 2: 2}):
        #     # if memo is None:
        #     #     memo = dict()
        #
        #     if n in memo:
        #         return memo[n]
        #
        #     # if n < 4:
        #     #     memo[n] = n
        #     #     return n
        #
        #     memo[n] = withMemo(n - 2) + withMemo(n - 1)
        #     return memo[n]
        #
        # return withMemo(n)

        # # # # Solution 2 - iterative with tabulation
        # tbl = [0] * (n + 1)
        # tbl[1] = 1
        # tbl[2] = 2
        #
        # for i in range(3, n + 1):
        #     tbl[i] = tbl[i - 1] + tbl[i - 2]
        #
        # return tbl[n]

        # # # Solution 3 - iterative WITHOUT tabulation - fastest
        if n < 4:
            return n
        s1, s2 = 1, 2
        for _ in range(3, n + 1):
            s1, s2 = s2, s1 + s2
        return s2


def testing():
    sol = Solution()

    result = sol.climbStairs(n=2)
    # print(f"result: {result}")
    assert (2 == result)

    result = sol.climbStairs(n=3)
    # print(f"result: {result}")
    assert (3 == result)

    result = sol.climbStairs(n=4)
    # print(f"result: {result}")
    assert (5 == result)

    result = sol.climbStairs(n=5)
    # print(f"result: {result}")
    assert (8 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=10000)))
