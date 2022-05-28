#
#   Date - 28.05.2022
#
#
# 34. Find First and Last Position of Element in Sorted Array
# Medium
#
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
#
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#
# Example 3:
#
# Input: nums = [], target = 0
# Output: [-1,-1]
#
#
#
# Constraints:
#
#     0 <= nums.length <= 105
#     -109 <= nums[i] <= 109
#     nums is a non-decreasing array.
#     -109 <= target <= 109
#


from math import prod
import timeit
from typing import List, Optional, Set, Dict
# from collections import defaultdict
import collections


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        The best way to get ahead is to get starting..?
        """

        def directed_bin_search(nums: List[int], target: int,
                                direction: int = -1, start_i: int = 0) -> int:
            left, right = start_i, len(nums) - 1
            while left <= right:
                mid = (right - left) // 2 + left
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    if mid == (len(nums) - 1) * (direction > 0) or nums[mid + direction] != target:
                        return mid
                    else:
                        if direction == -1:
                            right = mid - 1
                        else:
                            left = mid + 1
            return -1

        res_left = directed_bin_search(nums, target)
        if res_left == -1: return [-1, -1]
        res_right = directed_bin_search(nums, target, 1, res_left)
        return [res_left, res_right]


def testing():
    sol = Solution()

    result = sol.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8)
    # print(f"result: {result}")
    assert ([3, 4] == result)

    result = sol.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6)
    # print(f"result: {result}")
    assert ([-1, -1] == result)

    result = sol.searchRange(nums=[], target=0)
    # print(f"result: {result}")
    assert ([-1, -1] == result)

    result = sol.searchRange(nums=[5, 7, 7, 8, 10], target=8)
    # print(f"result: {result}")
    assert ([3, 3] == result)

    result = sol.searchRange(nums=[2, 2], target=2)
    # print(f"result: {result}")
    assert ([0, 1] == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
