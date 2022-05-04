# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
#
# You can return the answer in any order.
from typing import List
import time


def two_sum(nums: List[int], target: int) -> List[int]:
    #   The Official Solution
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i

    #   My Solution
    # note Carina: I think this solution is an equivalent to 'two-pass hash-table'
    #   since the first pass is when python builds himself the hashtable ( for using 'index')
    #   and the second pass is for the actual search.
    #   the solution above (i.e. "official") builds and searches in one pass
    #   and in most cases won't have to build the whole hash-table - it will stop when a proper result is found
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #   start_time = time.time()  # fixme
    #   for i in range(len(nums)):
    #       try:
    #           j = nums.index(target - nums[i], i + 1)
    #       except ValueError:
    #           pass
    #       else:
    #           print("--- %.8f seconds ---" % (time.time() - start_time))  # fixme
    #           return [i, j]


if __name__ == '__main__':
    res_list = two_sum(nums=[2, 7, 11, 15], target=9)
    print(f"\nres_list:{res_list}")
    res_list = two_sum(nums=[3, 2, 4], target=6)
    print(f"\nres_list:{res_list}")
    res_list = two_sum(nums=[3, 3], target=6)
    print(f"\nres_list:{res_list}")
