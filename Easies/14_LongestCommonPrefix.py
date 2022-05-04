# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


from typing import List
import time


def longestCommonPrefix(strs: List[str]) -> str:
    res = ""
    i = 0
    try:
        while True:
            letters = set(s[i] for s in strs)
            if 1 == len(letters):
                res += letters.pop()
                i += 1
            else:
                raise
    finally:
        return res


if __name__ == '__main__':
    start_time = time.time()  # fixme
    result = longestCommonPrefix(strs=["flower", "flow", "flight"])
    print(f"\nresult:{result}")
    assert ("fl" == result)
    result = longestCommonPrefix(strs=["dog", "racecar", "car"])
    print(f"\nresult:{result}")
    assert ("" == result)
    result = longestCommonPrefix(strs=["dog"])
    print(f"\nresult:{result}")
    assert ("dog" == result)
    result = longestCommonPrefix(strs=[""])
    print(f"\nresult:{result}")
    assert ("" == result)
    result = longestCommonPrefix(strs=[])
    print(f"\nresult:{result}")
    assert ("" == result)
    print("--- %.8f seconds ---" % (time.time() - start_time))  # fixme
