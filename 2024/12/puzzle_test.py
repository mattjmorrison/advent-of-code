import pytest
from data import DATA
from puzzle import Puzzle


EXAMPLE = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
""".strip()


def test_count_top_edge() -> None:
    puzzle = Puzzle(EXAMPLE)
    region = puzzle.build_region((0, 0))
    assert puzzle.count_top_edge(region) == 2


def test_count_right_edge() -> None:
    puzzle = Puzzle(EXAMPLE)
    region = puzzle.build_region((0, 0))
    assert puzzle.count_right_edge(region) == 3


def test_count_bottom_edge() -> None:
    puzzle = Puzzle(EXAMPLE)
    region = puzzle.build_region((0, 0))
    assert puzzle.count_bottom_edge(region) == 3


def test_count_left_edge() -> None:
    puzzle = Puzzle(EXAMPLE)
    region = puzzle.build_region((0, 0))
    assert puzzle.count_left_edge(region) == 2


def test_inner_boundaries() -> None:
    data = """
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
    """.strip()
    puzzle = Puzzle(data)
    region = puzzle.build_region((0, 0))
    assert puzzle.count_top_edge(region) == 3
    assert puzzle.count_right_edge(region) == 3
    assert puzzle.count_bottom_edge(region) == 3
    assert puzzle.count_left_edge(region) == 3


def test_find_top_gaps() -> None:
    puzzle = Puzzle("")
    top_edges = [
        (0, 0),         (0, 3),
                (1, 2),         (1, 4),  # noqa: E131
    ]
    assert puzzle.count_top_edge(top_edges) == 4


def test_find_bottom_gaps() -> None:
    puzzle = Puzzle("")
    bottom_edges = [
        (0, 0),         (0, 3),
                (1, 2),         (1, 4),  # noqa: E131
    ]
    assert puzzle.count_bottom_edge(bottom_edges) == 4


def test_find_right_gaps() -> None:
    puzzle = Puzzle("")
    right_edges = [
        (0, 0),
                (1, 2),  # noqa: E131
        (2, 0),
                (3, 2),  # noqa: E131
    ]
    assert puzzle.count_right_edge(right_edges) == 4


def test_find_left_gaps() -> None:
    puzzle = Puzzle("")
    left_edges = [
        (0, 0),
                (1, 2),  # noqa: E131
        (2, 0),
                (3, 2),  # noqa: E131
    ]
    assert puzzle.count_left_edge(left_edges) == 4


def test_inner_boundaries_two() -> None:
    data = """
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
    """.strip()
    puzzle = Puzzle(data)
    region = puzzle.build_region((0, 0))
    assert puzzle.count_top_edge(region) == 5
    assert puzzle.count_right_edge(region) == 5
    assert puzzle.count_bottom_edge(region) == 5
    assert puzzle.count_left_edge(region) == 5


@pytest.mark.parametrize('plot, sides', (
    ((0, 0), 10),
))
def test_discounted_sides_example(
    plot: tuple[int, int], sides: int
) -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.count_discounted_sides(plot) == sides


@pytest.mark.parametrize('plot, price', (
    ((0, 0), 216),
    ((0, 4), 32),
    ((0, 6), 392),
    ((0, 9), 180),
    ((2, 0), 260),
    ((3, 6), 220),
    ((4, 7), 4),
    ((4, 9), 234),
    ((5, 2), 308),
    ((7, 0), 60),
    ((9, 4), 24),
))
def test_example_costs(plot: tuple[int, int], price: int) -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.calc_price(plot) == price


def test_get_all_regions() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert len(puzzle.get_regions()) == 11


def test_find_neighbors_with_skip() -> None:
    puzzle = Puzzle(EXAMPLE)
    results = puzzle.get_neighbors_with_matching_plant((0, 0), skip=(1, 0))
    assert results == [
        (0, 1),
    ]


def test_build_region_for_plant() -> None:
    puzzle = Puzzle(EXAMPLE)
    results = puzzle.build_region((0, 0))
    assert sorted(results) == sorted([
        (0, 0), (0, 1), (0, 2), (0, 3),
        (1, 0), (1, 1), (1, 2), (1, 3),
        (2, 2), (2, 3), (2, 4), (3, 2),
    ])


@pytest.mark.parametrize('plot, perimeter', (
    ((4, 7), 4),
    ((9, 4), 8),
))
def test_perimeter(plot: tuple[int, int], perimeter: int) -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.calc_perimeter(plot) == perimeter


@pytest.mark.parametrize('plot, area', (
    ((4, 7), 1),
    ((9, 4), 3),
))
def test_area(plot: tuple[int, int], area: int) -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.calc_area(plot) == area


@pytest.mark.parametrize('plot, sides', (
    ((4, 7), 4),
    ((9, 4), 2),
    ((9, 5), 3),
    ((8, 4), 3),
    ((7, 2), 0),
    ((0, 0), 2),
    ((0, 9), 2),
    ((9, 0), 2),
))
def test_gets_number_of_sides_with_no_neighbors(
    plot: tuple[int, int], sides: int
) -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.count_sides_with_no_neighbors(plot) == sides


def test_builds_initial_structure() -> None:
    data = """
ABCD
EFGH
IJKL
    """.strip()
    puzzle = Puzzle('')
    assert puzzle.parse(data) == [
        ['A', 'B', 'C', 'D'],
        ['E', 'F', 'G', 'H'],
        ['I', 'J', 'K', 'L'],
    ]


def test_counts_unique_plants() -> None:
    data = """
ABLA
ELAH
IAKL
""".strip()
    puzzle = Puzzle(data)
    assert sorted(puzzle.unique_plants) == [
        'A', 'B', 'E', 'H', 'I', 'K', 'L'
    ]


@pytest.mark.parametrize('plot, results', (
    (
        (1, 1),
        [
            (0, 1),
            (2, 1),
            (1, 2),
            (1, 0),
        ]
    ),
    (
        (0, 0),
        [
            (1, 0),
            (0, 1),
        ]
    ),
    (
        (1, 2),
        [
            (0, 2),
            (2, 2),
            (1, 1),

        ]
    ),
    (
        (0, 1),
        [
            (1, 1),
            (0, 2),
            (0, 0),
        ]
    ),
    (
        (1, 0),
        [
            (0, 0),
            (2, 0),
            (1, 1),

        ]
    ),
))
def test_get_neighbor_coords(
    plot: tuple[int, int], results: list[tuple[int, int]]
) -> None:
    data = """
ABC
DEF
GHI
    """.strip()
    puzzle = Puzzle(data)
    assert puzzle.get_neighbor_coords(plot) == results


@pytest.mark.parametrize('data, plot, results', (
    (
        """
BAB
AAA
BAB
        """.strip(),
        (1, 1),
        [
            (0, 1),
            (2, 1),
            (1, 2),
            (1, 0),
        ]
    ),
    (
        """
BAB
AAA
BAB
        """.strip(),
        (0, 0),
        []
    ),
))
def test_get_neighbors_with_matching_plant(
    data: str, plot: tuple[int, int], results: list[tuple[int, int]]
) -> None:
    puzzle = Puzzle(data)
    assert puzzle.get_neighbors_with_matching_plant(plot) == results


def test_example() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.answer == 1930


def test_simple() -> None:
    data = """
AAAA
BBCD
BBCC
EEEC
    """.strip()
    puzzle = Puzzle(data)
    assert puzzle.answer == 140


def test_nested_example() -> None:
    data = """
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
    """.strip()
    puzzle = Puzzle(data)
    assert puzzle.answer == 772
    assert puzzle.discounted_answer == 436


def test_discount() -> None:
    data = """
AAAA
BBCD
BBCC
EEEC
    """.strip()
    puzzle = Puzzle(data)
    assert puzzle.answer == 140
    assert puzzle.discounted_answer == 80


def test_discount_example_two() -> None:
    data = """
EEEEE
EXXXX
EEEEE
EXXXX
EEEEE
    """.strip()
    puzzle = Puzzle(data)
    assert puzzle.answer == 692
    assert puzzle.discounted_answer == 236


def test_discount_example_three() -> None:
    data = """
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
    """.strip()
    puzzle = Puzzle(data)
    assert puzzle.answer == 1184
    assert puzzle.discounted_answer == 368


def test_part_one() -> None:
    puzzle = Puzzle(DATA)
    assert puzzle.answer == 1_467_094


def test_part_two() -> None:
    puzzle = Puzzle(DATA)
    assert puzzle.discounted_answer == 881_182
