# Given a sorted array of distinct integers and a target value,
# return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.

from typing import List
import time


def search_insert(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)
    while l < r:
        m = l + (r - l) // 2
        if target < nums[m]:
            r = m
        elif target > nums[m]:
            l = m + 1
        else:
            return m
    return l


if __name__ == '__main__':
    start_time = time.time()  # fixme
    result = search_insert(nums=[1, 3, 5, 6], target=5)
    print(f"\nresult:{result}")
    result = search_insert(nums=[1, 3, 5, 6], target=2)
    print(f"\nresult:{result}")
    result = search_insert(nums=[1, 3, 5, 6], target=7)
    print(f"\nresult:{result}")
    result = search_insert(nums=[1, 3], target=2)
    print(f"\nresult:{result}")
    print("--- %.8f seconds ---" % (time.time() - start_time))  # fixme
