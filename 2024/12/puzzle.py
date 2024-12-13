from typing import Optional
from functools import lru_cache
from itertools import chain


class Puzzle:

    def __init__(self, data: str):
        self._data = data

    @property
    def answer(self) -> int:
        total = 0
        for region in self.get_regions():
            total += self.calc_price(region[0])
        return total

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

    def calc_area(self, plot: tuple[int, int]) -> int:
        return len(self.build_region(plot))

    def count_sides_with_no_neighbors(self, plot: tuple[int, int]) -> int:
        outside_edges = 0
        row, col = plot
        if row - 1 < 0 or row + 1 >= len(self.data):
            outside_edges += 1
        if col - 1 < 0 or col + 1 >= len(self.data[0]):
            outside_edges += 1
        return outside_edges + len(
            set(
                self.get_neighbor_coords(plot)
            ).difference(
                set(self.get_neighbors_with_matching_plant(plot))
            )
        )

    def calc_price(self, plot: tuple[int, int]) -> int:
        sides = self.calc_perimeter(plot)
        area = self.calc_area(plot)
        return sides * area

    def get_regions(self) -> list[list[tuple[int, int]]]:
        regions: list[list[tuple[int, int]]] = []
        for rindex, row in enumerate(self.data):
            for cindex, _ in enumerate(row):
                plot = (rindex, cindex)
                if not self.already_plotted(regions, plot):
                    regions.append(self.build_region(plot))
        return regions

    def already_plotted(
        self, regions: list[list[tuple[int, int]]],
        plot: tuple[int, int]
    ) -> bool:
        for region in regions:
            if plot in region:
                return True
        return False
