#
#   Date - 24.05.2022
#
#
# 141. Linked List Cycle
# Easy
#
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
#
# There is a cycle in a linked list if there is some node in the list
# that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
# Note that pos is not passed as a parameter.
#
# Return true if there is a cycle in the linked list. Otherwise, return false.
#
#
#
# Example 1:
#
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
#
# Example 2:
#
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
#
# Example 3:
#
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#
#
#
# Constraints:
#
#     The number of the nodes in the list is in the range [0, 104].
#     -105 <= Node.val <= 105
#     pos is -1 or a valid index in the linked-list.
#
#
#
# Follow up: Can you solve it using O(1) (i.e. constant) memory?
#


from math import prod
import timeit
from typing import List, Optional, Set, Dict
import collections  # from collections import defaultdict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        # print(f'{self.next}')

    def create_list_node(nums: List[int]) -> 'ListNode':
        if not nums:
            return ListNode()
        tail = ListNode(nums[-1])
        for num in reversed(nums[:-1]):
            new_tail = ListNode(num, tail)
            tail = new_tail
        return tail

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
        tail: ListNode = self
        res: List[str] = []
        max_repe_len = 30
        while tail and max_repe_len:
            res.append(str(tail.val))
            tail = tail.next
            max_repe_len -= 1
        return ' --> '.join(res)

    def __hash__(self):
        return id(self)

    def update_pos(self, pos):
        if pos < 0:
            return self
        ptr = self
        for _ in range(pos):
            ptr = ptr.next
        tail = self
        while tail.next:
            tail = tail.next
        tail.next = ptr
        # print(f'self {self}')
        return self


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not head:
            return False
        slow = head
        fast = head.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        return False


def testing():
    sol = Solution()
    nums = [3, 2, 0, -4]
    pos = 1
    res = sol.hasCycle(ListNode.create_list_node(nums).update_pos(pos))
    # print(f'res {res}')
    assert (True == res)

    nums = [1, 2]
    pos = 0
    res = sol.hasCycle(ListNode.create_list_node(nums).update_pos(pos))
    assert (True == res)

    nums = [1]
    pos = -1
    res = sol.hasCycle(ListNode.create_list_node(nums).update_pos(pos))
    assert (False == res)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (
        timeit.timeit(testing, number=100)))
