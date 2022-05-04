#
#   Date - 02.02.2022
#
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.
#
#
# Example 1:
#
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
#
# Example 2:
#
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
#
#
#
# Constraints:
#
#     1 <= s.length <= 105
#     s[i] is a printable ascii character.

import timeit
from typing import List, Optional


def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(len(s) // 2): s[i], s[~i] = s[~i], s[i]


def testing():
    nums = ["h", "e", "l", "l", "o"]
    reverseString(nums)
    assert (["o", "l", "l", "e", "h"] == nums)

    nums = ["H", "a", "n", "n", "a", "h"]
    reverseString(nums)
    assert (["h", "a", "n", "n", "a", "H"] == nums)

    nums = ["H", "o", "n", "t", "a", "h"]
    reverseString(nums)
    assert (["h", "a", "t", "n", "o", "H"] == nums)

    # nums = [0, -1]
    # reverseString(nums)
    # assert ([-1, 0] == nums)
    #
    # nums = [0, 0]
    # reverseString(nums)
    # assert ([0, 0] == nums)
    #


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (timeit.timeit(testing, number=100000)))
    # testing()
