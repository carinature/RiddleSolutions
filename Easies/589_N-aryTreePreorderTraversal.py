#
#   Date - 11.05.2022
#
#
# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
#
# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the None value (See examples)
#
#
#
# Example 1:
#
# Input: root = [1,None,3,2,4,None,5,6]
# Output: [1,3,5,6,2,4]
#
# Example 2:
#
# Input: root = [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14]
# Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
#
#
#
# Constraints:
#
#     The number of nodes in the tree is in the range [0, 104].
#     0 <= Node.val <= 104
#     The height of the n-ary tree is less than or equal to 1000.
#
import itertools
import timeit
from math import prod
from typing import List, Optional, Set

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def preorder(root: 'Node') -> List[int]:
    if not root:
        return []
    order: List[int] = [root.val]
    for child in root.children:
        order.extend(preorder(child))
    return order


def testing():
    # result = preorder(root=[1, None, 3, 2, 4, None, 5, 6])
    # # print(f"result: {result}")
    # assert ([1, 3, 5, 6, 2, 4] == result)
    #
    # result = preorder(
    #     root=[1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10,
    #           None, None, 11, None, 12, None, 13, None, None, 14])
    # # print(f"result: {result}")
    # assert (False == result)
    #
    # result = preorder(root="sdjflk")
    # # print(f"result: {result}")
    # assert (True == result)

    pass


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))

