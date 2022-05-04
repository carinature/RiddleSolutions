# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#
#     1. Open brackets must be closed by the same type of brackets.
#     2. Open brackets must be closed in the correct order.
#
#
#
# Example 1:
# Input: s = "()"
# Output: true
#
# Example 2:
# Input: s = "()[]{}"
# Output: true
#
# Example 3:
# Input: s = "(]"
# Output: false


from typing import List
import time


def isValid(s: str) -> bool:
    stack = []
    dct = {"(": ")", "[": "]", "{": "}"}
    bset = set("([{")
    for c in s:
        if c in bset:
            stack += dct[c]
        elif not stack or c != stack.pop():
            return False
    return not stack


if __name__ == '__main__':
    start_time = time.time()  # fixme
    result = isValid(s="()")
    print(f"\nresult:{result}")
    assert result
    result = isValid(s="()[]{}")
    print(f"\nresult:{result}")
    assert result
    result = isValid(s="(]")
    print(f"\nresult:{result}")
    assert not result
    result = isValid(s="([]){()}")
    print(f"\nresult:{result}")
    assert result
    result = isValid(s="([()[]])")
    print(f"\nresult:{result}")
    assert result
    result = isValid(s="([()[])])")
    print(f"\nresult:{result}")
    assert not result
    result = isValid(s="([()[])]))")
    print(f"\nresult:{result}")
    assert not result
    result = isValid(s="(")
    print(f"\nresult:{result}")
    assert not result
    result = isValid(s="]")
    print(f"\nresult:{result}")
    assert not result
    print("--- %.8f seconds ---" % (time.time() - start_time))  # fixme
