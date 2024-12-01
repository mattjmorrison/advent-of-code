

class Puzzle:

    def __init__(self, input):
        self.input = input

    @property
    def number_sets(self):
        left, right = [], []
        for r in self.input.split('\n'):
            a, b = r.split()
            left.append(int(a))
            right.append(int(b))

        return zip(sorted(left), sorted(right))

    @property
    def number_diffs(self):
        for a, b in self.number_sets:
            yield abs(a - b)

    @property
    def diffs_sum(self):
        return sum(self.number_diffs)