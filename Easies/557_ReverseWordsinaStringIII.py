#
#   Date - 03.02.2022
#
#
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
#
#
# Example 1:
#
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
#
# Example 2:
#
# Input: s = "God Ding"
# Output: "doG gniD"
#
#
#
# Constraints:
#
#     1 <= s.length <= 5 * 104
#     s contains printable ASCII characters.
#     s does not contain any leading or trailing spaces.
#     There is at least one word in s.
#     All the words in s are separated by a single space.


import timeit
from typing import List, Optional


def reverseWords(s: str) -> str:
    new: List[str] = [""]
    for i in range(len(s)-1, -1, -1):
        if s[i] != ' ':
            new[-1] += (s[i])
        else:
            new.append("")
    return ' '.join(new[::-1])

    # a perfect and fast solution from leetCodeUser
    # return " ".join([x[::-1] for x in s.split()])


def testing():
    result = reverseWords(s="Let's take LeetCode contest")
    # print(f"result: {result}")
    assert ("s'teL ekat edoCteeL tsetnoc" == result)

    result = reverseWords(s="God Ding")
    # print(f"result: {result}")
    assert ("doG gniD" == result)

    result = reverseWords(s="g")
    # print(f"result: {result}")
    assert ("g" == result)

    # # not sure this case is relevant considering the 4th constraint
    # result = reverseWords(s=" ")
    # # print(f"result: {result}")
    # assert (" " == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (timeit.timeit(testing, number=100000)))
