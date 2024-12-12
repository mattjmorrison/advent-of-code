from typing import Optional
from functools import lru_cache
from itertools import chain


class Puzzle:

    def __init__(self, data: str):
        self._data = data

    @property
    def answer(self) -> int:
        return 0

    @property
    def data(self) -> list[list[str]]:
        return self.parse(self._data)

    @lru_cache(maxsize=10)
    def parse(self, data: str) -> list[list[str]]:
        return [list(x) for x in data.split('\n')]

    @property
    def unique_plants(self) -> list[str]:
        return list(set(chain(*self.data)))

    def get_neighbor_coords(
        self, plot: tuple[int, int]
    ) -> list[tuple[int, int]]:
        row, col = plot
        mods = (
            (-1, 0),
            (1, 0),
            (0, 1),
            (0, -1),
        )
        results = []
        for arow, acol in mods:
            nrow = row + arow
            ncol = col + acol
            if not self.too_small(nrow, ncol) and not self.too_big(nrow, ncol):
                results.append((nrow, ncol))
        return results

    def too_small(self, row: int, col: int) -> bool:
        return row < 0 or col < 0

    def too_big(self, row: int, col: int) -> bool:
        return row >= len(self.data) or col >= len(self.data[0])

    def get_neighbors_with_matching_plant(
        self, plot: tuple[int, int], skip: Optional[tuple[int, int]] = None
    ) -> list[tuple[int, int]]:
        matches = []
        row, col = plot
        plant = self.data[row][col]
        for nrow, ncol in self.get_neighbor_coords(plot):
            if self.data[nrow][ncol] == plant:
                if skip and skip == (nrow, ncol):
                    continue
                matches.append((nrow, ncol))
        return matches

    def build_region(
        self, plot: tuple[int, int],
        region: Optional[list[tuple[int, int]]] = None,
    ) -> list[tuple[int, int]]:
        region = region or [plot]
        for neighbor in self.get_neighbors_with_matching_plant(plot):
            if neighbor not in region:
                region.append(neighbor)
                self.build_region(neighbor, region)
        return region

    def calc_perimeter(self, plot: tuple[int, int]) -> int:
        total = 0
        for one in self.build_region(plot):
            total += self.count_sides_with_no_neighbors(one)
        return total

    def count_sides_with_no_neighbors(self, plot: tuple[int, int]) -> int:
        return len(
            set(
                self.get_neighbor_coords(plot)
            ).difference(
                set(self.get_neighbors_with_matching_plant(plot))
            )
        )
