#
#   Date - 18.05.2022
#
#
# BFS
#   Breadth First Search
#   remove node from the front of the line
#   add all it's child nodes to the end of the line
#
# DFS
#   Breadth First Search
#   remove node from the back of the line, and explore the next
#   add all it's child nodes to the end of the line
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
    print(' --- bfs_print --- ')
    seen: List[str] = []
    unseen: List[str] = [start_node]  # Queue
    while unseen:
        node = unseen.pop(0)
        if node not in seen:
            print(node)
            seen.append(node)
        unseen.extend(graph[node])
    print(' ----------------- ')
    return


def dfs_print(graph: Dict[str, list], start_node: str):
    """
    The best way to get ahead is to get starting..?
    """
    print(' --- dfs_print --- ')
    seen: List[str] = []
    unseen: List[str] = [start_node]  # Stack
    while unseen:
        node = unseen.pop()
        if node not in seen:
            print(node)
            seen.append(node)
        unseen.extend(reversed(graph[node]))
    print(' ----------------- ')
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
    dfs_print(graph, 'a')

    # result = some_function(nums=124356)
    # print(f"result: {result}")
    # assert (124356 == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
