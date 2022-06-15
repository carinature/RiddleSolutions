# HowSum in Dynamic Programing
# return the list of elements in the arr whose sum equals target
#

import timeit
from typing import Dict, List, Set, Optional


# Solution 1 - Iterative with Tabulation -    O(n*m)
def HowSum(target_sum: int, arr: List[int]) -> Optional[List[int]]:
    tbl: List[List[int]] = [None] * (target_sum + 1)
    tbl[0] = []

    for i in range(target_sum + 1):
        if tbl[i] is not None:
            for n in arr:
                if i + n <= target_sum:
                    tbl[i + n] = tbl[i] + [n]

    return tbl[target_sum]


def testing():
    result = HowSum(7, [5, 3, 4])
    assert ([4, 3] == result)

    result = HowSum(0, [5, 3, 4])
    assert ([] == result)

    result = HowSum(7, [5, 7])
    assert ([7] == result)

    result = HowSum(7, [5, 3, 4, 7])
    assert ([7] == result or [4, 3] == result)

    result = HowSum(7, [2, 4])
    assert (None == result)

    result = HowSum(8, [2, 3, 5])
    # print(f'result: {result}')
    assert ([2, 2, 2, 2] == result or [2, 3, 3] == result or [5, 3] == result)

    result = HowSum(300, [7, 14])
    assert (None == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=10)))
