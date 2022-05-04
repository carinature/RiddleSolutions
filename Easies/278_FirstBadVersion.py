# You are a product manager and currently leading a team to develop a new product.
# Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
# which causes all the following ones to be bad.
#
# You are given an API bool isBadVersion(version) which returns whether version is bad.

# Implement a function to find the first bad version.
# You should minimize the number of calls to the API.

from typing import List
import time


def firstBadVersion(n: int, bad: int) -> int:
    # The isBadVersion API is already defined for you.
    def isBadVersion(version: int) -> bool:
        return version == bad

    left, right = 1, n
    while left < right:
        mid = left + (right - left) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left


bla = [1, 2, 3, 4, 5]

if __name__ == '__main__':
    result = firstBadVersion(n=5, bad=4)
    print(f"\nresult:{result}")
    result = firstBadVersion(n=1, bad=1)
    print(f"\nresult:{result}")
    # result = solution.search(nums=[3, 3], target=6)
    # print(f"\nresult:{result}")
