from typing import Optional
from functools import lru_cache
from itertools import chain
from collections import defaultdict


# pylint: disable=too-many-public-methods
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
    def discounted_answer(self) -> int:
        total = 0
        for region in self.get_regions():
            total += self.calc_discounted_price(region[0])
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

    def count_discounted_sides(self, plot: tuple[int, int]) -> int:
        region = self.build_region(plot)
        return sum([
            self.count_top_edge(region),
            self.count_right_edge(region),
            self.count_bottom_edge(region),
            self.count_left_edge(region),
        ])

    def count_top_edge(self, region: list[tuple[int, int]]) -> int:
        top_edge_plots = []
        for row, col in region:
            if (row - 1, col) not in region:
                top_edge_plots.append((row, col))
        return self.count_column_gaps(top_edge_plots)

    def count_column_gaps(  # noqa: C901
        self, edge_plots: list[tuple[int, int]]
    ) -> int:
        groups = defaultdict(list)
        for plot in edge_plots:
            groups[plot[0]].append(plot[1])
        edges = 0
        for a in groups.values():
            b = sorted(a)
            edges += 1
            for i in range(len(b) - 1):
                if b[i] + 1 != b[i + 1]:
                    edges += 1
        return edges

    def count_row_gaps(  # noqa: C901
        self, edge_plots: list[tuple[int, int]]
    ) -> int:
        groups = defaultdict(list)
        for plot in edge_plots:
            groups[plot[1]].append(plot[0])
        edges = 0
        print(groups)
        for a in groups.values():
            b = sorted(a)
            edges += 1
            for i in range(len(b) - 1):
                if b[i] + 1 != b[i + 1]:
                    edges += 1
        return edges

    def count_bottom_edge(self, region: list[tuple[int, int]]) -> int:
        bottom_edge_plots = []
        for row, col in region:
            if (row + 1, col) not in region:
                bottom_edge_plots.append((row, col))
        return self.count_column_gaps(bottom_edge_plots)

    def count_right_edge(self, region: list[tuple[int, int]]) -> int:
        right_edge_plots = []
        for row, col in region:
            if (row, col + 1) not in region:
                right_edge_plots.append((row, col))
        return self.count_row_gaps(right_edge_plots)

    def count_left_edge(self, region: list[tuple[int, int]]) -> int:
        left_edge_plots = []
        for row, col in region:
            if (row, col - 1) not in region:
                left_edge_plots.append((row, col))
        return self.count_row_gaps(left_edge_plots)

    def get_edges_with_no_neighbors(
        self, plot: tuple[int, int]
    ) -> list[tuple[int, int]]:
        outside_edges = []
        row, col = plot
        if row - 1 < 0 or row + 1 >= len(self.data):
            outside_edges += [plot]
        if col - 1 < 0 or col + 1 >= len(self.data[0]):
            outside_edges += [plot]
        return outside_edges + list(set(
                self.get_neighbor_coords(plot)
            ).difference(
                set(self.get_neighbors_with_matching_plant(plot))
            )
        )

    def count_sides_with_no_neighbors(self, plot: tuple[int, int]) -> int:
        return len(self.get_edges_with_no_neighbors(plot))

    def calc_price(self, plot: tuple[int, int]) -> int:
        sides = self.calc_perimeter(plot)
        area = self.calc_area(plot)
        return sides * area

    def calc_discounted_price(self, plot: tuple[int, int]) -> int:
        sides = self.count_discounted_sides(plot)
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
