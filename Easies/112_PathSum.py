#
#   Date - 16.06.2022
#
#
# 112. Path Sum
# Easy
#
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
#
# A leaf is a node with no children.
#
#
#
# Example 1:
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.
#
# Example 2:
#
# Input: root = [1,2,3], targetSum = 5
# Output: false
# Explanation: There two root-to-leaf paths in the tree:
# (1 --> 2): The sum is 3.
# (1 --> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.
#
# Example 3:
#
# Input: root = [], targetSum = 0
# Output: false
# Explanation: Since the tree is empty, there are no root-to-leaf paths.
#
#
#
# Constraints:
#
#     The number of nodes in the tree is in the range [0, 5000].
#     -1000 <= Node.val <= 1000
#     -1000 <= targetSum <= 1000
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
    def some_function(self, root: Optional['TreeNode']) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        print(f'root: {root}')


def testing():
    sol = Solution()
    root = [0, 1, 0, 3, 12]
    sol.some_function(TreeNode.create_tree(root))
    assert ([1, 3, 12, 0, 0] == root)

    root = [0]
    sol.some_function(TreeNode.create_tree(root))
    assert ([0] == root)

    root = [0, -1]
    sol.some_function(TreeNode.create_tree(root))
    assert ([-1, 0] == root)

    root = [0, 0]
    sol.some_function(TreeNode.create_tree(root))
    assert ([0, 0] == root)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (
        timeit.timeit(testing, number=100)))
