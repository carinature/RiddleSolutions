# Fibonacci in Dynamic Programing
import collections
import timeit
from typing import Dict, List


# Solution 1 - Iterative with Tabulation    O(n)
def fibonacci(n: int) -> int:
    if n < 2:
        return n

    tbl: List[int] = [0] * (n + 1)
    tbl[1] = 1

    for i in range(2, n + 1):
        tbl[i] = tbl[i - 1] + tbl[i - 2]

    return tbl[n]


def testing():
    result = fibonacci(0)
    assert (0 == result)

    result = fibonacci(1)
    assert (1 == result)

    result = fibonacci(2)
    assert (1 == result)

    result = fibonacci(6)
    assert (8 == result)

    result = fibonacci(8)
    assert (21 == result)

    result = fibonacci(30)
    assert (832040 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=10)))
