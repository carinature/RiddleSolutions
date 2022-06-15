#
#   Date - 16.05.2022
#
#
# 83. Remove Duplicates from Sorted List
# Easy
#
# Given the head of a sorted linked list,
# delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.
#
#
#
# Example 1:
#
# Input: head = [1,1,2]
# Output: [1,2]
#
# Example 2:
#
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
#
#
#
# Constraints:
#
#     The number of nodes in the list is in the range [0, 300].
#     -100 <= Node.val <= 100
#     The list is guaranteed to be sorted in ascending order.
#

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

    # def __eq__(self, other: List[int]) -> bool:
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
    def deleteDuplicates(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Do not return anything, modify nums in-place instead.
        """

        # # # # Solution 1 - naive
        # ptr = head
        # while ptr:
        #     if ptr.next and ptr.val == ptr.next.val:
        #         ptr.next = ptr.next.next
        #     ptr = ptr.next
        # return head

        # # # Solution 2 - fast & slow pointes
        slow = head
        while slow:
            fast = slow
            while fast.next and fast.next.val == slow.val:
                fast.next = fast.next.next
            slow = fast.next
        return head


def testing():
    sol = Solution()

    nums = [1, 1, 2]
    res = sol.deleteDuplicates(ListNode.create_list_node(nums), val=6)
    # print(f'res {res}')
    assert ([1, 2] == to_list(res))

    nums = [1, 1, 2, 3, 3]
    res = sol.deleteDuplicates(ListNode.create_list_node(nums), val=7)
    assert ([1, 2, 3] == to_list(res))

    nums = []
    res = sol.deleteDuplicates(ListNode.create_list_node(nums), val=1)
    # print(f'res {res}')
    assert ([] == to_list(res))

    nums = [1, 2]
    res = sol.deleteDuplicates(ListNode.create_list_node(nums), val=6)
    # print(f'res {res}')
    assert ([1, 2] == to_list(res))

    nums = [1]
    res = sol.deleteDuplicates(ListNode.create_list_node(nums), val=6)
    # print(f'res {res}')
    assert ([1] == to_list(res))


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (
        timeit.timeit(testing, number=1000)))
