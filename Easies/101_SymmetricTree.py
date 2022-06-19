#
#   Date - 17.06.2022
#
#
# 101. Symmetric Tree
# Easy
#
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
#
#
#
# Example 1:
#
# Input: root = [1,2,2,3,4,4,3]
# Output: true
#
# Example 2:
#
# Input: root = [1,2,2,null,3,null,3]
# Output: false
#
#
#
# Constraints:
#
#     The number of nodes in the tree is in the range [1, 1000].
#     -100 <= Node.val <= 100
#
#
# Follow up: Could you solve it both recursively and iteratively?
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left, right = [root.left], [root.right]
        while left and right:
            l = left.pop()
            r = right.pop()
            if not l and not r:
                continue
            if not l or not r or l.val != r.val:
                return False
            left += [l.left, l.right]
            right += [r.right, r.left]
        return not (left or right)


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
