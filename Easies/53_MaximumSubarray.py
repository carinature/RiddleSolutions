#
#   Date - 01.02.2022
#   Date - 18.05.2022
#
#
# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
#
# A subarray is a contiguous part of an array.
#
#
#
# Example 1:
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
# Example 2:
#
# Input: nums = [1]
# Output: 1
#
# Example 3:
#
# Input: nums = [5,4,-1,7,8]
# Output: 23
#
#
#
# Constraints:
#
#     1 <= nums.length <= 105
#     -104 <= nums[i] <= 104
#
#
#
# Follow up: If you have figured out the O(n) solution,
# try coding another solution using the divide and conquer approach, which is more subtle.


import timeit
from typing import List, Optional, Tuple


def maxSubArray(nums: List[int]) -> int:
    pass
    # if len(nums) == 1:
    #     return nums[0]
    #
    # sums: List[int] = [0] * (len(nums)+1)
    #
    # for i in range(1, 1+len(nums)):
    #     sums[i] = sums[i-1] + nums[i-1]
    #
    # mx = max(sums[1:])
    # mn = min(sums[: sums.index(mx)])
    # imn = sums.index(mn)
    #
    # # return mx-sums[imn-1]
    # # return mx-nums[imn]
    # return mx-mn


def testing():
    result = maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(f"result: {result}")
    assert (6 == result)

    result = maxSubArray(nums=[1])
    print(f"result: {result}")
    assert (1 == result)

    result = maxSubArray(nums=[5, 4, -1, 7, 8])
    print(f"result: {result}")
    assert (23 == result)

    result = maxSubArray(nums=[-1])
    print(f"result: {result}")
    assert (-1 == result)

    result = maxSubArray(nums=[-2, -1])
    print(f"result: {result}")
    assert (-1 == result)

    result = maxSubArray(nums=[-1, -2])
    print(f"result: {result}")
    assert (-1 == result)

    result = maxSubArray(nums=[-1, 0, -2])
    print(f"result: {result}")
    assert (0 == result)

    result = maxSubArray(nums=[-2, 1])
    print(f"result: {result}")
    assert (1 == result)

    result = maxSubArray(nums=[-2, -1, -2])
    print(f"result: {result}")
    assert (-1 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (timeit.timeit(testing, number=1)))
