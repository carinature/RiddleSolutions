#
#   Date - 15.05.2022
#
#
# You are given an array coordinates,
# coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
# Check if these points make a straight line in the XY plane.
#
#
#
#
#
# Example 1:
#
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true
#
# Example 2:
#
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false
#
#
#
# Constraints:
#
#     2 <= coordinates.length <= 1000
#     coordinates[i].length == 2
#     -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
#     coordinates contains no duplicate point.
#


from math import prod
import timeit
from typing import List, Optional, Set


def checkStraightLine(coordinates: List[List[int]]) -> bool:
    """
    The best way to get ahead is to get starting..?
    """
    x, y = coordinates[0][0], coordinates[0][1]
    # if not sum(map(lambda c: x - c[0], coordinates)):  # [1:])):
    #     return True
    if not (x - coordinates[1][0]):
        for xx, __ in coordinates[2:]:
            if x - xx:
                return False
        return True
    m = (y - coordinates[1][1]) / (x - coordinates[1][0])
    for xx, yy in coordinates[2:]:
        if m * (x - xx) - y + yy:
            return False
    return True


def testing():
    result = checkStraightLine(
        coordinates=[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
    # print(f"result: {result}")
    assert (True == result)

    result = checkStraightLine(
        coordinates=[[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]])
    # print(f"result: {result}")
    assert (False == result)

    result = checkStraightLine(
        coordinates=[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [1, 8]])
    # print(f"result: {result}")
    assert (False == result)

    result = checkStraightLine(
        coordinates=[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [8, 2]])
    # print(f"result: {result}")
    assert (False == result)

    result = checkStraightLine(
        coordinates=[[0, 0], [0, 1], [0, -1]])
    # print(f"result: {result}")
    assert (True == result)

    result = checkStraightLine(
        coordinates=[[0, 0], [1, 0], [-1, 0]])
    # print(f"result: {result}")
    assert (True == result)

    result = checkStraightLine(
        coordinates=[[0, 0], [0, 5], [5, 5], [5, 0]])
    # print(f"result: {result}")
    assert (False == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
