# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n,
# where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
#
#
#   Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The nums1 of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
#
#   Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The nums1 of the merge is [1].
#
#   Example 3:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The nums1 of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge nums1 can fit in nums1.
#
#
#
# Constraints:
#
#     nums1.length == m + n
#     nums2.length == n
#     0 <= m, n <= 200
#     1 <= m + n <= 200
#     -109 <= nums1[i], nums2[j] <= 109

from typing import List
import time


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    while n > 0:
        if m <= 0 or nums2[n - 1] >= nums1[m - 1]:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
        else:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1

    # i, j = m, n
    # for k in range(m + n - 1, -1, -1):
    #     if not j:
    #         return
    #     if not i:
    #         nums1[:k + 1] = nums2[:j]
    #         return
    #     if nums2[j - 1] >= nums1[i - 1]:
    #         nums1[k] = nums2[j - 1]
    #         j -= 1
    #     else:
    #         nums1[k] = nums1[i - 1]
    #         i -= 1


if __name__ == '__main__':
    start_time = time.time()  # fixme

    nums1 = [1, 2, 3, 0, 0, 0]
    merge(nums1, m=3, nums2=[2, 5, 6], n=3)
    print(f"nums1: {nums1}")
    assert ([1, 2, 2, 3, 5, 6] == nums1)

    nums1 = [1]
    merge(nums1, m=1, nums2=[], n=0)
    print(f"nums1: {nums1}")
    assert ([1] == nums1)

    nums1 = [0]
    merge(nums1, m=0, nums2=[1], n=1)
    print(f"nums1: {nums1}")
    assert ([1] == nums1)

    nums1 = [0]
    merge(nums1, m=0, nums2=[0], n=1)
    print(f"nums1: {nums1}")
    assert ([0] == nums1)

    nums1 = []
    merge(nums1, m=0, nums2=[], n=0)
    print(f"nums1: {nums1}")
    assert ([] == nums1)

    nums1 = [0, 0, 0]
    merge(nums1, m=0, nums2=[1, 4, 5], n=3)
    print(f"nums1: {nums1}")
    assert ([1, 4, 5] == nums1)

    nums1 = [1, 4, 5]
    merge(nums1, m=3, nums2=[], n=0)
    print(f"nums1: {nums1}")
    assert ([1, 4, 5] == nums1)

    nums1 = [1, 4, 5, 0, 0, 0]
    merge(nums1, m=3, nums2=[-5, -4, 0], n=3)
    print(f"nums1: {nums1}")
    assert ([-5, -4, 0, 1, 4, 5] == nums1)

    nums1 = [1, 2, 3, 0, 0, 0]
    merge(nums1, m=3, nums2=[4, 5, 6], n=3)
    print(f"nums1: {nums1}")
    assert ([1, 2, 3, 4, 5, 6] == nums1)


    print("--- %.8f seconds ---" % (time.time() - start_time))  # fixme
