#
#   Date - 15.05.2022
#
#
# You are given an m x n integer grid accounts where
#   accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank.
#   Return the wealth that the richest customer has.
#
# A customer's wealth is the amount of money they have in all their bank accounts.
# The richest customer is the customer that has the maximum wealth.
#
#
#
# Example 1:
#
# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each, so return 6.
#
# Example 2:
#
# Input: accounts = [[1,5],[7,3],[3,5]]
# Output: 10
# Explanation:
# 1st customer has wealth = 6
# 2nd customer has wealth = 10
# 3rd customer has wealth = 8
# The 2nd customer is the richest with a wealth of 10.
#
# Example 3:
#
# Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
# Output: 17
#
#
#
# Constraints:
#
#     m == accounts.length
#     n == accounts[i].length
#     1 <= m, n <= 50
#     1 <= accounts[i][j] <= 100
#


from math import prod
import timeit
from typing import List, Optional, Set


def maximumWealth(accounts: List[List[int]]) -> int:
    """
    The best way to get ahead is to get starting..?
    """
    # #     Pythonic Solution
    return max(map(sum, accounts))

    # #     Algorithmic Solution
    # ma = 0
    # for a in accounts:
    #     ma = max(ma, sum(a))
    #     # if s > ma:
    #     #     ma = s
    # return ma


def testing():
    result = maximumWealth(accounts=[[1, 2, 3], [3, 2, 1]])
    # print(f"result: {result}")
    assert (6 == result)

    result = maximumWealth(accounts=[[1, 5], [7, 3], [3, 5]])
    # print(f"result: {result}")
    assert (10 == result)

    result = maximumWealth(accounts=[[2, 8, 7], [7, 1, 3], [1, 9, 5]])
    # print(f"result: {result}")
    assert (17 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
