#
#   Date - 04.05.2022
#
#
# You are given an array of unique integers salary
#   where salary[i] is the salary of the ith employee.
#
# Return the average salary of employees excluding the minimum and maximum salary.
#   Answers within 10^-5 of the actual answer will be accepted.
#
#
#
# Example 1:
#
# Input: salary = [4000,3000,1000,2000]
# Output: 2500.00000
# Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
# Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500
#
# Example 2:
#
# Input: salary = [1000,2000,3000]
# Output: 2000.00000
# Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
# Average salary excluding minimum and maximum salary is (2000) / 1 = 2000
#
#
#
# Constraints:
#
#     3 <= salary.length <= 100
#     1000 <= salary[i] <= 10^6
#     All the integers of salary are unique.
#


import timeit
from typing import List, Optional, Set


def some_function(salary: List[int]) -> float:
    """
    The best way to get ahead is to get starting..?
    """
    sumall, max, min = 0, 0, 1000000
    for s in salary:
        sumall += s
        if max < s: max = s
        if min > s: min = s
    return (sumall-max-min)/(len(salary)-2)


def testing():
    result = some_function(salary=[4000, 3000, 1000, 2000])
    print(f"result: {result}")
    assert (2500.00000 == result)

    result = some_function(salary=[1000, 2000, 3000])
    print(f"result: {result}")
    assert (2000.00000 == result)

    # result = some_function(salary=124356)
    # print(f"result: {result}")
    # assert (124356 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
