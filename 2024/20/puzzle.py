from functools import cached_property
from collections import deque

MODS = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
)

CHEATS = (
    (2, 0),
    (1, 1),
    (0, 2),
    (-1, 1),

    (-2, 0),
    (-1, -1),
    (0, -2),
    (1, -1)
)


class Puzzle:

    def __init__(self, data: str):
        self.data = data
        self._distances: list[list[int]] = []

    @property
    def answer(self) -> int:
        count = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if self.is_wall(row, col):
                    continue
                for new_row, new_col in self.cheat_dirs((row, col)):
                    if self.is_outside_grid(new_row, new_col):
                        continue
                    if self.is_wall(new_row, new_col):
                        continue
                    if self.distances[row][col] - self.distances[new_row][new_col] >= 102:
                        count += 1
        return count

    def dirs(self, coords: tuple[int, int]) -> list[tuple[int, int]]:
        dirs = []
        for row, col in MODS:
            dirs.append((coords[0] + row, coords[1] + col))
        return dirs

    def cheat_dirs(self, coords: tuple[int, int]) -> list[tuple[int, int]]:
        dirs = []
        for row, col in CHEATS:
            dirs.append((coords[0] + row, coords[1] + col))
        return dirs
    
    @property
    def part_two(self) -> int:
        count = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if self.is_wall(row, col):
                    continue
                for distance in range(2, 21):
                    for row_dist in range(distance + 1):
                        col_dist = distance - row_dist
                        for new_row, new_col in set([
                            (row + row_dist, col + col_dist),
                            (row + row_dist, col - col_dist),
                            (row - row_dist, col + col_dist),
                            (row - row_dist, col - col_dist),
                        ]):
                            if self.is_outside_grid(new_row, new_col):
                                continue
                            if self.is_wall(new_row, new_col):
                                continue
                            if self.distances[row][col] - self.distances[new_row][new_col] >= 100 + distance:
                                count += 1
        return count

    def is_outside_grid(self, row: int, col: int) -> bool:
        if row < 0 or row >= self.rows:
            return True
        if col < 0 or col >= self.cols:
            return True
        return False

    def is_wall(self, row: int, col: int) -> bool:
        return self.grid[row][col] == '#'

    def already_checked(self, row: int, col: int) -> bool:
        return self._distances[row][col] != -1

    def needs_checked(self, row: int, col: int) -> bool:
        return not any([
            self.is_outside_grid(row, col),
            self.is_wall(row, col),
            self.already_checked(row, col),
        ])

    @cached_property
    def distances(self) -> list[list[int]]:
        if not self._distances:
            self._build_distances()
        return self._distances

    def _build_distances(self) -> None:
        self._distances = [[-1] * self.cols for _ in range(self.rows)]
        self._distances[self.start[0]][self.start[1]] = 0
        queue = deque([self.start])
        while queue:
            cur_row, cur_col = queue.popleft()
            for new_row, new_col in self.dirs((cur_row, cur_col)):
                if self.needs_checked(new_row, new_col):
                    self._distances[new_row][new_col] = (
                        self._distances[cur_row][cur_col] + 1
                    )
                    queue.append((new_row, new_col))

    @property
    def rows(self) -> int:
        return len(self.grid)

    @property
    def cols(self) -> int:
        return len(self.grid[0])

    @cached_property
    def grid(self) -> tuple[tuple[str, ...], ...]:
        grid = []
        for row_data in self.data.split('\n'):
            row = []
            for column in row_data:
                row.append(column)
            grid.append(tuple(row))
        return tuple(grid)

    @cached_property
    def start(self) -> tuple[int, int]:
        return self._find_spot('S')

    @cached_property
    def end(self) -> tuple[int, int]:
        return self._find_spot('E')

    def _find_spot(self, char: str) -> tuple[int, int]:
        for rindex, row in enumerate(self.grid):
            for cindex, column in enumerate(row):
                if column == char:
                    return (rindex, cindex)
        return (0, 0)
