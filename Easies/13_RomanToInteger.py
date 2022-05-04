# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# For example, 2 is written as II in Roman numeral, just two one's added together.
# 12 is written as XII, which is simply X + II.
# The number 27 is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII.
# Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:
#
#     I can be placed before V (5) and X (10) to make 4 and 9.
#     X can be placed before L (50) and C (100) to make 40 and 90.
#     C can be placed before D (500) and M (1000) to make 400 and 900.
#
# Given a roman numeral, convert it to an integer.
#
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].
import timeit
from typing import List
import time

specialDict = {"CM": 900, "CD": 400, "XC": 90, "XL": 40, "IX": 9, "IV": 4}


def roman_to_int(s: str) -> int:
    # "s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M')."
    roman_dct = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = roman_dct[s[-1]]
    for i in range(len(s) - 1):
        if roman_dct[s[i]] >= roman_dct[s[i+1]]:
            num += roman_dct[s[i]]
        else:
            num -= roman_dct[s[i]]
    return num


def testing():
    # start_time = time.time()  # fixme

    result = roman_to_int(s="III")
    # print(f"result: {result}")
    assert (3 == result)

    result = roman_to_int(s="LVIII")
    # print(f"result: {result}")
    assert (58 == result)

    result = roman_to_int(s="MCMXCIV")
    print(f"result: {result}")
    assert (1994 == result)

    # print("--- %.8f seconds ---" % (time.time() - start_time))  # fixme


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (timeit.timeit(testing, number=10000)))
