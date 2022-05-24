#
#   Date - 24.05.2022
#
#
# 1309. Decrypt String from Alphabet to Integer Mapping
# Easy
#
# You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:
#
#     Characters ('a' to 'i') are represented by ('1' to '9') respectively.
#     Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
#
# Return the string formed after mapping.
#
# The test cases are generated so that a unique mapping will always exist.
#
#
#
# Example 1:
#
# Input: s = "10#11#12"
# Output: "jkab"
# Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
#
# Example 2:
#
# Input: s = "1326#"
# Output: "acz"
#
#
#
# Constraints:
#
#     1 <= s.length <= 1000
#     s consists of digits and the '#' letter.
#     s will be a valid string such that mapping is always possible.
#
#


from math import prod
import timeit
from typing import List, Optional, Set, Dict
# from collections import defaultdict
import collections


class Solution:
    def freqAlphabets(self, s: str) -> str:
        # # Solution 1
        for i in range(10,27):
            s = s.replace(f'{i}#', chr(i+96))
        for i in range(1,10):
            s = s.replace(f'{i}', chr(i+96))
        return s

        # # # Solution 2 - slightly more elegent - NOTE the '#'*(i>9)
        # for i in range(26, 0, -1): s = s.replace(str(i) + '#' * (i > 9), chr(96 + i))
        # return s

        # res = []
        # i = len(s) - 1
        # while i > 0:
        #     if s[i] == '#':
        #         res.append(chr(96 + int(s[i - 2:i])))  # todo
        #         i -= 3
        #     else:
        #         res.append(chr(96 + int(s[i])))
        #         i -= 1
        #     print(f'res  {res}')
        # res.reverse()
        # return ''.join(res)

def testing():
    sol = Solution()

    result = sol.freqAlphabets(s="10#11#12")
    # print(f"result: {result}")
    assert ('jkab' == result)

    result = sol.freqAlphabets(s="1326#")
    # print(f"result: {result}")
    assert ('acz' == result)

    # result = sol.freqAlphabets(s='LOVELY')
    # # print(f"result: {result}")
    # assert ('lovely' == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
