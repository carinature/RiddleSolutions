#
#   Date - 01.02.2022
#
#
# Given an array, rotate the array to the right by k steps, where k is non-negative.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
# Example 2:
#
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
#
#
#
# Constraints:
#
#     1 <= nums.length <= 105
#     -231 <= nums[i] <= 231 - 1
#     0 <= k <= 105

import timeit
from typing import List, Optional


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # n = len(nums)
    # if n == 1 or not k:
    #     return
    #
    # if n % 2:
    #     old_t = nums[0]
    #     for j in range(1, n+1):
    #         nums[(j * k) % n], old_t = old_t, nums[(j * k) % n]
    #
    # elif k:
    #     old_t = [nums[0], nums[1]]
    #     for j in range(1, n+1 // 2):
    #         nums[(j * k) % n], old_t[0] = old_t[0], nums[(j * k) % n]
    #         nums[(j * k + 1) % n], old_t[1] = old_t[1], nums[(j * k + 1) % n]

    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]

    print(f'nums: {nums}')


def testing():
    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate(nums, k=3)
    assert ([5, 6, 7, 1, 2, 3, 4] == nums)

    nums = [-1, -100, 3, 99]
    rotate(nums, k=2)
    assert ([3, 99, -1, -100] == nums)

    nums = [1]
    rotate(nums, k=4)
    assert ([1] == nums)

    nums = [1, 2]
    rotate(nums, k=1)
    assert ([2, 1] == nums)

    nums = [1, 2]
    rotate(nums, k=3)
    assert ([2, 1] == nums)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (timeit.timeit(testing, number=1)))
