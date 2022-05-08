#
#   Date - 08.05.2022
#
#
# There is a function signFunc(x) that returns:
#
#     1 if x is positive.
#     -1 if x is negative.
#     0 if x is equal to 0.
#
# You are given an integer array nums. Let product be the product of all values in the array nums.
#
# Return signFunc(product).
#
#
#
# Example 1:
#
# Input: nums = [-1,-2,-3,-4,3,2,1]
# Output: 1
# Explanation: The product of all values in the array is 144, and signFunc(144) = 1
#
# Example 2:
#
# Input: nums = [1,5,0,2,-3]
# Output: 0
# Explanation: The product of all values in the array is 0, and signFunc(0) = 0
#
# Example 3:
#
# Input: nums = [-1,1,-1,1,-1]
# Output: -1
# Explanation: The product of all values in the array is -1, and signFunc(-1) = -1
#
#
#
# Constraints:
#
#     1 <= nums.length <= 1000
#     -100 <= nums[i] <= 100
#


import timeit
from math import prod
from typing import List, Optional, Set


def arraySign( nums: List[int]) -> int:
    # # pythonic
    product = prod(nums)
    if product:
        return product//abs(product)
    return 0

    # # # algebraic
    # sign = 1
    # for n in nums:
    #     if not n:
    #         return 0
    #     sign *= n // abs(n)
    # return sign


def testing():
    result = arraySign(nums=[-1, -2, -3, -4, 3, 2, 1])
    # print(f"result: {result}")
    assert (1 == result)

    result = arraySign(nums=[1, 5, 0, 2, -3])
    # print(f"result: {result}")
    assert (0 == result)

    result = arraySign(nums=[-1, 1, -1, 1, -1])
    # print(f"result: {result}")
    assert (-1 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
