#
#   Date - 26.05.2022
#
#
# 2280. Minimum Lines to Represent a Line Chart
# Medium
#
# You are given a 2D integer array stockPrices
# where stockPrices[i] = [dayi, pricei] indicates the price of the stock on day dayi is pricei.
# A line chart is created from the array by plotting the points on an XY plane
# with the X-axis representing the day
# and the Y-axis representing the price and connecting adjacent points.
# One such example is shown below:
#
# Return the minimum number of lines needed to represent the line chart.
#
#
#
# Example 1:
#
# Input: stockPrices = [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]
# Output: 3
# Explanation:
# The diagram above represents the input, with the X-axis representing the day and Y-axis representing the price.
# The following 3 lines can be drawn to represent the line chart:
# - Line 1 (in red) from (1,7) to (4,4) passing through (1,7), (2,6), (3,5), and (4,4).
# - Line 2 (in blue) from (4,4) to (5,4).
# - Line 3 (in green) from (5,4) to (8,1) passing through (5,4), (6,3), (7,2), and (8,1).
# It can be shown that it is not possible to represent the line chart using less than 3 lines.
#
# Example 2:
#
# Input: stockPrices = [[3,4],[1,2],[7,8],[2,3]]
# Output: 1
# Explanation:
# As shown in the diagram above, the line chart can be represented with a single line.
#
#
#
# Constraints:
#
#     1 <= stockPrices.length <= 105
#     stockPrices[i].length == 2
#     1 <= dayi, pricei <= 109
#     All dayi are distinct.
#

from math import prod
import timeit
from typing import List, Optional, Set, Dict
# from collections import defaultdict
import collections


class Solution:

    def minimumLines(self, stockPrices: List[List[int]]) -> Optional[int]:
        """
        The best way to get ahead is to get starting..?
        """
        if len(stockPrices) < 2: return 0
        stockPrices.sort()
        res = [
            (stockPrices[i + 1][1] - stockPrices[i][1]) * (stockPrices[i + 2][0] - stockPrices[i + 1][0])
            !=
            (stockPrices[i + 2][1] - stockPrices[i + 1][1]) * (stockPrices[i + 1][0] - stockPrices[i][0])
            for i in range(len(stockPrices) - 2)]
        return res.count(True) + 1


def testing():
    sol = Solution()

    result = sol.minimumLines(stockPrices=[[1, 7], [2, 6], [3, 5], [4, 4], [5, 4], [6, 3], [7, 2], [8, 1]])
    # print(f"result: {result}")
    assert (3 == result)

    result = sol.minimumLines(stockPrices=[[3, 4], [1, 2], [7, 8], [2, 3]])
    # print(f"result: {result}")
    assert (1 == result)

    result = sol.minimumLines(
        stockPrices=[[36, 9], [17, 93], [34, 4], [30, 11], [11, 41], [53, 36], [5, 92], [81, 92], [28, 36], [3, 45],
                     [72, 33], [64, 1], [4, 70], [16, 73], [99, 20], [49, 33], [47, 74], [83, 91]])
    # print(f"result: {result}")
    assert (17 == result)

    result = sol.minimumLines(
        stockPrices=[[72, 98], [62, 27], [32, 7], [71, 4], [25, 19], [91, 30], [52, 73], [10, 9], [99, 71], [47, 22],
                     [19, 30], [80, 63], [18, 15], [48, 17], [77, 16], [46, 27], [66, 87], [55, 84], [65, 38], [30, 9],
                     [50, 42], [100, 60], [75, 73], [98, 53], [22, 80], [41, 61], [37, 47], [95, 8], [51, 81], [78, 79],
                     [57, 95]])
    # print(f"result: {result}")
    assert (29 == result)

    result = sol.minimumLines(
        stockPrices=[[1, 1], [500000000, 499999999], [1000000000, 999999998]]
    )
    # print(f"result: {result}")
    assert (2 == result)

    result = sol.minimumLines(
        stockPrices=[[1, 1]]
    )
    # print(f"result: {result}")
    assert (0 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
