#
#   Date - 18.05.2022
#
#
# Selection Sort
#   push every smallest item to front of the array and continue with the rest of (unsorted) array
#   O(n^2)
#

from math import prod
import timeit
from typing import List, Optional, Set, Dict


# very slow and O(n^2) worst case
def selection_sort(l: List[int]):
    i = 0
    while i < len(l):
        imin = i
        for j in range(i, len(l)):
            if l[j] < l[imin]:
                imin = j
        l[i], l[imin] = l[imin], l[i]
        i += 1
    print(l)
    return l


def testing():
    l = [4, 1, 5, 3, 2]

    selection_sort(l)

    # result = some_function(nums=124356)
    # print(f"result: {result}")
    # assert (124356 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
