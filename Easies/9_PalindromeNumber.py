# Given an integer x, return true if x is palindrome integer.
#
# An integer is a palindrome when it reads the same backward as forward.
#
#     For example, 121 is a palindrome while 123 is not.
import math
from typing import List
import time


def is_palindrome(x: int) -> bool:
    if not x:
        return True
    if x != abs(x) or x % 10 == 0:
        return False
    dl = int(math.log10(abs(x))) + 1  # todo remember this trick - using log 10 to find the number of digits
    new = 0
    for i in range(dl // 2):
        new = new * 10 + x % 10
        x = x // 10
    x = x // (10 ** (dl - 2 * (dl // 2)))
    return x == new

    #   Solution 1
    # left = x // 10 ** (dl - (dl // 2))
    # right = x % (10 ** (dl // 2))
    # new = 0
    # for i in range(dl // 2):
    #     new = new * 10 + left % 10
    #     left = left // 10
    # print(f'right - {right}')
    # print(f'left - {left}')

    #   Solution 2
    # if not x:
    #     return True
    # if x != abs(x):
    #     return False
    # dl = int(math.log10(abs(x))) + 1  # todo remember this trick - using log 10 to find the number of digits
    # for i in range(1, dl // 2 + 1):
    #     if ((x % (10 ** i)) // (10 ** (i - 1))) != ((x // (10 ** (dl - i))) % 10):
    #         return False
    # return True

    # s = str(x)
    # lx = len(s)
    # dl = len(s) // 2
    # for i in range(dl):
    #     if s[i] != s[lx - i - 1]:
    #         return False
    # return True


if __name__ == '__main__':
    start_time = time.time()  # fixme
    result = is_palindrome(x=121)
    print(f"\nresult:{result}")
    result = is_palindrome(x=-121)
    print(f"\nresult:{result}")
    result = is_palindrome(x=10)
    print(f"\nresult:{result}")
    result = is_palindrome(x=-1)
    print(f"\nresult:{result}")
    result = is_palindrome(x=0)
    print(f"\nresult:{result}")
    result = is_palindrome(x=1231)
    print(f"\nresult:{result}")
    result = is_palindrome(x=12341)
    print(f"\nresult:{result}")
    result = is_palindrome(x=12345678)
    print(f"\nresult:{result}")
    result = is_palindrome(x=123456789)
    print(f"\nresult:{result}")
    result = is_palindrome(x=1001)
    print(f"\nresult:{result}")
    print("--- %.8f seconds ---" % (time.time() - start_time))  # fixme
