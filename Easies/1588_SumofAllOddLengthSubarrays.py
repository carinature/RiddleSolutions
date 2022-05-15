#
#   Date - 15.05.2022
#
#
# Given an array of positive integers arr,
# calculate the sum of all possible odd-length subarrays.
#
# A subarray is a contiguous subsequence of the array.
#
# Return the sum of all odd-length subarrays of arr.
#
#
#
# Example 1:
#
# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
#
# Example 2:
#
# Input: arr = [1,2]
# Output: 3
# Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
#
# Example 3:
#
# Input: arr = [10,11,12]
# Output: 66
#
#
#
# Constraints:
#
#     1 <= arr.length <= 100
#     1 <= arr[i] <= 1000
#


from math import prod
import timeit
from typing import List, Optional, Set


def sumOddLengthSubarrays(arr: List[int]) -> int:
    """
    The best way to get ahead is to get starting..?
    """
    #   fixme there's a much more efficient solution
    return sum(
        [sum(
            [sum(
                arr[i:i + l])
                for i in range(len(arr) - l + 1)])
            for l in range(1, len(arr) + 1, 2)])


def testing():
    result = sumOddLengthSubarrays(arr=[1, 4, 2, 5, 3])
    # print(f"result: {result}")
    assert (58 == result)

    result = sumOddLengthSubarrays(arr=[1, 2])
    # print(f"result: {result}")
    assert (3 == result)

    result = sumOddLengthSubarrays(arr=[10, 11, 12])
    # print(f"result: {result}")
    assert (66 == result)

    result = sumOddLengthSubarrays(arr=[2])
    # print(f"result: {result}")
    assert (2 == result)

    result = sumOddLengthSubarrays(arr=[1, 2, 3, 4, 5, 6])
    # print(f"result: {result}")
    assert (98 == result)

    result = sumOddLengthSubarrays(arr=[1, 2, 3, 4, 5, 6, 7])
    # print(f"result: {result}")
    assert (176 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
