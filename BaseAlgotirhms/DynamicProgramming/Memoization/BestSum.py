# BestSum in Dynamic Programing
# return the "best" (shortest) list of elements in the arr whose sum equals target
#

import timeit
from typing import Dict, List, Set, Optional


# # # Solution 1 - Recursive (Naive) - O(2^(n+m) )
def BestSum(target_sum: int, arr: List[int]) -> Optional[List[int]]:
    if target_sum == 0: return []
    if target_sum < 0: return None
    res: List[int] = None
    for num in arr:
        sol = BestSum(target_sum - num, arr)
        if sol is not None:
            if res is None or len(res) - 1 > len(sol):
                res = sol + [num]
    return res


# # # Solution 2 - Recursive with Memoization - O(n)
def BestSum(target_sum: int, arr: List[int], memo=None) -> Optional[List[int]]:
    if memo is None: memo: Dict[int, List[int]] = dict()

    if target_sum in memo: return memo[target_sum]
    if target_sum == 0: return []
    if target_sum < 0: return None

    res: List[int] = None

    for num in arr:
        sol = BestSum(target_sum - num, arr, memo)
        if sol is not None:
            if res is None or len(res) - 1 > len(sol):
                res = sol + [num]
    memo[target_sum] = res
    return res


def testing():
    result = BestSum(7, [5, 3, 4])
    # print(f'result: {result}')
    assert ([4, 3] == result)

    result = BestSum(0, [5, 3, 4])
    assert ([] == result)

    result = BestSum(7, [5, 7])
    assert ([7] == result)

    result = BestSum(7, [5, 3, 4, 7])
    assert ([7] == result)  # or [4, 3] == result)

    result = BestSum(7, [2, 4])
    assert (None == result)

    result = BestSum(8, [2, 3, 5])
    assert ([5, 3] == result)

    result = BestSum(300, [7, 14])
    assert (None == result)


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
