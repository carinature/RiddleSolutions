#
#   Date - 15.05.2022
#
#
# You are given two strings word1 and word2.
#   Merge the strings by adding letters in alternating order, starting with word1.
#   If a string is longer than the other,
#   append the additional letters onto the end of the merged string.
#
# Return the merged string.
#
#
#
# Example 1:
#
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
#
# Example 2:
#
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b
# word2:    p   q   r   s
# merged: a p b q   r   s
#
# Example 3:
#
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q
# merged: a p b q c   d
#
#
#
# Constraints:
#
#     1 <= word1.length, word2.length <= 100
#     word1 and word2 consist of lowercase English letters.
#
#
from itertools import zip_longest, chain
from math import prod
import timeit
from typing import List, Optional, Set


def mergeAlternately(word1: str, word2: str) -> str:
    """
    The best way to get ahead is to get starting..?
    """
    # # # #   solution #1
    s: str = ""
    for w1, w2 in zip(word1, word2):
        s += w1 + w2
    l = len(s) // 2
    return s + word1[l:] + word2[l:]

    # # # #   solution #2
    # s: str = ""
    # m = min(len(word1), len(word2))
    # for i in range(m):
    #     s += word1[i] + word2[i]
    # return s + word1[m:] + word2[m:]

    # # #   solution from leetCode
    # return ''.join(chain(*zip_longest(word1, word2, fillvalue='')))


def testing():
    result = mergeAlternately(word1="abc", word2="pqr")
    # print(f"result: {result}")
    assert ("apbqcr" == result)

    result = mergeAlternately(word1="ab", word2="pqrs")
    # print(f"result: {result}")
    assert ("apbqrs" == result)

    result = mergeAlternately(word1="abcd", word2="pq")
    # print(f"result: {result}")
    assert ("apbqcd" == result)

    result = mergeAlternately(word1="a", word2="b")
    # print(f"result: {result}")
    assert ("ab" == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
