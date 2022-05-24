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

    def __repr__(self):
        tail: ListNode = self
        res: List[str] = []
        while tail:
            res.append(str(tail.val))
            tail = tail.next
        return ' --> '.join(res)


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # # # Solution 1
        # node = head
        # while head.next:
        #     head = head.next
        #     node = node.next
        #     if head.next:
        #         head = head.next
        # return node

        # # # # Solution 2
        # slow = fast = head
        fast = head
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
        return head

        # # # # Solution 3
        # node = head
        # try:
        #     while head.next:
        #         head = head.next
        #         node = node.next
        #         head = head.next
        # finally:
        #     return node

        # print(head)


def testing():
    sol = Solution()

    head = [1, 2, 3, 4, 5]
    head = sol.middleNode(ListNode.create_list_node(head))
    assert ([3, 4, 5] == head)

    head = [1, 2, 3, 4, 5, 6]
    head = sol.middleNode(ListNode.create_list_node(head))
    assert ([4, 5, 6] == head)

    # head = [0, -1]
    # sol.middleNode(ListNode.create_list_node(head))
    # assert ([-1, 0] == head)
    #
    # head = [0, 0]
    # sol.middleNode(ListNode.create_list_node(head))
    # assert ([0, 0] == head)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (
        timeit.timeit(testing, number=100)))
