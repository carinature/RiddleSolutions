#
#   Date - 04.06.2022
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
    def numberOfSteps(self, num: int) -> int:
        # # # # Solution 1 - straightforward (but also good)
        # steps = 0
        # while num:
        #     num = num - 1 if num%2 else num // 2
        #     steps += 1
        # return steps

        # # Solution 2 - Bits
        return bin(num).count()


def testing():
    sol = Solution()

    result = sol.numberOfSteps(num=14)
    # print(f"result: {result}")
    assert (6 == result)

    result = sol.numberOfSteps(num=8)
    # print(f"result: {result}")
    assert (4 == result)

    result = sol.numberOfSteps(num=123)
    # print(f"result: {result}")
    assert (12 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
