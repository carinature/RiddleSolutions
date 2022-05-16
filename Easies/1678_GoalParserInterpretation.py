#
#   Date - 16.05.2022
#
#
# You own a Goal Parser that can interpret a string command.
# The command consists of an alphabet of "G", "()" and/or "(al)" in some order.
# The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al".
# The interpreted strings are then concatenated in the original order.
#
# Given the string command, return the Goal Parser's interpretation of command.
#
#
#
# Example 1:
#
# Input: command = "G()(al)"
# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal".
#
# Example 2:
#
# Input: command = "G()()()()(al)"
# Output: "Gooooal"
#
# Example 3:
#
# Input: command = "(al)G(al)()()G"
# Output: "alGalooG"
#
#
#
# Constraints:
#
#     1 <= command.length <= 100
#     command consists of "G", "()", and/or "(al)" in some order.
#


from math import prod
import timeit
from typing import List, Optional, Set


def interpret(command: str) -> str:
    """
    The best way to get ahead is to get starting..?
    """
    # # Algorithmic Solution
    # i, s = 0, ""
    # while i < len(command):
    #     if "G" == command[i]:
    #         s += "G"
    #     elif ")" == command[i + 1]:
    #         s += "o"
    #         i += 1
    #     else:
    #         s += "al"
    #         i += 3
    #     i += 1
    # return s

    # Pythonic Solution
    return command.replace("()", "o").replace("(al)", "al")


def testing():
    result = interpret(command="G()(al)")
    # print(f"result: {result}")
    assert ("Goal" == result)

    result = interpret(command="G()()()()(al)")
    # print(f"result: {result}")
    assert ("Gooooal" == result)

    result = interpret(command="(al)G(al)()()G")
    # print(f"result: {result}")
    assert ("alGalooG" == result)

    result = interpret(command="G")
    # print(f"result: {result}")
    assert ("G" == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
