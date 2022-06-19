#
#   Date - 16.05.2022
#
#
# 206. Reverse Linked List
# Easy
#
# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
#
#
# Example 1:
#
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#
# Example 2:
#
# Input: head = [1,2]
# Output: [2,1]
#
# Example 3:
#
# Input: head = []
# Output: []
#
#
#
# Constraints:
#
#     The number of nodes in the list is the range [0, 5000].
#     -5000 <= Node.val <= 5000
#
#
#
# Follow up: A linked list can be reversed either iteratively or recursively.
# Could you implement both?
#

import timeit
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

    def __repr__(self):
        tail: ListNode = self
        res: List[str] = []
        max_repe_len = 30  # in case of loops in linked list ..
        while tail and max_repe_len:
            res.append(str(tail.val))
            tail = tail.next
            max_repe_len -= 1
        return ' --> '.join(res)

    def create_list_node(nums: List[int]) -> 'ListNode':
        if not nums:
            # return ListNode()
            return None
        tail = ListNode(nums[-1])
        for num in reversed(nums[:-1]):
            new_tail = ListNode(num, tail)
            tail = new_tail
        return tail


def to_list(ln: Optional[ListNode]) -> List[int]:
    l = []
    while ln:
        l.append(ln.val)
        ln = ln.next
    return l


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # # Solution 1 - Iterative
        res = None
        while head:
            res = ListNode(head.val, res)
            head = head.next
        return res

        # # # Solution 2 - Recursive
        pass


def testing():
    sol = Solution()

    # nums = [1, 2, 3, 4, 5]
    # res = sol.reverseList(ListNode.create_list_node(nums))
    # # print(f'res {res}')
    # assert ([5, 4, 3, 2, 1] == to_list(res))
    #
    # nums = [0]
    # res = sol.reverseList(ListNode.create_list_node(nums))
    # assert ([0] == to_list(res))
    #
    # nums = [1, 2]
    # res = sol.reverseList(ListNode.create_list_node(nums))
    # assert ([2, 1] == to_list(res))

    nums = []
    res = sol.reverseList(ListNode.create_list_node(nums))
    assert ([] == to_list(res))


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (
        timeit.timeit(testing, number=100)))
