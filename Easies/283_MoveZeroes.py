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

from typing import List, Optional
import time
import timeit


def some_function(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    # #    -------- Solution 1 (mine)
    # # find 1st zero zero
    zero = 0
    while zero < len(nums) and nums[zero]:
        zero += 1
    i = zero + 1
    while i < len(nums):
        if nums[i]:
            nums[zero], nums[i] = nums[i], 0
            zero += 1
        i += 1

    # zero = 0
    # try:
    #     while nums[zero]:
    #         zero += 1
    # except:
    #     return
    # # while zero < len(nums) and nums[zero]:
    # #     zero += 1
    # for i in range(zero + 1, len(nums)):
    #     if nums[i]:
    #         nums[zero], nums[i] = nums[i], 0
    #         zero += 1
    #

    # # fixme The above solution's run time was 280-344ms on leetCode while the two below took 4185-5197ms. WHY????
    #
    # #    -------- Solution 2 (mine)
    # for zero in range(len(nums)):
    #     if not nums[zero]:
    #         i = zero + 1
    #         while i < len(nums):
    #             if nums[i]:
    #                 nums[zero], nums[i] = nums[i], 0
    #                 zero += 1
    #             i += 1

    # # # -------- Solution 3 (mine)
    # zero = 0
    # while zero < len(nums):
    #     if not nums[zero]:
    #         i = zero + 1
    #         while i < len(nums):
    #             if nums[i]:
    #                 nums[zero], nums[i] = nums[i], 0
    #                 zero += 1
    #             i += 1
    #     zero += 1
    #

def testing():
    nums = [0, 1, 0, 3, 12]
    some_function(nums)
    # print(f"nums: {nums}")
    assert ([1, 3, 12, 0, 0] == nums)

    nums = [0]
    some_function(nums)
    # print(f"nums: {nums}")
    assert ([0] == nums)

    nums = [0, -1]
    some_function(nums)
    # print(f"nums: {nums}")
    assert ([-1, 0] == nums)

    nums = [0, 0]
    some_function(nums)
    # print(f"nums: {nums}")
    assert ([0, 0] == nums)

    nums = [1, 1]
    some_function(nums)
    # print(f"nums: {nums}")
    assert ([1, 1] == nums)

    nums = [1, 0]
    some_function(nums)
    # print(f"nums: {nums}")
    assert ([1, 0] == nums)


if __name__ == '__main__':
    print("--- %.5f seconds ---" % (timeit.timeit(testing, number=100)))
