#
#   Date - 23.03.2022
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


import timeit
from typing import List, Optional, Set


def lengthOfLongestSubstring(s: str) -> int:
    """
    A journey of a thousand Miles starts with one step.
    """
    #   option 1
    temp_set: Set[str] = set()
    max_len = 0
    # set_size = 0
    for c in s:
        if c in temp_set:
            max_len = max(len(temp_set), max_len)
            temp_set = {c}
            # set_size = 1
        else:
            temp_set.add(c)
            # set_size += 1
    return max(len(temp_set), max_len)

    # #   option 2
    # temp_set: Set[str] = set()
    # max_len = 0
    # for c in s:
    #     set_size = len(temp_set)
    #     temp_set.add(c)
    #     if set_size == len(temp_set):
    #         temp_set.clear()
    #         temp_set.add(c)
    #         max_len = max(set_size, max_len)
    # return max(len(temp_set), max_len)


def testing():
    result = lengthOfLongestSubstring(s="abcabcbb")
    print(f"result: {result}")
    assert (3 == result)

    result = lengthOfLongestSubstring(s="bbbb")
    print(f"result: {result}")
    assert (1 == result)

    result = lengthOfLongestSubstring(s="pwwkew")
    print(f"result: {result}")
    assert (3 == result)

    result = lengthOfLongestSubstring(s="dvdf")
    print(f"result: {result}")
    assert (3 == result)

    result = lengthOfLongestSubstring(s="")
    print(f"result: {result}")
    assert (0 == result)

    result = lengthOfLongestSubstring(s=" ")
    print(f"result: {result}")
    assert (1 == result)

    result = lengthOfLongestSubstring(s="  ")
    print(f"result: {result}")
    assert (1 == result)

    result = lengthOfLongestSubstring(s="1234")
    print(f"result: {result}")
    assert (4 == result)

    result = lengthOfLongestSubstring(s="12 ab ")
    print(f"result: {result}")
    assert (5 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (timeit.timeit(testing,
                                                                 number=100
                                                                 )))
