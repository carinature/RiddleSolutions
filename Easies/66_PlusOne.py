#
#   Date - 27.07.2023
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
    def some_function(self, digits: List[int]) -> List[int]:
        """
        The best way to get ahead is to get starting...?
        """
        # Naive Pythonic Solution - O(n) time and O(1) space
        if not digits: return digits

        i = len(digits)
        overflow = 1
        while overflow and i:
            i -= 1
            overflow, digits[i] = divmod(digits[i] + 1, 10)

        return digits if not overflow else [1] + digits


def testing():
    sol = Solution()

    result = sol.some_function(digits=[1,2,3])
    # print(f"result: {result}")
    assert ([1,2,4] == result)

    result = sol.some_function(digits=[4,3,2,1])
    # print(f"result: {result}")
    assert ([4,3,2,2] == result)

    result = sol.some_function(digits=[9])
    # print(f"result: {result}")
    assert ([1,0] == result)

    result = sol.some_function(digits=[9,9])
    # print(f"result: {result}")
    assert ([1,0,0] == result)

    result = sol.some_function(digits=[])
    # print(f"result: {result}")
    assert ([] == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
