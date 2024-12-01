from collections import Counter


class Puzzle:

    def __init__(self, input: str):
        self.input = input
        self._left: list[int] = []
        self._right: list[int] = []

    @property
    def number_sets(self):
        for r in self.input.split('\n'):
            a, b = r.split()
            self._left.append(int(a))
            self._right.append(int(b))

        return zip(sorted(self._left), sorted(self._right))

    @property
    def number_diffs(self):
        for a, b in self.number_sets:
            yield abs(a - b)

    @property
    def diffs_sum(self):
        return sum(self.number_diffs)

    @property
    def similarity_scores(self):
        tuple(self.number_sets)
        counter = Counter(self._right)
        for a in self._left:
            if a in counter:
                yield a * counter[a]
            else:
                yield 0

    @property
    def similarity_sum(self):
        return sum(self.similarity_scores)