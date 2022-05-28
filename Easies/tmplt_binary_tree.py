#
#   Date - 01.06.2022
#
#
# Given an integer array root, move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
#
#
#       Example 1:
# Input: root = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
#       Example 2:
# Input: root = [0]
# Output: [0]
#
#
#       Constraints:
#     1 <= root.length <= 104
#     -231 <= root[i] <= 231 - 1
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
