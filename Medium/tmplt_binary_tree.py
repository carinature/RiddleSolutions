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

    def sortedArrayToBST(self, nums: List[int]) -> Optional['TreeNode']:
        if not nums:
            return None
        return TreeNode(nums[len(nums) // 2],
                        self.sortedArrayToBST(nums[:len(nums) // 2]),
                        self.sortedArrayToBST(nums[len(nums) // 2 + 1:])
                        )

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

    def __repr__(self):
        return f'{self.val} [LEFT {self.left}, RIGHT {self.right}]'

    def to_list(self):
        st = [self]
        res = []
        while st:
            node = st.pop(0)
            if node:
                res.append(node.val)
                st += [node.left, node.right]
            else:
                res.append(None)
        # remove tail Nones:
        while not res[-1]:
            res.pop()
        return res


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
