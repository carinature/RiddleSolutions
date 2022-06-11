#
#   Date - 11.06.22
#
#
# 746. Min Cost Climbing Stairs
# Easy
#
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
# Once you pay the cost, you can either climb one or two steps.
#
# You can either start from the step with index 0, or the step with index 1.
#
# Return the minimum cost to reach the top of the floor.
#
#
#
# Example 1:
#
# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
#
# Example 2:
#
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.
#
#
#
# Constraints:
#
#     2 <= cost.length <= 1000
#     0 <= cost[i] <= 999
#


from math import prod
import timeit
from typing import List, Optional, Set, Dict
# from collections import defaultdict
import collections


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # # # # # # Solution 1  - iterative w/ tabulation
        # total = [0] * (len(cost) + 1)
        # for i in range(2, len(total)):
        #     total[i] = min(cost[i - 1] + total[i - 1], cost[i - 2] + total[i - 2])
        #
        # return total[-1]

        # # # # # Solution 2  - iterative w/out tabulation
        total1 = total2 = 0
        for i in range(2, len(cost) + 1):
            total2, total1 = total1, min(cost[i - 2] + total2, cost[i - 1] + total1)

        return total1


def testing():
    sol = Solution()

    result = sol.minCostClimbingStairs(cost=[10, 15, 20])
    # print(f"result: {result}")
    assert (15 == result)

    result = sol.minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
    # print(f"result: {result}")
    assert (6 == result)

    # result = sol.minCostClimbingStairs(cost=4)
    # # print(f"result: {result}")
    # assert (5 == result)
    #
    # result = sol.minCostClimbingStairs(cost=5)
    # # print(f"result: {result}")
    # assert (8 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=10000)))
