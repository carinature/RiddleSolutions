#
#   Date - 01.02.2022
#
#
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
#
#
# Example 1:
#
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#
# Example 2:
#
# Input: head = [1], n = 1
# Output: []
#
# Example 3:
#
# Input: head = [1,2], n = 1
# Output: [1]
#
#
#
# Constraints:
#
#     The number of nodes in the list is sz.
#     1 <= sz <= 30
#     0 <= Node.val <= 100
#     1 <= n <= sz
#
#
#
# Follow up: Could you do this in one pass?


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


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    hl = []
    while head:
        hl.append(head)
        head = head.next
    if len(hl) == n:
        return hl[0].next
    else:
        hl[~n].next = hl[~n].next.next
    return hl[0]


def testing():
    head = [1, 2, 3, 4, 5]
    n = 2
    head = removeNthFromEnd(ListNode.create_list_node(head), n)
    assert (head == [1, 2, 3, 5])

    head = [1]
    n = 1
    head = removeNthFromEnd(ListNode.create_list_node(head), n)
    assert (head == [] or head is None)

    head = [1, 2]
    n = 1
    head = removeNthFromEnd(ListNode.create_list_node(head), n)
    assert (head == [1])


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (timeit.timeit(testing, number=1)))
