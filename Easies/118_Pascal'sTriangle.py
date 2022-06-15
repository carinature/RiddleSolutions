#
#   Date - 15.06.2022
#
#
# 118. Pascal's Triangle
# Easy
#
# Given an integer numRows, return the first numRows of Pascal's triangle.
# 
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
#
#
# Example 1:
#
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#
# Example 2:
#
# Input: numRows = 1
# Output: [[1]]
#
#
#
# Constraints:
#
#     1 <= numRows <= 30
#


from math import prod
import timeit
from typing import List, Optional, Set, Dict
# from collections import defaultdict
import collections


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        The best way to get ahead is to get starting..?
        """
        print(f'numRows: {numRows}')
        res = [[1] * j for j in range(1, 1 + numRows)]
        print(f'res: {res}')

        for r in range(2, len(res)):
            for c in range(1, len(res[r]) - 1):
                res[r][c] = res[r - 1][c - 1] + res[r - 1][c]
                print(f'res: {res}')
        #
        # # for c in range(numRows):
        # #     res[c].append([j for j in range(c)])

        return res


def testing():
    sol = Solution()

    result = sol.generate(numRows=5)
    # print(f"result: {result}")
    assert ([[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]] == result)

    result = sol.generate(numRows=1)
    # print(f"result: {result}")
    assert ([[1]] == result)

    result = sol.generate(numRows=2)
    # print(f"result: {result}")
    assert ([[1], [1, 1]] == result)

    # result = sol generate(numRows=124356)
    # # print(f"result: {result}")
    # assert (124356 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=10)))
