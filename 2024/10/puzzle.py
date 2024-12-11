from typing import Self
from functools import cached_property, lru_cache


class Point:
    MODS = (
        (-1, 0),
        (0, -1),
        (1, 0),
        (0, 1)
    )

    def __init__(self, value: int, row: int, column: int):
        self.value = value
        self.row = row
        self.column = column

    def __str__(self) -> str:
        return f'{self.value}-{self.row}-{self.column}'

    def __repr__(self) -> str:
        return str(self)

    def __hash__(self) -> int:
        return int(f"1{self.value}{self.row}{self.column}1")

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Point) and all([
            self.value == other.value,
            self.row == other.row,
            self.column == other.column,
        ])

    @cached_property
    def neighbors(self) -> tuple[tuple[int, int], ...]:
        results = []
        for row, col in self.MODS:
            new_row = self.row - row
            new_col = self.column - col
            if new_row >= 0 and new_col >= 0:
                results.append((new_row, new_col))
        return tuple(results)

    def is_neighbor(self, point: Self) -> bool:
        for row, column in self.neighbors:
            if point.row == row and point.column == column:
                return True
        return False

    def is_next_neighbor(self, point: Self) -> bool:
        next_value = self.value + 1 == point.value
        return self.is_neighbor(point) and next_value


class Puzzle:

    def __init__(self, data: str, rating: bool = False):
        self.data = data
        self.rating = rating

    @property
    def answer(self) -> int:
        total: int = 0
        for trail_head in self.trail_heads:
            ends = self.walk_trail(trail_head)
            total += len(ends if self.rating else set(ends))
        return total

    @lru_cache(maxsize=5000)
    def walk_trail(self, point: Point) -> list[Point]:
        points: list[Point] = []
        for move in self.get_next_moves(point):
            if move.value == 9:
                points.append(move)
            else:
                points.extend(self.walk_trail(move))
        return points

    @cached_property
    def trail_heads(self) -> list[Point]:
        heads = []
        for row in self.grid:
            for point in row:
                if point.value == 0:
                    heads.append(point)
        return heads

    @cached_property
    def grid(self) -> list[list[Point]]:
        grid: list[list[Point]] = []
        for rindex, row in enumerate(self.data.split('\n')):
            grid.append([])
            for cindex, value in enumerate(list(row)):
                grid[rindex].append(
                    Point(value=int(value), row=rindex, column=cindex)
                )
        return grid

    def get_next_moves(self, point: Point) -> list[Point]:
        next_move: list[Point] = []
        for row, column in point.neighbors:
            if row < len(self.grid) and column < len(self.grid[row]):
                neighbor_point = self.grid[row][column]
                if point.is_next_neighbor(neighbor_point):
                    next_move.append(neighbor_point)
        return next_move
