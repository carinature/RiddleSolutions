#
#   Date - 08.05.2022
#
#
# Given a string s consisting of some words separated by some number of spaces,
# return the length of the last word in the string.
#
# A word is a maximal substring consisting of non-space characters only.
#
#
#
# Example 1:
#
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
#
# Example 2:
#
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
#
# Example 3:
#
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
#
#
#
# Constraints:
#
#     1 <= s.length <= 104
#     s consists of only English letters and spaces ' '.
#     There will be at least one word in s.
#


import timeit
from typing import List, Optional, Set


def lengthOfLastWord(s: str) -> int:
    """
    The best way to get ahead is to get starting..?
    """
    # # # #   pythonic (and also faster)
    # for ss in s.rsplit(' ')[::-1]:
    #     if ss:
    #         return len(ss)
    return len(s.rstrip(' ').split(' ')[-1])

    # # #   algebraic (and for some reason slower)
    # counter = 0
    # i = len(s)
    # while ' ' == s[i - 1]:
    #     i -= 1
    # # i now points to the index of the last letter(-not-space)
    # while i and ' ' != s[i - 1]:
    #     counter += 1
    #     i -= 1
    # return counter


def testing():
    result = lengthOfLastWord(s="Hello World")
    # print(f"result: {result}")
    assert (5 == result)

    result = lengthOfLastWord(s="   fly me   to   the moon  ")
    # print(f"result: {result}")
    assert (4 == result)

    result = lengthOfLastWord(s="luffy is still joyboy")
    # print(f"result: {result}")
    assert (6 == result)

    result = lengthOfLastWord(s="s ")
    # print(f"result: {result}")
    assert (1 == result)

    result = lengthOfLastWord(s=" s ")
    # print(f"result: {result}")
    assert (1 == result)

    result = lengthOfLastWord(s=" s")
    # print(f"result: {result}")
    assert (1 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
