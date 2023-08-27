#
#   Date - 25.07.2023
#
#
# Given a string s, find the length of the longest substring without repeating characters.
#
#
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
#
#
# Constraints:
#
#     0 <= s.length <= 5 * 104
#     s consists of English letters, digits, symbols and spaces.
#


from math import prod
import timeit
from typing import List, Optional, Set, Dict
# from collections import defaultdict
import collections


class Solution:
    def some_function(self, haystack: str, needle: str) -> int:
        # # Pythonic Solution
        # try:
        #     return haystack.index(needle)
        # except:
        #     return -1

        # Naive Solution
        hlen, nlen = len(haystack), len(needle)
        for i in range(hlen - nlen + 1):
            j = 0
            while haystack[i + j] == needle[j]:
                j += 1
                if j == nlen:
                    return i
        return -1

        # Naive Solution #2 - not as good
        # hlen, nlen = len(haystack), len(needle)
        # i = j = 0
        # while i < hlen:
        #     if haystack[i] == needle[j]:
        #         j += 1
        #         if j == nlen:
        #             return i - j + 1
        #     else:
        #         i -= j
        #         j = 0
        #     i += 1
        # return -1





def testing():
    sol = Solution()

    result = sol.some_function(haystack="sadbutsad", needle="sad")
    # print(f"result: {result}")
    assert (0 == result)

    result = sol.some_function(haystack="leetcode", needle="leeto")
    # print(f"result: {result}")
    assert (-1 == result)

    result = sol.some_function(haystack="aaa", needle="aaaa")
    # print(f"result: {result}")
    assert (-1 == result)

    result = sol.some_function(haystack="aaa", needle="aaaaaa")
    # print(f"result: {result}")
    assert (-1 == result)

    result = sol.some_function(haystack="aaaaa", needle="aaaa")
    # print(f"result: {result}")
    assert (0 == result)

    result = sol.some_function(haystack="a", needle="a")
    # print(f"result: {result}")
    assert (0 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
