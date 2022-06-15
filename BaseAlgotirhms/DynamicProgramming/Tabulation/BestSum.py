# BestSum in Dynamic Programing
# return the "best" (shortest) list of elements in the arr whose sum equals target
#

import timeit
from typing import Dict, List, Set, Optional


# # # Solution 1 - Recursive (Naive) - O(2^(n+m) )
def BestSum(target_sum: int, arr: List[int]) -> Optional[List[int]]:
    tbl = [None] * (target_sum + 1)
    tbl[0] = []
    for i in range(target_sum + 1):
        if tbl[i] is not None:
            for n in arr:
                if i + n <= target_sum and (tbl[i + n] is None or len(tbl[i + n]) > len(tbl[i]) + 1):
                    tbl[i + n] = tbl[i] + [n]

    return tbl[target_sum]


def testing():
    result = BestSum(7, [5, 3, 4])
    # print(f'result: {result}')
    assert (sorted([4, 3]) == result)

    result = BestSum(0, [5, 3, 4])
    assert ([] == result)

    result = BestSum(7, [5, 7])
    assert ([7] == result)

    result = BestSum(7, [5, 3, 4, 7])
    assert ([7] == result)  # or [4, 3] == result)

    result = BestSum(7, [7, 5, 3, 4])
    assert ([7] == result)  # or [4, 3] == result)

    result = BestSum(7, [2, 4])
    assert (None == result)

    result = BestSum(8, [2, 3, 5])
    assert (sorted([5, 3]) == result)

    result = BestSum(300, [7, 14])
    assert (None == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=10)))
