#
#   Date - 17.05.2022
#
#
# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the
#   number of nodes along the longest path from the root node down to the farthest leaf node.
#
#
#
# Example 1:
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
#
# Example 2:
#
# Input: root = [1,null,2]
# Output: 2
#
#
#
# Constraints:
#
#     The number of nodes in the tree is in the range [0, 104].
#     -100 <= Node.val <= 100

import timeit
from typing import List, Optional


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


def maxDepth(root: 'TreeNode') -> int:
    """
    Do not return anything, modify nums in-place instead.
    """

    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1


def testing():
    null = None

    nums = [3, 9, 20, null, null, 15, 7]
    maxDepth(TreeNode.create_tree(nums))
    assert (3 == nums)

    nums = [1, null, 2]
    maxDepth(TreeNode.create_tree(nums))
    assert (2 == nums)

    nums = [0]
    maxDepth(TreeNode.create_tree(nums))
    assert (1 == nums)

    nums = []
    maxDepth(TreeNode.create_tree(nums))
    assert (0 == nums)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (
        timeit.timeit(testing, number=100)))
