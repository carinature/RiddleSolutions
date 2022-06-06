# Fibonacci in Dynamic Programing
import timeit
from typing import Dict


# Solution 1 - Recursive (Naive) - O(2^n)
def fibonacci(n: int) -> int:
    if n <= 1:  # todo maybe safer   n==0 or n=1    ?
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Solution 2 - Recursive with Memoization - O(n)

# def fibonacci(n: int, memo=None) -> int:
#     if memo is None:
#         memo = {}

def fibonacci(n: int, memo: Dict[int, int] = dict()) -> int:
    if n in memo:
        return memo[n]
    if n <= 1:  # todo maybe safer   n==0 or n=1    ?
        memo[n] = n
        # return memo[n]
        return n
    # memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    memo[n] = fibonacci(n - 2) + fibonacci(n - 1)
    return memo[n]


def testing():
    result = fibonacci(30)
    assert (832040 == result)

    result = fibonacci(8)
    assert (21 == result)

    result = fibonacci(6)
    assert (8 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=1000000)))

#
#
#
#
#
#
#
# Time complexity of the naive recursive alg would be an O(2^n):
# if we imagine all the call to the function as a tree
# (let's say we call the fib function with 7 as the argument)
# then at the top of the tree we will have n=7
# at the level below n-1=6 and n-2=5
# and below each one 2 more nodes and the same all the way to the leave nodes
# as a result we can visualise the calls as binary tree,
# with depth/hight of n and therefore number of call is as the number of nodes - 2^n
#
# Space complexity - should count the stack of recursion calls, as well as space allocated
# but note that not all call are made at once.
# in fact, we only call fib(n-2) after we "closed" (poped the stack frame) of the last func call.
# so we only allocate frames on the stack as the number of concurrent calls, which is the depth of the tree.
# and so the space complexity is actually only O(n).
#
# Memoization (like Memo - a reminder / log)
# since there are a lot of very similar calls (duplicate identical sub-trees in the calls tree)
# (for instance we make the calls fib(3)-->[fib(1),fib(2)-->[fib(0),fib(1)]]
#   a lot of times - for fib(3), fib(4), fib(5)...)
# we can just "remember" the result for duplicate function calls,
# instead of multiple calls for same value).
# so we want to store those results that we are likely to get more than once
# and refer to that storage, instead of make the same call again and again.
# so time complexity goes down to O(n) -- explain!
# since in every node n in a sub tree we have to child nodes n-1 and n-2
# and for every node n-1 we call n-2 and n-3.
# but for n-1 we already know the result for n-2 (because we already calculated it (for n..))
# and the same for n-3 and so on. so instead of having a "full" binary tree we get a chain of n nodes
# and for each of the nodes these is a sister node (except for root) - so all in all we have 2n-1 nodes.
# each node represents a functions call (and each sister node - a hashmap/dict result
# so the time complexity is O(n)
# and the space complexity stays the same - O(n)
#
#
#
#
#
