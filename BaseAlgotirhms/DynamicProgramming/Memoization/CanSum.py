# CanSum in Dynamic Programing
# return True if target_sum can be constructed from any combination of array numbers (all positive)
#

import timeit
from typing import Dict, List, Set


# # # Solution 1 - Recursive (Naive) - O(2^(n+m) )
def CanSum(target_sum: int, arr: List[int]) -> bool:
    # Tnai Azira
    if 0 == target_sum:
        return True
    if 0 > target_sum:
        return False
    for num in arr:
        if CanSum(target_sum - num, arr):
            return True
    return False


# # # Solution 2 - Recursive with Memoization - O(n)
def CanSum(target_sum: int, arr: List[int], memo=None) -> bool:
    if memo is None:
        memo: Set[int] = set()  # Dict[int, bool] = dict()

    if target_sum in memo: return False
    if 0 == target_sum: return True
    if 0 > target_sum: return False

    for num in arr:
        new_target = target_sum - num
        if CanSum(new_target, arr, memo):
            return True

    memo.add(target_sum)
    return False


def testing():
    result = CanSum(7, [5, 3, 4, 7])
    assert (True == result)

    result = CanSum(7, [5, 3, 4])
    assert (True == result)

    result = CanSum(7, [5, 7])
    assert (True == result)

    result = CanSum(7, [2, 4])
    assert (False == result)

    result = CanSum(8, [2, 3, 5])
    assert (True == result)

    result = CanSum(300, [7, 14])
    assert (False == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=10)))

#
#
#
#
#
#
# assuming:
# n = len(arr)
# m = target_sum
# # Time complexity of the naive recursive alg would be an O(n^m):
# the height of the tree is the number of time we can subtract a number from the array of target_sum.
# so worst case scenario we subtract 1 from target_sum each step
# (arr items are positive integers)
# and we can do that at most m time.
# so the height of the tree is m.
# the width of tree:
# te number of possible child nodes is at most n,
# because every function call we iterate over every number in the arr
# and we call the function for each of the nums.
# so in each "level" of the tree we add n child nodes for each of the child nodes
# (essentially we are multiplying the number of nodes by n each level)
# which means we have O(n^m) nodes.
# meaning time complexity is O(n^m)
# space complexity O(m) - the maximum height of the tree.
#
#
#
# but for the memoized solution
# time complexity is O(m*n)
# space complexity stays the same
#
#
#
#
#
#
