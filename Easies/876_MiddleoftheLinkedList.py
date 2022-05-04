#
#   Date - 01.02.2022
#
#
# Given the head of a singly linked list, return the middle node of the linked list.
#
# If there are two middle nodes, return the second middle node.
#
#
#
# Example 1:
#
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
#
# Example 2:
#
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
#
#
#
# Constraints:
#
#     The number of nodes in the list is in the range [1, 100].
#     1 <= Node.val <= 100


import timeit
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode( head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Do not return anything, modify nums in-place instead.
    """
    node = head
    while head.next:
        head = head.next
        node = node.next
        if head.next:
            head = head.next
    return node


def testing():
    pass # check in leetcode
    # result = some_function(nums=124356)
    # print(f"result: {result}")
    # assert (124356 == result)
    #
    # result = some_function(nums=124356)
    # print(f"result: {result}")
    # assert (124356 == result)
    #
    # result = some_function(nums=124356)
    # print(f"result: {result}")
    # assert (124356 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (timeit.timeit(testing, number=1)))
