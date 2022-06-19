#
#   Date - 19.06.2022
#
#
# 74. Search a 2D Matrix
# Medium
#
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
# This matrix has the following properties:
#
#     Integers in each row are sorted from left to right.
#     The first integer of each row is greater than the last integer of the previous row.
#
#
#
# Example 1:
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#
# Example 2:
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#
#
#
# Constraints:
#
#     m == matrix.length
#     n == matrix[i].length
#     1 <= m, n <= 100
#     -104 <= matrix[i][j], target <= 104
#


from math import prod
import timeit
from typing import List, Optional, Set, Dict
# from collections import defaultdict
import collections


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        The best way to get ahead is to get starting..?
        """
        print(f'nums: {matrix}')
        top, bottom = 0, len(matrix) - 1
        line = (bottom + top) // 2

        while top <= bottom:
            line = (bottom + top) // 2
            if target < matrix[line][0]:
                bottom = line - 1
            elif target > matrix[line][-1]:
                top = line + 1
            else:  # if matrix[line][0]<target<matrix[line][-1]:
                break
        else:
            print('kakakakaka')

        if top > bottom:  # or is it top > bottom
            return False

        left, right = 0, len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2
            if target < matrix[line][mid]:
                right = mid - 1
            elif target > matrix[line][mid]:
                left = mid + 1
            else:
                return True

        return False


def testing():
    sol = Solution()

    result = sol.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3)
    # print(f"result: {result}")
    assert (True == result)

    result = sol.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13)
    # print(f"result: {result}")
    assert (False == result)

    result = sol.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=11)
    # print(f"result: {result}")
    assert (True == result)

    result = sol.searchMatrix(matrix=[[1, 3, 5, 7]], target=1)
    # print(f"result: {result}")
    assert (True == result)
    result = sol.searchMatrix(matrix=[[1, 3, 5, 7]], target=3)
    # print(f"result: {result}")
    assert (True == result)
    result = sol.searchMatrix(matrix=[[1, 3, 5, 7]], target=5)
    # print(f"result: {result}")
    assert (True == result)
    result = sol.searchMatrix(matrix=[[1, 3, 5, 7]], target=7)
    # print(f"result: {result}")
    assert (True == result)
    result = sol.searchMatrix(matrix=[[1, 3, 5, 7]], target=17)
    # print(f"result: {result}")
    assert (False == result)

    result = sol.searchMatrix(matrix=[[1], [3], [5], [7]], target=1)
    # print(f"result: {result}")
    assert (True == result)
    result = sol.searchMatrix(matrix=[[1], [3], [5], [7]], target=3)
    # print(f"result: {result}")
    assert (True == result)
    result = sol.searchMatrix(matrix=[[1], [3], [5], [7]], target=5)
    # print(f"result: {result}")
    assert (True == result)
    result = sol.searchMatrix(matrix=[[1], [3], [5], [7]], target=7)
    # print(f"result: {result}")
    assert (True == result)
    result = sol.searchMatrix(matrix=[[1], [3], [5], [7]], target=11)
    # print(f"result: {result}")
    assert (False == result)

    # result = sol.searchMatrix(matrix=124356)
    # # print(f"result: {result}")
    # assert (124356 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=10)))
