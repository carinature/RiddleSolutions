#
#   Date - 16.05.2022
#
#
# You are given an integer array arr.
# Sort the integers in the array in ascending order by the number of 1's in their binary representation
# and in case of two or more integers have the same number of 1's you have to sort them in ascending order.
#
# Return the array after sorting it.
#
#
#
# Example 1:
#
# Input: arr = [0,1,2,3,4,5,6,7,8]
# Output: [0,1,2,4,8,3,5,6,7]
# Explantion: [0] is the only integer with 0 bits.
# [1,2,4,8] all have 1 bit.
# [3,5,6] have 2 bits.
# [7] has 3 bits.
# The sorted array by bits is [0,1,2,4,8,3,5,6,7]
#
# Example 2:
#
# Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
# Output: [1,2,4,8,16,32,64,128,256,512,1024]
# Explantion: All integers have 1 bit in the binary representation, you should just sort them in ascending order.
#
#
#
# Constraints:
#
#     1 <= arr.length <= 500
#     0 <= arr[i] <= 104
#
import functools
from math import prod
import timeit
from typing import List, Optional, Set


def sortByBits(arr: List[int]) -> List[int]:
    """
    The best way to get ahead is to get starting..?
    """

    # # Pythonic Solution
    return sorted(arr, key=lambda n: (bin(n).count('1'), n))



def testing():
    result = sortByBits(arr=[0, 1, 2, 3, 4, 5, 6, 7, 8])
    # print(f"result: {result}")
    assert ([0, 1, 2, 4, 8, 3, 5, 6, 7] == result)

    result = sortByBits(arr=[1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1])
    # print(f"result: {result}")
    assert ([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024] == result)

    # result = sortByBits(arr=124356)
    # # print(f"result: {result}")
    # assert (124356 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
