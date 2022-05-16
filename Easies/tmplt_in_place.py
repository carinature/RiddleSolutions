#
#   Date - 01.02.2022
#
#
# Given an integer array nums, move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
#
#
#       Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
#       Example 2:
# Input: nums = [0]
# Output: [0]
#
#
#       Constraints:
#     1 <= nums.length <= 104
#     -231 <= nums[i] <= 231 - 1

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


def some_function(nums: 'ListNode') -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    print(f'nums: {nums}')


def testing():
    nums = [0, 1, 0, 3, 12]
    some_function(ListNode.create_list_node(nums))
    assert ([1, 3, 12, 0, 0] == nums)

    nums = [0]
    some_function(ListNode.create_list_node(nums))
    assert ([0] == nums)

    nums = [0, -1]
    some_function(ListNode.create_list_node(nums))
    assert ([-1, 0] == nums)

    nums = [0, 0]
    some_function(ListNode.create_list_node(nums))
    assert ([0, 0] == nums)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (
        timeit.timeit(testing, number=100)))
