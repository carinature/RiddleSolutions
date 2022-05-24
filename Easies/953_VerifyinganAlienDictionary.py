#
#   Date - 24.05.2022
#
#
# 953. Verifying an Alien Dictionary
# Easy
#
# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order.
# The order of the alphabet is some permutation of lowercase letters.
#
# Given a sequence of words written in the alien language, and the order of the alphabet,
# return true if and only if the given words are sorted lexicographically in this alien language.
#
#
#
# Example 1:
#
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
#
# Example 2:
#
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
#
# Example 3:
#
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.)
# According to lexicographical rules "apple" > "app", because 'l' > '∅',
# where '∅' is defined as the blank character which is less than any other character (More info).
#
#
#
# Constraints:
#
#     1 <= words.length <= 100
#     1 <= words[i].length <= 20
#     order.length == 26
#     All characters in words[i] and order are English lowercase letters.
#


from math import prod
import timeit
from typing import List, Optional, Set, Dict
# from collections import defaultdict
import collections


class Solution:

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        The best way to get ahead is to get starting..?
        """

        vals = {order[i]: i for i in range(26)}
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]) or vals[words[i][j]] > vals[words[i + 1][j]]:
                    return False
                elif vals[words[i][j]] < vals[words[i + 1][j]]:
                    break
        return True

        # complexity - let's talk about it
        # init map O(26) = O(1)
        # for each word - check the adjacent word - O(n)
        #   for each letter -  O(l)
        #       check with prev word same letter - O(1)
        # todo learn to explain the alg in your words (not just pseudo/code)
        #         plus the complexity isn't really O(N*L)


def testing():
    sol = Solution()

    result = sol.isAlienSorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz")
    # print(f"result: {result}")
    assert (True == result)

    result = sol.isAlienSorted(words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz")
    # print(f"result: {result}")
    assert (False == result)

    result = sol.isAlienSorted(words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz")
    # print(f"result: {result}")
    assert (False == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
