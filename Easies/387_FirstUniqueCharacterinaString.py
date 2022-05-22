#
#   Date - 22.05.2022
#
#
# 387. First Unique Character in a String
# Easy
#
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
#
#
#
# Example 1:
#
# Input: s = "leetcode"
# Output: 0
#
# Example 2:
#
# Input: s = "loveleetcode"
# Output: 2
#
# Example 3:
#
# Input: s = "aabb"
# Output: -1
#
#
#
# Constraints:
#
#     1 <= s.length <= 105
#     s consists of only lowercase English letters.
#


from math import prod
import timeit
from typing import List, Optional, Set, Dict
# from collections import defaultdict
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # # solution 1 - defaultdict
        ss = collections.defaultdict(int)
        for c in s:
            ss[c] += 1
        for i, c in enumerate(s):
            if ss[c] == 1:
                return i
        return -1

        # # solution 2 - counter
        # cntr = collections.Counter(s)
        # for i, c in enumerate(s):
        #     if cntr[c]==1:
        #         return i
        # return -1


def testing():
    sol = Solution()

    result = sol.firstUniqChar(s="leetcode")
    # print(f"result: {result}")
    assert (0 == result)

    result = sol.firstUniqChar(s="loveleetcode")
    # print(f"result: {result}")
    assert (2 == result)

    result = sol.firstUniqChar(s="aabb")
    # print(f"result: {result}")
    assert (-1 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
