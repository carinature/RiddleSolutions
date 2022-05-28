#
#   Date - 28.05.2022
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


# Definition for singly-linked list.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def create_tree(nums: List[int]) -> 'TreeNode':
        if not nums:
            return TreeNode()
        head: TreeNode = TreeNode(nums.pop(0), nums.pop(1), nums.pop(2))
        # for num in nums[3:]:

    # def __eq__(self, other: List[int]):
    #     temp = self
    #     if not other: return temp.next is None
    #     for x in other:
    #         if x == temp.val:
    #             try:
    #                 temp = temp.next
    #             except:
    #                 return False
    #         else:
    #             return False
    #     return True


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


def testing():
    sol = Solution()

    nums = [0, 1, 0, 3, 12]
    sol.some_function(TreeNode.create_tree(nums))
    assert ([1, 3, 12, 0, 0] == nums)

    nums = [0]
    sol.some_function(TreeNode.create_tree(nums))
    assert ([0] == nums)

    nums = [0, -1]
    sol.some_function(TreeNode.create_tree(nums))
    assert ([-1, 0] == nums)

    nums = [0, 0]
    sol.some_function(TreeNode.create_tree(nums))
    assert ([0, 0] == nums)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (
        timeit.timeit(testing, number=100)))
