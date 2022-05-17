#
#   Date - 15.05.2022
#
#
# In MATLAB, there is a handy function called reshape which can
#   reshape an m x n matrix into a new one with a different size r x c keeping its original data.
#
# You are given an m x n matrix mat and two integers r and c representing
#   the number of rows and the number of columns of the wanted reshaped matrix.
#
# The reshaped matrix should be filled with all the elements of the original matrix
#   in the same row-traversing order as they were.
#
# If the reshape operation with given parameters is possible and legal,
#   output the new reshaped matrix; Otherwise, output the original matrix.
#
#
#
# Example 1:
#
# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]
#
# Example 2:
#
# Input: mat = [[1,2],[3,4]], r = 2, c = 4
# Output: [[1,2],[3,4]]
#
#
#
# Constraints:
#
#     m == mat.length
#     n == mat[i].length
#     1 <= m, n <= 100
#     -1000 <= mat[i][j] <= 1000
#     1 <= r, c <= 300
#


from math import prod
import timeit
from typing import List, Optional, Set


def matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    """
    The best way to get ahead is to get starting..?
    """

    m, n = len(mat), len(mat[0])
    print(f'm {m}, n {n}')
    # maybe not necessary :
    if m * n - r * c:
        return mat


    # # newmat = [mat[i][j] for i in range(m) for j in range(n)]
    # newmat: List[List[int]] = [[-1001] * n] * m
    # print(f'newmat - {newmat}')
    # for i in range(m):
    #     for j in range(n):
    #         # row, col = divmod(i * n + j, c)
    #         newmat[row][col] = mat[i][j]
    # return newmat


def testing():
    result = matrixReshape(mat=[[1, 2], [3, 4]], r=1, c=4)
    # print(f"result: {result}")
    assert ([[1, 2, 3, 4]] == result)

    result = matrixReshape(mat=[[1, 2], [3, 4]], r=2, c=4)
    # print(f"result: {result}")
    assert ([[1, 2], [3, 4]] == result)

    result = matrixReshape(mat=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], r=2, c=6)
    # print(f"result: {result}")
    assert ([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]] == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
