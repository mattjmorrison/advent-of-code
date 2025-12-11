from itertools import combinations

class Puzzle:

    def __init__(self, input):
        self.input: str = input

    def parse(self):
        rows = [r.split(',') for r in self.input.split('\n')]
        return [(int(x), int(y)) for x, y in rows]

    def calc_part_one(self, args):
        (x1, y1), (x2, y2) = args
        height = (max((x1, x2)) - min((x1, x2))) + 1
        width = (max((y1, y2)) - min((y1, y2))) + 1
        result = height * width
        return result

    def solve_part_one(self):
        points = self.parse()
        combos = combinations(points + points, 2)
        results = map(self.calc_part_one, combos)
        return max(results)
