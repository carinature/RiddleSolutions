#
#   Date - 16.06.22
#
#
# 700. Search in a Binary Search Tree
# Easy
#
# You are given the root of a binary search tree (BST) and an integer val.
#
# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
#
#
#
# Example 1:
#
# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
#
# Example 2:
#
# Input: root = [4,2,7,1,3], val = 5
# Output: []
#
#
#
# Constraints:
#
#     The number of nodes in the tree is in the range [1, 5000].
#     1 <= Node.val <= 107
#     root is a binary search tree.
#     1 <= val <= 107
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
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:  # and root.val!=val:
            if root.val > val:
                root = root.left
            elif root.val < val:
                root = root.right
            else:
                break
        return root


def testing():
    sol = Solution()
    root = root = [4,2,7,1,3]
    val = 2
    sol.searchBST(TreeNode.create_tree(root), val)
    assert ([2,1,3] == root)

    root = [4,2,7,1,3]
    val = 5
    sol.searchBST(TreeNode.create_tree(root), val)
    assert ([] == root)




if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (
        timeit.timeit(testing, number=100)))
