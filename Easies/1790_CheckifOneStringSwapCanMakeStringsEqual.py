#
#   Date - 08.05.2022
#
#
# You are given two strings s1 and s2 of equal length.
# A string swap is an operation where you choose two indices in a string
# (not necessarily different) and swap the characters at these indices.
#
# Return true if it is possible to make both strings equal
# by performing at most one string swap on exactly one of the strings.
# Otherwise, return false.
#
#
#
# Example 1:
#
# Input: s1 = "bank", s2 = "kanb"
# Output: true
# Explanation: For example, swap the first character with the last character of s2 to make "bank".
#
# Example 2:
#
# Input: s1 = "attack", s2 = "defend"
# Output: false
# Explanation: It is impossible to make them equal with one string swap.
#
# Example 3:
#
# Input: s1 = "kelb", s2 = "kelb"
# Output: true
# Explanation: The two strings are already equal, so no string swap operation is required.
#
#
#
# Constraints:
#
#     1 <= s1.length, s2.length <= 100
#     s1.length == s2.length
#     s1 and s2 consist of only lowercase English letters.
#
import itertools
import timeit
from math import prod
from typing import List, Optional, Set


def areAlmostEqual(s1: str, s2: str) -> bool:
    # # # solution 1 - O(n^2)
    if set(s1) != set(s2):
        return False
    s1, s2, l = list(s1), list(s2), len(s1)
    for i in range(l):
        for j in range(i, l):
            s1[i], s1[j] = s1[j], s1[i]
            if s1 == s2:
                return True
            s1[i], s1[j] = s1[j], s1[i]
    return False


def testing():
    result = areAlmostEqual(s1="bank", s2="kanb")
    # print(f"result: {result}")
    assert (True == result)

    result = areAlmostEqual(s1="attack", s2="defend")
    # print(f"result: {result}")
    assert (False == result)

    result = areAlmostEqual(s1="kelb", s2="kelb")
    # print(f"result: {result}")
    assert (True == result)

    result = areAlmostEqual(s1="kelb", s2="kele")
    # print(f"result: {result}")
    assert (False == result)

    result = areAlmostEqual(s1="kel", s2="kel")
    # print(f"result: {result}")
    assert (True == result)

    result = areAlmostEqual(s1="kel", s2="ken")
    # print(f"result: {result}")
    assert (False == result)

    result = areAlmostEqual(s1="kel", s2="knl")
    # print(f"result: {result}")
    assert (False == result)

    result = areAlmostEqual(s1="ke", s2="ke")
    # print(f"result: {result}")
    assert (True == result)

    result = areAlmostEqual(s1="ke", s2="kl")
    # print(f"result: {result}")
    assert (False == result)

    result = areAlmostEqual(s1="k", s2="k")
    # print(f"result: {result}")
    assert (True == result)

    result = areAlmostEqual(s1="k", s2="l")
    # print(f"result: {result}")
    assert (False == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
