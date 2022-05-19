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


class SomethingToWatch:
    def __init__(self, name: str, genre: str):
        self.name = name
        self.genre = genre

    def __repr__(self):
        s: str = f'{type(self).__name__}\n'
        for k, v in self.__dict__.items():
            s += f' - {k} = {v}\n'
        return s


class Movie(SomethingToWatch):
    def __init__(self, name: str, genre: str, time: int):
        super().__init__(name, genre)
        self.time = time


class Series(SomethingToWatch):
    def __init__(self, name: str, genre: str, seasons: int):
        super().__init__(name, genre)
        self.episodes = seasons


def testing():

    movie = Movie("Up", "Cartoon", 130)
    series = Series("My Name is Earl", "Comedy", 4)
    print(f'Movie - {movie}')
    print(f'Series - {series}')


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
