# GreedTraveler in Dynamic Programing
# can only move in 2 directions out of four (e.g. right and down)
# on a mXn grid

import timeit
from typing import Dict


# Solution 1 - Iterative with Tabulation -    O(n)
def GridTraveler(m: int, n: int) -> int:
    if not m * n:
        return 0

    tbl = [[0] * (n + 1) for _ in range(m + 1)]
    tbl[1] = [1 if i else 0 for i in range(n + 1)]

    for i in range(2, m + 1):
        for j in range(1, n + 1):
            tbl[i][j] = tbl[i - 1][j] + tbl[i][j - 1]

    return tbl[m][n]


def testing():
    result = GridTraveler(0, 1)
    assert (0 == result)

    result = GridTraveler(1, 0)
    assert (0 == result)

    result = GridTraveler(0, 0)
    assert (0 == result)

    result = GridTraveler(1, 1)
    assert (1 == result)

    result = GridTraveler(2, 3)
    assert (3 == result)

    result = GridTraveler(3, 2)
    # print(f'{result}')
    assert (3 == result)

    result = GridTraveler(3, 3)
    assert (6 == result)

    result = GridTraveler(18, 18)
    assert (2333606220 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=10)))

#
#
#
#
#
# Time complexity of the naive recursive alg would be an O(2^(m*n)):
# space complexity O(n)
#
#
#
# but for the memoized solution
# time complexity is O(m*n)
# space complexity stays the same
#
#
