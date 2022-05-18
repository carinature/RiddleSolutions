#
#   Date - 01.02.2022
#
#
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays
# and you may return the result in any order.
#
#
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
#
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
#
#
#
# Constraints:
#
#     1 <= nums1.length, nums2.length <= 1000
#     0 <= nums1[i], nums2[i] <= 1000
#
#
#
# Follow up: #todo
#
#     What if the given array is already sorted? How would you optimize your algorithm?
#     What if nums1's size is small compared to nums2's size? Which algorithm is better?
#     What if elements of nums2 are stored on disk,
#       and the memory is limited such that you cannot load all elements into the memory at once?


import timeit
from collections import defaultdict
from typing import List, Optional


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:

    if not nums1 or not nums2: return []
    nums1.sort()
    nums2.sort()
    i, j = 0, 0
    res: List[int] = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            j += 1

        elif nums1[i] < nums2[j]:
            i += 1

        else:
            res.append(nums1[i])
            i += 1
            j += 1

    return res

    # todo - *after* solving, consider also *all* the follow-up questions


def testing():
    result = intersect(nums1=[1, 2, 2, 1], nums2=[2, 2])
    print(f"result: {result}")
    assert ([2, 2] == result)

    result = intersect([4, 9, 5], nums2=[9, 4, 9, 8, 4])
    print(f"result: {result}")
    assert ([4, 9] == result or [9, 4] == result)

    # result = intersect(nums=124356)
    # print(f"result: {result}")
    # assert (124356 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (timeit.timeit(testing, number=1)))
