#
#   Date - 07.05.2022
#
#
# Given an integer array nums,
# return the largest perimeter of a triangle with a non-zero area,
# formed from three of these lengths.
# If it is impossible to form any triangle of a non-zero area, return 0.
#
#
#
# Example 1:
#
# Input: nums = [2,1,2]
# Output: 5
#
# Example 2:
#
# Input: nums = [1,2,1]
# Output: 0
#
#
#
# Constraints:
#
#     3 <= nums.length <= 104
#     1 <= nums[i] <= 106
#


import timeit
from math import prod
from typing import List, Optional, Set


def largestPerimeter(nums: List[int]) -> int:
    """
    The best way to get ahead is to get starting..?
    """
    # you need 3 numbers a,b,c that meet the conditions:
    #   a < b+c
    #   a > b >= c (implied by a=max())
    #   P = a+b+c  is maximal

    # find max pop into a
    # while nums
    # find 2n & 3rd max and pop into b & c
    # if all 3 conditions are met return P
    # else  b,c <-- a,b

    # # pythonic
    a = max(nums)
    nums.pop(nums.index(a))
    b = max(nums)
    nums.pop(nums.index(b))
    while nums:
        c = max(nums)
        nums.pop(nums.index(c))
        if a < b + c:  return a + b + c
        a, b = b, c
    return 0

    # # # algebraic
    # max_e = 0
    # max_group:set = set()
    # for i, n in nums:
    #     if n > max_e:
    #         if max_e:
    #             max_group.add(max_e)
    #         # index, max = i, n
    #         max_e = nums.pop(i)


def testing():
    result = largestPerimeter(nums=[2, 1, 2])
    # print(f"result: {result}")
    assert (5 == result)

    result = largestPerimeter(nums=[1, 2, 1])
    # print(f"result: {result}")
    assert (0 == result)

    result = largestPerimeter(nums=[2, 1, 2, 1])
    # print(f"result: {result}")
    assert (5 == result)

    result = largestPerimeter(nums=[2, 1, 2, 2])
    # print(f"result: {result}")
    assert (6 == result)

    result = largestPerimeter(nums=[2, 1, 2, 2, 2])
    # print(f"result: {result}")
    assert (6 == result)

    result = largestPerimeter(nums=[1, 2, 1, 1])
    # print(f"result: {result}")
    assert (3 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
