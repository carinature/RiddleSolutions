# GreedTraveler in Dynamic Programing
# can only move in 2 directions out of four (e.g. right and down)
# on a mXn grid

import timeit
from typing import Dict


# Solution 1 - Recursive (Naive) - O(2^(n+m) )
def GridTraveler(m: int, n: int) -> int:
    # Tnai Azira
    if 1 == n and 1 == m:
        return 1
    # Sanity Check
    if not m or not n:
        return 0

    return GridTraveler(m - 1, n) + GridTraveler(m, n - 1)


# Solution 2 - Recursive with Memoization - O(n)
def GridTraveler(m: int, n: int, memo: Dict[str, int] = dict()) -> int:
    key = str(m) + ',' + str(n)
    if key in memo:
        return memo[key]
    # Tnai Azira
    if 1 == n and 1 == m:
        memo[key] = 1
        return 1
    # Sanity Check
    if 0 == m or 0 == n:
        memo[key] = 0
        return 0
    memo[key] = GridTraveler(m - 1, n) + GridTraveler(m, n - 1)
    return memo[key]


def testing():
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
          (timeit.timeit(testing, number=10000)))

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
