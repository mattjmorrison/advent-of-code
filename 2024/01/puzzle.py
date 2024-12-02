from collections import Counter
from typing import Generator, Iterator

class Puzzle:

    def __init__(self, input: str):
        self.input = input
        self._left: list[int] = []
        self._right: list[int] = []

    @property
    def number_sets(self) -> Iterator[tuple[int, int]]:
        for r in self.input.split('\n'):
            a, b = r.split()
            self._left.append(int(a))
            self._right.append(int(b))

        return zip(sorted(self._left), sorted(self._right))

    @property
    def number_diffs(self) -> Generator[int]:
        for a, b in self.number_sets:
            yield abs(a - b)

    @property
    def diffs_sum(self) -> int:
        return sum(self.number_diffs)

    @property
    def similarity_scores(self) -> Generator[int]:
        tuple(self.number_sets)
        counter = Counter(self._right)
        for a in self._left:
            if a in counter:
                yield a * counter[a]
            else:
                yield 0

    @property
    def similarity_sum(self) -> int:
        return sum(self.similarity_scores)