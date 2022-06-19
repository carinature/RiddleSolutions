#
#   Date - 01.06.2022
#
#
# template for binary tree questions
# including some basic DBG functionality - create from array (sorted or not), to list, repr...
#


import timeit
from typing import List, Optional


# Definition for singly-linked list.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    res = sol.some_function(TreeNode.arrayToBST(root))
    assert ([1, 3, 12, 0, 0] == root)

    root = [0]
    res = sol.some_function(TreeNode.arrayToBST(root))
    assert ([0] == root)

    root = [0, -1]
    res = sol.some_function(TreeNode.arrayToBST(root))
    assert ([-1, 0] == root)

    root = [0, 0]
    res = sol.some_function(TreeNode.arrayToBST(root))
    assert ([0, 0] == root)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (
        timeit.timeit(testing, number=10)))
