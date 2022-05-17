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

    # try:

    m, n = len(mat), len(mat[0])
    res: List[List[int]] = [[-1001] * c for _ in range(r)]

    # fixme this next line causes some weird bug, during items assignment:
    #  if you do res[0][0]=x then x will be put in all res[*][0]
    #   WORTH CHECKING
    # res: List[List[int]] = [[-1001] * c] * r

    if m * n - r * c: return mat
    for i in range(m * n):
        res [i // c] [i % c] = mat [i // n] [i % n]
    return res

    # except IndexError as e:
    #     print(f'e - {e}')
    #     print(f'i - {i}')
    #     print(f'res - {res}')
    #     print(f'res[i // c][i % c] - res{[i // c]}{[i % c]} = {res[i // c][i % c]}')
    #     print(f'mat[i // n][i % n] - mat{[i // n]}{[i % n]} = {mat[i // n][i % n]}')
    #     return res


def testing():
    result = matrixReshape(mat=[[1, 2], [3, 4]], r=1, c=4)
    # print(f"result: {result}")
    assert ([[1, 2, 3, 4]] == result)

    result = matrixReshape(mat=[[1, 2], [3, 4]], r=2, c=4)
    # print(f"result: {result}")
    assert ([[1, 2], [3, 4]] == result)

    result = matrixReshape(mat=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], r=2, c=6)
    print(f"result: {result}")
    assert ([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]] == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
