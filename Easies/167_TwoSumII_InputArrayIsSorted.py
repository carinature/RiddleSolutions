#
#   Date - 02.02.2022
#
#
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
#
# Return the indices of the two numbers,
# index1 and index2, added by one as an integer array [index1, index2] of length 2.
#
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
#
#
#
# Example 1:
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
#
# Example 2:
#
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
#
# Example 3:
#
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
#
#
#
# Constraints:
#
#     2 <= numbers.length <= 3 * 104
#     -1000 <= numbers[i] <= 1000
#     numbers is sorted in non-decreasing order.
#     -1000 <= target <= 1000
#     The tests are generated such that there is exactly one solution.
import timeit
from typing import List, Optional
import time


def twoSum(numbers: List[int], target: int) -> List[int]:
    # for i, num in enumerate(numbers):
    #     for j, num2 in enumerate(numbers[i + 1:]):
    #         if target == num + num2:
    #             return [i + 1, j + i + 2]  # meaning j + (i + 1) + 1
    #         elif target < num + num2:
    #             break

    i, j = 0, len(numbers) - 1
    while True:  # while i < j:
        if target > numbers[i] + numbers[j]:
            i += 1
        elif target < numbers[i] + numbers[j]:
            j -= 1
        else:
            return [i + 1, j + 1]

    #     Another interesting solution form the site, by a lettCode user:
    # dictionary
    # dic = {}
    # for i, num in enumerate(numbers):
    #     if target - num in dic:
    #         return [dic[target - num] + 1, i + 1]
    #     dic[num] = i


def testing():
    result = twoSum(numbers=[2, 7, 11, 15], target=9)
    # print(f"result: {result}")
    assert ([1, 2] == result)

    result = twoSum(numbers=[2, 3, 4], target=6)
    # print(f"result: {result}")
    assert ([1, 3] == result)

    result = twoSum(numbers=[-1, 0], target=-1)
    # print(f"result: {result}")
    assert ([1, 2] == result)

    result = twoSum(numbers=[2, 7, 11, 15, 16], target=9)
    # print(f"result: {result}")
    assert ([1, 2] == result)

    result = twoSum(numbers=[2, 3, 7, 11, 15], target=9)
    # print(f"result: {result}")
    assert ([1, 3] == result)

    result = twoSum(numbers=[1, 2, 3, 7, 9, 11, 15], target=9)
    # print(f"result: {result}")
    assert ([2, 4] == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (timeit.timeit(testing, number=100000)))
