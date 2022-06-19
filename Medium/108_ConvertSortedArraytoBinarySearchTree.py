#
#   Date - 19.06.2022
#
#
# 108. Convert Sorted Array to Binary Search Tree
# Easy
#
# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.
#
# A height-balanced binary tree is a binary tree in which
# the depth of the two subtrees of every node never differs by more than one.
#
#
#
# Example 1:
#
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
#
# Example 2:
#
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
#
#
#
# Constraints:
#
#     1 <= nums.length <= 104
#     -104 <= nums[i] <= 104
#     nums is sorted in a strictly increasing order.
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
        while res[-1] is None:
            res.pop()
        return res


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        return TreeNode(nums[len(nums) // 2],
                        self.sortedArrayToBST(nums[:len(nums) // 2]),
                        self.sortedArrayToBST(nums[len(nums) // 2 + 1:])
                        )


def testing():
    sol = Solution()

    # sol.sortedArrayToBST(TreeNode.create_tree(root))
    res = sol.sortedArrayToBST(nums=[-10, -3, 0, 5, 9])
    # print(f'res {res}')
    # print(f'res.to_list() {res.to_list()}')
    assert ([0, -3, 9, -10, None, 5] == res.to_list()
            or [0, -10, 5, None, -3, None, 9] == res.to_list())

    res = sol.sortedArrayToBST([1, 3])
    assert ([1, None, 3] == res.to_list() or [3, 1] == res.to_list())

    res = sol.sortedArrayToBST([0])
    assert ([0] == res.to_list())


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (
        timeit.timeit(testing, number=10)))
