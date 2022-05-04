# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.
#

from typing import List
import time


def sorted_squares(nums: List[int]) -> List[int]:
    res = []
    n = len(nums)
    left, right = 0, n - 1
    for i in range(n):
        if abs(nums[left]) > abs(nums[right]):
            res.append(nums[left] ** 2)
            left += 1
        else:
            res.append( nums[right] ** 2)
            right -= 1
    res.reverse()
    return res
    # i = len(nums) - 1
    # while nums[i] > 0 and i > 0:
    #     pos.append(nums[i] ** 2)  # pos in descending order for now
    #     i -= 1
    # while i >= 0:
    #     neg.append(nums[i] ** 2)
    #     i -= 1
    # i, j = len(pos) - 1, 0
    # while i >= 0 and j < len(neg):
    #     nj, pi = neg[j], pos[i]
    #     if nj < pi:
    #         res.append(nj)
    #         j += 1
    #     else:
    #         res.append(pi)
    #         i -= 1
    # # while i >= 0:
    # #     res.append(pos[i])
    # #     i -= 1
    # res += pos[i + 1:0:-1]
    # res += neg[j:]
    # while j < len(neg):
    #     res.append(neg[j])
    #     j += 1

    return res

    # for i in range (len(nums), 0, -1):


if __name__ == '__main__':
    start_time = time.time()  # fixme
    result = sorted_squares(nums=[-4, -1, 0, 3, 10])
    print(f"\nresult:{result}")
    assert ([0, 1, 9, 16, 100] == result)
    result = sorted_squares(nums=[-7, -3, 2, 3, 11])
    print(f"\nresult:{result}")
    assert ([4, 9, 9, 49, 121] == result)
    result = sorted_squares(nums=[1])
    print(f"\nresult:{result}")
    assert ([1] == result)
    result = sorted_squares(nums=[-1])
    print(f"\nresult:{result}")
    assert ([1] == result)
    result = sorted_squares(nums=[-5, -3, -2, -1])
    print(f"\nresult:{result}")
    assert ([1, 4, 9, 25] == result)
    print("--- %.8f seconds ---" % (time.time() - start_time))  # fixme
