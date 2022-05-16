#
#   Date - 16.05.2022
#
#
# Given head which is a reference node to a singly-linked list.
# The value of each node in the linked list is either 0 or 1.
# The linked list holds the binary representation of a number.
#
# Return the decimal value of the number in the linked list.
#
#
#
# Example 1:
#
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10
#
# Example 2:
#
# Input: head = [0]
# Output: 0
#
#
#
# Constraints:
#
#     The Linked List is not empty.
#     Number of nodes will not exceed 30.
#     Each node's value is either 0 or 1.

import timeit
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def create_list_node(nums: List[int]) -> 'ListNode':
        if not nums:
            return ListNode()
        tail = ListNode(nums[-1])
        for num in reversed(nums[:-1]):
            new_tail = ListNode(num, tail)
            tail = new_tail
        return tail

    def __eq__(self, other: List[int]):
        temp = self
        if not other: return temp.next is None
        for x in other:
            if x == temp.val:
                try:
                    temp = temp.next
                except:
                    return False
            else:
                return False
        return True


def getDecimalValue(head: ListNode) -> int:
    """
    Do not return anything, modify nums in-place instead.
    """
    val = 0
    while head:
        val += val + head.val
        head = head.next
    return val


def testing():
    nums = [1, 0, 1]
    res = getDecimalValue(ListNode.create_list_node(nums))
    assert (5 == res)

    nums = [0]
    res = getDecimalValue(ListNode.create_list_node(nums))
    assert (0 == res)

    # nums = [0, -1]
    # some_function(ListNode.create_list_node(nums))
    # assert ([-1, 0] == nums)
    #
    # nums = [0, 0]
    # some_function(ListNode.create_list_node(nums))
    # assert ([0, 0] == nums)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (
        timeit.timeit(testing, number=100)))
