#
#   Date - 16.06.2022
#
#
# 226. Invert Binary Tree
# Easy
#
# Given the root of a binary tree, invert the tree, and return its root.
#
#
#
# Example 1:
#
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
#
# Example 2:
#
# Input: root = [2,1,3]
# Output: [2,3,1]
#
# Example 3:
#
# Input: root = []
# Output: []
#
#
#
# Constraints:
#
#     The number of nodes in the tree is in the range [0, 100].
#     -100 <= Node.val <= 100
#
#


import timeit
from typing import List, Optional


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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


def testing():
    sol = Solution()
    # root = [0, 1, 0, 3, 12]
    # sol.some_function(TreeNode.create_tree(root))
    # assert ([1, 3, 12, 0, 0] == root)
    #
    # root = [0]
    # sol.some_function(TreeNode.create_tree(root))
    # assert ([0] == root)
    #
    # root = [0, -1]
    # sol.some_function(TreeNode.create_tree(root))
    # assert ([-1, 0] == root)
    #
    # root = [0, 0]
    # sol.some_function(TreeNode.create_tree(root))
    # assert ([0, 0] == root)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (
        timeit.timeit(testing, number=100)))
