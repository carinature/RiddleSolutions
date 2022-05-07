#
#   Date - 04.05.2022
#
#
# Given two non-negative integers low and high.
#   Return the count of odd numbers between low and high (inclusive).
#
#
#
# Example 1:
#
# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].
#
# Example 2:
#
# Input: low = 8, high = 10
# Output: 1
# Explanation: The odd numbers between 8 and 10 are [9].
#
#
#
# Constraints:
#
#     0 <= low <= high <= 10^9
#


import timeit
from typing import List, Optional, Set


def countOdds(low: int, high: int) -> int:
    """
    The best way to get ahead is to get starting..?
    """
    return (high - low) // 2 + (high + low + high * low) % 2
    # but an even more elegant solution:
    #   return  (high + 1) // 2 - low // 2


def testing():
    print(" --------------------------- ")

    result = countOdds(low=3, high=7)
    print(f"result: {result}")
    assert (3 == result)  # 7-3 = 4

    result = countOdds(low=2, high=7)
    print(f"result: {result}")
    assert (3 == result)  # 7-2 = 5

    result = countOdds(low=3, high=8)
    print(f"result: {result}")
    assert (3 == result)  # 8-3 = 5

    result = countOdds(low=2, high=8)
    print(f"result: {result}")
    assert (3 == result)  # 8-2 = 6

    result = countOdds(low=8, high=10)
    print(f"result: {result}")
    assert (1 == result)

    result = countOdds(low=9, high=11)
    print(f"result: {result}")
    assert (2 == result)

    result = countOdds(low=3, high=3)
    print(f"result: {result}")
    assert (1 == result)

    result = countOdds(low=2, high=3)
    print(f"result: {result}")
    assert (1 == result)

    result = countOdds(low=3, high=4)
    print(f"result: {result}")
    assert (1 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
