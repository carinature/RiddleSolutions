#
#   Date - 26.05.2022
#
#
# 2279. Maximum Bags With Full Capacity of Rocks
# Medium
#
# You have n bags numbered from 0 to n - 1.
# You are given two 0-indexed integer arrays capacity and rocks.
# The ith bag can hold a maximum of capacity[i] rocks and currently contains rocks[i] rocks.
# You are also given an integer additionalRocks, the number of additional rocks you can place in any of the bags.
#
# Return the maximum number of bags that could have full capacity after placing the additional rocks in some bags.
#
#
#
# Example 1:
#
# Input: capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2
# Output: 3
# Explanation:
# Place 1 rock in bag 0 and 1 rock in bag 1.
# The number of rocks in each bag are now [2,3,4,4].
# Bags 0, 1, and 2 have full capacity.
# There are 3 bags at full capacity, so we return 3.
# It can be shown that it is not possible to have more than 3 bags at full capacity.
# Note that there may be other ways of placing the rocks that result in an answer of 3.
#
# Example 2:
#
# Input: capacity = [10,2,2], rocks = [2,2,0], additionalRocks = 100
# Output: 3
# Explanation:
# Place 8 rocks in bag 0 and 2 rocks in bag 2.
# The number of rocks in each bag are now [10,2,2].
# Bags 0, 1, and 2 have full capacity.
# There are 3 bags at full capacity, so we return 3.
# It can be shown that it is not possible to have more than 3 bags at full capacity.
# Note that we did not use all of the additional rocks.
#
#
#
# Constraints:
#
#     n == capacity.length == rocks.length
#     1 <= n <= 5 * 104
#     1 <= capacity[i] <= 109
#     0 <= rocks[i] <= capacity[i]
#     1 <= additionalRocks <= 109
#


from math import prod
import timeit
from typing import List, Optional, Set, Dict
# from collections import defaultdict
import collections


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        dif = sorted([c - r for c, r in zip(capacity, rocks)])
        # print(f'dif {dif}')
        i = 0
        while i < len(dif) and additionalRocks > 0:
            additionalRocks -= dif[i]
            dif[i] = 0
            i += 1
            # print(f'additionalRocks {additionalRocks}')
            # print(f'dif {dif}')
            # print(f'i {i}')
        return dif.count(0)-int(additionalRocks<0)


def testing():
    sol = Solution()

    result = sol.maximumBags(capacity=[2, 3, 4, 5], rocks=[1, 2, 4, 4], additionalRocks=2)
    # print(f"result: {result}")
    assert (3 == result)

    result = sol.maximumBags(capacity=[10, 2, 2], rocks=[2, 2, 0], additionalRocks=100)
    # print(f"result: {result}")
    assert (3 == result)

    result = sol.maximumBags(
        capacity=[91, 54, 63, 99, 24, 45, 78], rocks=[35, 32, 45, 98, 6, 1, 25], additionalRocks=17)
    # print(f"result: {result}")
    assert (1 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
