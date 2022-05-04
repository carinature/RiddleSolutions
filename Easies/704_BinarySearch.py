# Given an array of integers nums which is sorted in ascending order, and an integer target,
# write a function to search target in nums.
# If target exists, then return its index.
# Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.
import timeit
from typing import List
import time


# def search(nums: List[int], target: int) -> int:
#     start, fin = 0, len(nums)
#     while start < fin:
#         mid = start + (fin - start) // 2
#         if target == nums[mid]:
#             return mid
#         if target > nums[mid]:
#             start = mid + 1
#         else:
#             fin = mid
#     return -1


def search(nums: List[int], target: int) -> int:
    start, fin = 0, len(nums)
    while start < fin:
        mid = start + (fin - start) // 2
        if target < nums[mid]:
            fin = mid
        elif target > nums[mid]:
            start = mid + 1
        else:
            return mid
    return -1


def testing():
    result = search(nums=[-1, 0, 3, 5, 9, 12], target=9)
    # print(f"\nresult:{result}")
    assert (4 == result)
    result = search(nums=[-1, 0, 3, 5, 9, 12], target=2)
    # print(f"\nresult:{result}")
    assert (-1 == result)
    # result = solution.search(nums=[3, 3], target=6)
    # print(f"\nresult:{result}")


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (timeit.timeit(testing, number=100000)))
    # testing()
