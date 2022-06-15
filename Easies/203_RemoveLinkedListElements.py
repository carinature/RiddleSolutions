#
#   Date - 16.05.2022
#
#
# 203. Remove Linked List Elements
# Easy
#
# Given the head of a linked list and an integer val,
# remove all the nodes of the linked list that has Node.val == val,
# and return the new head.
#
#
#
# Example 1:
#
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
#
# Example 2:
#
# Input: head = [], val = 1
# Output: []
#
# Example 3:
#
# Input: head = [7,7,7,7], val = 7
# Output: []
#
#
#
# Constraints:
#
#     The number of nodes in the list is in the range [0, 104].
#     1 <= Node.val <= 50
#     0 <= val <= 50

import timeit
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def create_list_node(nums: List[int]) -> 'ListNode':
        if not nums:
            return None
        tail = ListNode(nums[-1])
        for num in reversed(nums[:-1]):
            new_tail = ListNode(num, tail)
            tail = new_tail
        return tail

    def __eq__(self, other: List[int]) -> bool:
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

    def __repr__(self) -> str:
        tail: ListNode = self
        res: List[str] = []
        max_repe_len = 30  # in case of loops in linked list
        while tail and max_repe_len:
            res.append(str(tail.val))
            tail = tail.next
            max_repe_len -= 1
        return ' --> '.join(res)


def to_list(ln: Optional[ListNode]) -> List[int]:
    l = []
    while ln:
        l.append(ln.val)
        ln = ln.next
    return l


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Do not return anything, modify nums in-place instead.
        """
        dummy_head = ListNode(next=head)
        ptr = dummy_head
        while ptr.next:
            if ptr.next.val == val:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return dummy_head.next


def testing():
    sol = Solution()

    nums = [1, 2, 6, 3, 4, 5, 6]
    res = sol.removeElements(ListNode.create_list_node(nums), val=6)
    assert ([1, 2, 3, 4, 5] == to_list(res))

    nums = []
    res = sol.removeElements(ListNode.create_list_node(nums), val=1)
    # print(f'res {res}')
    assert ([] == to_list(res))

    nums = [7, 7, 7, 7]
    res = sol.removeElements(ListNode.create_list_node(nums), val=7)
    assert ([] == to_list(res))

    # nums = [0, 0]
    # res = sol.removeElements(ListNode.create_list_node(nums))
    # assert ([0, 0] == res)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (
        timeit.timeit(testing, number=100)))
