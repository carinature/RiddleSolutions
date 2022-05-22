#
#   Date - 22.05.2022
#
#
# 383. Ransom Note
# Easy
#
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
#
#
#
# Example 1:
#
# Input: ransomNote = "a", magazine = "b"
# Output: false
#
# Example 2:
#
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
#
# Example 3:
#
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
#
#
#
# Constraints:
#
#     1 <= ransomNote.length, magazine.length <= 105
#     ransomNote and magazine consist of lowercase English letters.
#


from math import prod
import timeit
from typing import List, Optional, Set, Dict
# from collections import defaultdict
import collections


class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        The best way to get ahead is to get starting..?
        """
        # # # Solution 1 - Pythonic using Counter
        # return all(collections.Counter(magazine)[c] >= n for c, n in collections.Counter(ransomNote).items())

        # # # Solution 1.2 - Pythonic using Counter
        # return not collections.Counter(ransomNote) - collections.Counter(magazine)

        # # # Solution 2 - Pythonic using str.replace - fastest
        for c in ransomNote:
            if c not in magazine:
                return False
            magazine = magazine.replace(c, '', 1)
        return True


        # for i in set(ransomNote):
        #     if ransomNote.count(i) > magazine.count(i):
        #         return False
        # return True



def testing():
    sol = Solution()

    result = sol.canConstruct(ransomNote="a", magazine="b")
    # print(f"result: {result}")
    assert (False == result)

    result = sol.canConstruct(ransomNote="aa", magazine="ab")
    # print(f"result: {result}")
    assert (False == result)

    result = sol.canConstruct(ransomNote="aa", magazine="aab")
    # print(f"result: {result}")
    assert (True == result)

    result = sol.canConstruct(ransomNote="bg", magazine="efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj")
    # print(f"result: {result}")
    assert (True == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
