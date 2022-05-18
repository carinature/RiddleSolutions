#
#   Date - 18.05.2022
#
#
# 242. Valid Anagram
# Easy
#
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.
#
#
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
#
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
#
#
#
# Constraints:
#
#     1 <= s.length, t.length <= 5 * 104
#     s and t consist of lowercase English letters.
#
#
#
import collections
from collections import defaultdict, Counter
from math import prod
import timeit
from typing import List, Optional, Set, Dict


def some_function(s: str, t: str) -> bool:
    """
    The best way to get ahead is to get starting..?
    """
    # # #     Solution 1 - Pythonic
    # return sorted(s) == sorted(t)

    # # # #     Soltion 2 - Algorithmic
    # if len(s) - len(t):
    #     return False
    # d = collections.defaultdict(int)
    # for c in s:
    #     d[c] += 1
    # for c in t:
    #     d[c] -= 1
    #     if d[c] < 0:
    #         return False
    # return True

    # # #     Soltion 2.2 - Algorithmic
    # for x, y in zip(s, t):
    #     d[x] += 1
    #     d[y] -= 1
    # return all(v == 0 for v in d.values())


def testing():
    result = some_function(s="anagram", t="nagaram")
    # print(f"result: {result}")
    assert (True == result)

    result = some_function(s="rat", t="car")
    # print(f"result: {result}")
    assert (False == result)

    # result = some_function(s="rat", t="car")
    # # print(f"result: {result}")
    # assert (124356 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
