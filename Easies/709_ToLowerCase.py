#
#   Date - 24.05.2022
#
#
# 1709. To Lower Case
# Easy
#
# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
#
#
#
# Example 1:
#
# Input: s = "Hello"
# Output: "hello"
#
# Example 2:
#
# Input: s = "here"
# Output: "here"
#
# Example 3:
#
# Input: s = "LOVELY"
# Output: "lovely"
#
#
#
# Constraints:
#
#     1 <= s.length <= 100
#     s consists of printable ASCII characters.
#
#


from math import prod
import timeit
from typing import List, Optional, Set, Dict
# from collections import defaultdict
import collections


class Solution:
    def toLowerCase(self, s: str) -> str:
        # # # Solution 1
        # return ''.join([chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in s])

        # # # Solution 2 - with dict - slower
        # d = {chr(i + 97 - 32): chr(i + 97) for i in range(26)}
        # for c in d:
        #     s = s.replace(c, d[c])
        # return s

        # # # Solution 3 - pythonic
        return s.lower()


def testing():
    sol = Solution()

    result = sol.toLowerCase(s="Hello")
    # print(f"result: {result}")
    assert ('hello' == result)

    result = sol.toLowerCase(s='here')
    # print(f"result: {result}")
    assert ('here' == result)

    result = sol.toLowerCase(s='LOVELY')
    # print(f"result: {result}")
    assert ('lovely' == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
