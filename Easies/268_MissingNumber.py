#
#   Date - 01.02.2022
#
#
# 268. Missing Number
# Easy
#
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
#
#
#
# Example 1:
#
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
#
# Example 2:
#
# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
#
# Example 3:
#
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
#
#
#
# Constraints:
#
#     n == nums.length
#     1 <= n <= 104
#     0 <= nums[i] <= n
#     All the numbers of nums are unique.
#


from math import prod
import timeit
from typing import List, Optional, Set, Dict
# from collections import defaultdict
import collections


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (len(nums) + 1) * len(nums) // 2 - sum(nums)


def testing():
    sol = Solution()

    result = sol.missingNumber(nums=[3, 0, 1])
    # print(f"result: {result}")
    assert (2 == result)

    result = sol.missingNumber(nums=[0, 1])
    # print(f"result: {result}")
    assert (2 == result)

    result = sol.missingNumber(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1])
    # print(f"result: {result}")
    assert (8 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
