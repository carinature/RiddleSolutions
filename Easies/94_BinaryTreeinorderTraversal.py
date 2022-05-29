#
#   Date - 28.05.2022
#
#
# 94. Binary Tree Inorder Traversal
# Easy
#
# Given the root of a binary tree, return the inorder traversal of its nodes' values.
#
#
#
# Example 1:
#
# Input: root = [1,null,2,3]
# Output: [1,3,2]
#
# Example 2:
#
# Input: root = []
# Output: []
#
# Example 3:
#
# Input: root = [1]
# Output: [1]
#
#
#
# Constraints:
#
#     The number of nodes in the tree is in the range [0, 100].
#     -100 <= Node.val <= 100
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
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

    def create_tree(root: List[int]) -> 'TreeNode':
        if not root:
            return TreeNode()
        head: TreeNode = TreeNode(root.pop(0), root.pop(1), root.pop(2))
        # for num in root[3:]:

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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


def testing():
    sol = Solution()

    root = [1, None, 2, 3]
    sol.inorderTraversal(TreeNode.create_tree(root))
    assert ([1, 2, 3] == root)

    root = []
    sol.inorderTraversal(TreeNode.create_tree(root))
    assert ([] == root)

    root = [1]
    sol.inorderTraversal(TreeNode.create_tree(root))
    assert ([1] == root)

    # root = [0, 0]
    # sol.preorderTraversal(TreeNode.create_tree(root))
    # assert ([0, 0] == root)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (
        timeit.timeit(testing, number=100)))
