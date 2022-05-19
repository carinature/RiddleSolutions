#
#   Date - 18.05.2022
#
#
# BFS
#
#
# DFS
#
#
#

from math import prod
import timeit
from typing import List, Optional, Set, Dict


def bfs_print(graph: Dict[str, list], start_node: str):
    """
    The best way to get ahead is to get starting..?
    """
    seen: List[str] = []
    unseen: List[str] = [start_node]  # Queue
    while unseen:
        node = unseen.pop(0)
        if node not in seen:
            print(node)
            seen.append(node)
        unseen.extend(graph[node])
    return


def testing():
    graph: Dict[str, list] = {
        'a': ['b', 'c'],
        'b': ['d', 'e'],
        'c': ['f', 'g'],
        'd': [],
        'e': [],
        'f': [],
        'g': []
    }

    bfs_print(graph, 'a')

    # result = some_function(nums=124356)
    # print(f"result: {result}")
    # assert (124356 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
