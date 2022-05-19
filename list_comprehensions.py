#
#   Date - 18.05.2022
#
#
# Binary Search
#
#

from math import prod
import timeit
from typing import List, Optional, Set, Dict


def testing():
    l = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5]

    l_odd = [x for x in l if x % 2]
    print(f"l_odd {l_odd}")
    # [1, 3, 5, 7, 1, 3, 5]

    # Tuples
    l_odd_tuple = tuple((x for x in l if x % 2))
    print(f"l_odd {l_odd_tuple}")
    # (1, 3, 5, 7, 1, 3, 5)

    # Sets
    l_odd_set = {x for x in l if x % 2}
    print(f"l_odd {l_odd_set}")
    l_odd_set
    # {1, 3, 5, 7}

    # Dictionaries
    l_odd_dict = {x: x ** 2 for x in l}
    print(f"l_odd {l_odd_dict}")
    # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
    # Note that dict keys are a set of the list items(no repetitions)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
