#
#   Date - 18.05.2022
#
#
# 217. Contains Duplicate
# Easy
#
# Given an integer array nums,
# return true if any value appears at least twice in the array,
# and return false if every element is distinct.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: true
#
# Example 2:
#
# Input: nums = [1,2,3,4]
# Output: false
#
# Example 3:
#
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
#
#
#
# Constraints:
#
#     1 <= nums.length <= 105
#     -109 <= nums[i] <= 109


from math import prod
import timeit
from typing import List, Optional, Set, Dict
from collections import defaultdict


def containsDuplicate(nums: List[int]) -> bool:
    """
    The best way to get ahead is to get starting..?
    """
    return len(nums) != len(set(nums))


def testing():
    result = containsDuplicate(nums=[1, 2, 3, 1])
    # print(f"result: {result}")
    assert (True == result)

    result = containsDuplicate(nums=[1, 2, 3, 4])
    # print(f"result: {result}")
    assert (False == result)

    result = containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
    # print(f"result: {result}")
    assert (True == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
