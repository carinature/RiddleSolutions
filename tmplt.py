#
#   Date - 01.02.2022
#
#
# Given an integer array nums, move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
#
#
#       Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
#       Example 2:
# Input: nums = [0]
# Output: [0]
#
#
#       Constraints:
#     1 <= nums.length <= 104
#     -231 <= nums[i] <= 231 - 1


from math import prod
import timeit
from typing import List, Optional, Set


def some_function(nums: Optional[int]) -> Optional[int]:
    """
    The best way to get ahead is to get starting..?
    """
    return 124356


def testing():
    result = some_function(nums=124356)
    print(f"result: {result}")
    assert (124356 == result)

    result = some_function(nums=124356)
    print(f"result: {result}")
    assert (124356 == result)

    result = some_function(nums=124356)
    print(f"result: {result}")
    assert (124356 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
