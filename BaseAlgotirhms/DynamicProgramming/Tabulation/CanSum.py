# CanSum in Dynamic Programing
# return True if target_sum can be constructed from any combination of array numbers (all positive)
#

import timeit
from typing import Dict, List, Set


# Solution 1 - Iterative with Tabulation -    O(n*m)
def CanSum(target_sum: int, arr: List[int]) -> bool:
    tbl: List[bool] = [False] * (target_sum + 1)

    tbl[0] = True

    for i in range(target_sum):
        if tbl[i]:
            for n in arr:
                if i + n <= target_sum:
                    tbl[i + n] = True

    return tbl[target_sum]


def testing():
    result = CanSum(7, [5, 3, 4, 7])
    assert (True == result)

    result = CanSum(7, [5, 3, 4])
    assert (True == result)

    result = CanSum(7, [5, 7])
    assert (True == result)

    result = CanSum(7, [2, 4])
    assert (False == result)

    result = CanSum(8, [2, 3, 5])
    assert (True == result)

    result = CanSum(300, [7, 14])
    assert (False == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=10)))
