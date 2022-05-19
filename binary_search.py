#
#   Date - 18.05.2022
#
#
# Binary Search
#
#

from math import prod
import timeit
from typing import List, Optional, Set, Dict


# input is a SORTED array, O(logN)
def binary_search(l: List[int], e: int):
    left, right = 0, len(l)
    while left <= right:
        middle = left + (right - left) // 2
        if l[middle] < e:
            left = middle + 1
        elif l[middle] > e:
            right = middle
        else:
            return middle
    return -1


def testing():
    l = [1, 2, 4, 5, 9, 12]

    print(binary_search(l, 5))


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
