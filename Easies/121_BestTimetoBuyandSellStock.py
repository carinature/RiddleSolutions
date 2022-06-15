#
#   Date - 15.06.2022
#
#
# 121. Best Time to Buy and Sell Stock
# Easy
#
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#
#
#
# Example 1:
#
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
#
# Example 2:
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
#
#
#
# Constraints:
#
#     1 <= prices.length <= 105
#     0 <= prices[i] <= 104
#


from math import prod
import timeit
from typing import List, Optional, Set, Dict
# from collections import defaultdict
import collections


class Solution:
    def maxProfit(self, prices: List[int]) -> Optional[int]:
        """
        The best way to get ahead is to get starting..?
        """

        buy = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] <= buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy

        return profit


def testing():
    sol = Solution()

    result = sol.maxProfit(prices=[7, 1, 5, 3, 6, 4])
    # print(f"result: {result}")
    assert (5 == result)

    result = sol.maxProfit(prices=[7, 6, 4, 3, 1])
    print(f"result: {result}")
    assert (0 == result)

    result = sol.maxProfit(prices=[7])
    print(f"result: {result}")
    assert (0 == result)

    result = sol.maxProfit(prices=[1, 2])
    print(f"result: {result}")
    assert (1 == result)

    # result = sol.maxProfit(prices=124356)
    # # print(f"result: {result}")
    # assert (124356 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
