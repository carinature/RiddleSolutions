#
#   Date - 19.06.2022
#
#
# 653. Two Sum IV - Input is a BST
# Easy
#
# Given the root of a Binary Search Tree and a target number k,
# return true if there exist two elements in the BST such that their sum is equal to the given target.
#
#
#
# Example 1:
#
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
#
# Example 2:
#
# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false
#
#
#
# Constraints:
#
#     The number of nodes in the tree is in the range [1, 104].
#     -104 <= Node.val <= 104
#     root is guaranteed to be a valid binary search tree.
#     -105 <= k <= 105
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

    def sortedArrayToBST(self, nums: List[int]) -> Optional['TreeNode']:
        if not nums:
            return None
        return TreeNode(nums[len(nums) // 2],
                        self.sortedArrayToBST(nums[:len(nums) // 2]),
                        self.sortedArrayToBST(nums[len(nums) // 2 + 1:])
                        )

    def arrayToBST(nums: List[int]) -> Optional['TreeNode']:
        if not nums:
            return None
        root = TreeNode(nums.pop(0))
        st = [root]
        while nums:
            node = st.pop(0)
            if node:
                l = nums.pop(0)
                r = nums.pop(0)
                node.left = TreeNode(l) if l is not None else None
                node.right = TreeNode(r) if r is not None else None
                st += [node.left, node.right]
        # print(f'root {root}')
        return root

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
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # print(f'root: {root}')

        st = [root]
        s = set()
        for node in st:
            if node is not None:
                if node.val in s:
                    return True
                s.add(k - node.val)
                st += [node.left, node.right]

        return False


def testing():
    sol = Solution()

    nums = [5, 3, 6, 2, 4, None, 7]
    k = 9
    res = sol.findTarget(TreeNode.arrayToBST(nums), k)
    assert (True == res)

    nums = [5, 3, 6, 2, 4, None, 7]
    k = 28
    res = sol.findTarget(TreeNode.arrayToBST(nums), k)
    assert (False == res)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (
        timeit.timeit(testing, number=1000)))
