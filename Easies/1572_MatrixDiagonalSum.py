#
#   Date - 15.05.2022
#
#
# Given a square matrix mat, return the sum of the matrix diagonals.
#
# Only include the sum of all the elements on the primary diagonal and all the
#   elements on the secondary diagonal that are not part of the primary diagonal.
#
#
#
# Example 1:
#
# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.
#
# Example 2:
#
# Input: mat = [[1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1]]
# Output: 8
#
# Example 3:
#
# Input: mat = [[5]]
# Output: 5
#
#
#
# Constraints:
#
#     n == mat.length == mat[i].length
#     1 <= n <= 100
#     1 <= mat[i][j] <= 100
#


from math import prod
import timeit
from typing import List, Optional, Set


def diagonalSum(mat: List[List[int]]) -> int:
    """
    The best way to get ahead is to get starting..?
    """
    # # # #     Solution #1
    s, l = 0, len(mat)
    for i in range(l):
        s += mat[i][i] + mat[i][l - 1 - i]
    return s - mat[l // 2][l // 2] if l % 2 else s

    # # # #     Solution #2
    # l = len(mat)
    # s = sum([mat[i][i] +
    #          mat[i][l - 1 - i] +
    #          mat[l - 1 - i][i] +
    #          mat[l - 1 - i][l - 1 - i]
    #          for i in range(l // 2)])
    # return s + mat[l // 2][l // 2] if l % 2 else s


def testing():
    result = diagonalSum(mat=
                         [[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]])
    # print(f"result: {result}")
    assert (25 == result)

    result = diagonalSum(mat=
                         [[1, 1, 1, 1],
                          [1, 1, 1, 1],
                          [1, 1, 1, 1],
                          [1, 1, 1, 1]])
    # print(f"result: {result}")
    assert (8 == result)

    result = diagonalSum(mat=
                         [[5]])
    # print(f"result: {result}")
    assert (5 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
