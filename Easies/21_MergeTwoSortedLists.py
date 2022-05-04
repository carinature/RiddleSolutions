# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list.
# The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.
# Constraints:
#
#     The number of nodes in both lists is in the range [0, 50].
#     -100 <= Node.val <= 100
#     Both list1 and list2 are sorted in non-decreasing order.


from typing import List, Optional
import time


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # ml = []
    # i = 0
    # for li in list1.:
    #     while i < len(list2) and li >= list2[i]:
    #         ml.append(list2[i])
    #         i += 1
    #     ml.append(li)
    # ml += list2[i:]
    # return ml

    # ml = []
    # i1, i2 = 0, 0
    # while i1 < len(list1) and i2 < len(list2):
    #     if list1[i1] <= list2[i2]:
    #         ml.append(list1[i1])
    #         i1 += 1
    #     else:
    #         ml.append(list2[i2])
    #         i2 += 1
    # # Only one of the following will happen
    # ml += list1[i1:]
    # ml += list2[i2:]
    # return ml

    ml = ListNode()
    res = ml
    while list1:
        while list2 and list2.val <= list1.val:
            ml.next = list2
            ml = ml.next
            list2 = list2.next
        # if not list2:
        #     ml.next = list1
        #     return res.next
        ml.next = list1
        ml = ml.next
        list1 = list1.next
    ml.next = list2

    return res.next


# a BEAUTIFUL recursive solution from one of the users of leetCode:
class Solution:
    def mergeTwoLists(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b


if __name__ == '__main__':
    start_time = time.time()  # fixme
    result = mergeTwoLists(list1=[1, 2, 4], list2=[1, 3, 4])
    print(f"\nresult:{result}")
    assert ([1, 1, 2, 3, 4, 4] == result)
    result = mergeTwoLists(list1=[], list2=[])
    print(f"\nresult:{result}")
    assert ([] == result)
    result = mergeTwoLists(list1=[], list2=[0])
    print(f"\nresult:{result}")
    assert ([0] == result)
    result = mergeTwoLists(list1=[1], list2=[])
    print(f"\nresult:{result}")
    assert ([1] == result)
    result = mergeTwoLists(list1=[1], list2=[1])
    print(f"\nresult:{result}")
    assert ([1, 1] == result)
    # result = mergeTwoLists(list1=[], list2=[])
    # print(f"\nresult:{result}")
    # assert ([] == result)
    # result = mergeTwoLists(list1=[], list2=[])
    # print(f"\nresult:{result}")
    # assert ([] == result)
    print("--- %.8f seconds ---" % (time.time() - start_time))  # fixme
