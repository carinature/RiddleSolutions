#
#   Date - 04.06.2022
#
#
# 867. Transpose Matrix
# Easy
#
# Given a 2D integer array matrix, return the transpose of matrix.
#
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
#
#
#
# Example 1:
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
#
# Example 2:
#
# Input: matrix = [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]
#
#
#
# Constraints:
#
#     m == matrix.length
#     n == matrix[i].length
#     1 <= m, n <= 1000
#     1 <= m * n <= 105
#     -109 <= matrix[i][j] <= 109
#
#


import timeit
from typing import List, Optional


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # # Solution 1 - algoritmic
        res: List[List[int]] = [[None] * len(matrix) for _ in range(len(matrix[0]))]
        for r, row in enumerate(matrix):
            for c, cell in enumerate(row):
                res[c][r] = cell
        return res

        # # Solution 2 - Pythonic
        # return list(map(list,zip(*matrix)))


def testing():
    sol = Solution()

    result = sol.transpose(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # print(f"result: {result}")
    assert ([[1, 4, 7], [2, 5, 8], [3, 6, 9]] == result)

    result = sol.transpose(matrix=[[1, 2, 3], [4, 5, 6]])
    # print(f"result: {result}")
    assert ([[1, 4], [2, 5], [3, 6]] == result)

    # result = sol.transpose(matrix=124356)
    # # print(f"result: {result}")
    # assert (124356 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
