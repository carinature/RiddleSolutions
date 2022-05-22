#
#   Date - 01.02.2022
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


    def some_function(self, nums: Optional[int]) -> Optional[int]:
        """
        The best way to get ahead is to get starting..?
        """
        return 124356


def testing():
    sol = Solution()
    
    result = sol.some_function(nums=124356)
    # print(f"result: {result}")
    assert (124356 == result)

    result = sol.some_function(nums=124356)
    # print(f"result: {result}")
    assert (124356 == result)

    result = sol.some_function(nums=124356)
    # print(f"result: {result}")
    assert (124356 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
