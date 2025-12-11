from itertools import combinations
from functools import lru_cache
from collections import defaultdict

class Puzzle:

    def __init__(self, input):
        self.input: str = input

    def parse(self) -> list[tuple[int, int]]:
        rows = [r.split(',') for r in self.input.split('\n')]
        return [(int(x), int(y)) for x, y in rows]

    def calc_part_one(self, args) -> int:
        (x1, y1), (x2, y2) = args
        height = (max((x1, x2)) - min((x1, x2))) + 1
        width = (max((y1, y2)) - min((y1, y2))) + 1
        result = height * width
        return result

    def solve_part_one(self) -> int:
        points = self.parse()
        combos = combinations(points, 2)
        results = map(self.calc_part_one, combos)
        return max(results)

    @lru_cache
    def build_grid(self):
        points: list[tuple[int, int]] = self.parse()
        grid: list[tuple[int, int]] = []
        for combo in combinations(points, 2):
            (x1, y1), (x2, y2) = combo

            if x1 == x2:
                for y_loop in range(min((y1, y2)), max((y1, y2)) + 1):
                    if (x1, y_loop) not in grid:
                        grid.append((x1, y_loop))
            elif y1 == y2:
                for x_loop in range(min((x1, x2)), max((x1, x2)) + 1):
                    if (x_loop, y1) not in grid:
                        grid.append((x_loop, y1))
        return grid

    def solve_part_two(self) -> int:
        points: list[tuple[int, int]] = self.parse()
        matches: list[int] = []
        for combo in combinations(points, 2):
            if self.exists_in_grid(combo):
                matches.append(self.calc_part_one(combo))
        return max(matches)

    @lru_cache
    def exists_in_grid(self, coords):
        print(coords)
        min_x: int = min((coords[0][0], coords[1][0]))
        max_x: int = max((coords[0][0], coords[1][0]))
        min_y: int = min((coords[0][1], coords[1][1]))
        max_y: int = max((coords[0][1], coords[1][1]))
        grid = self.build_grid()
        return all(map(lambda c: c[0] <= min_x or c[0] >= max_x or c[1] <= min_y or c[1] >= max_y, grid))