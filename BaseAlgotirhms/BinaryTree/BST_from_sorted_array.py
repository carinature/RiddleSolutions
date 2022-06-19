#
# Creating a Binary Search Tree
#


from typing import List, Optional


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
