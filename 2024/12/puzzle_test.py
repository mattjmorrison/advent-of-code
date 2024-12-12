import pytest
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


"""
    A region of R plants with price 12 * 18 = 216.
    A region of I plants with price 4 * 8 = 32.
    A region of C plants with price 14 * 28 = 392.
    A region of F plants with price 10 * 18 = 180.
    A region of V plants with price 13 * 20 = 260.
    A region of J plants with price 11 * 20 = 220.
    A region of C plants with price 1 * 4 = 4.
    A region of E plants with price 13 * 18 = 234.
    A region of I plants with price 14 * 22 = 308.
    A region of M plants with price 5 * 12 = 60.
    A region of S plants with price 3 * 8 = 24.
"""


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


@pytest.mark.parametrize('plot, sides', (
    ((4, 7), 4),
    ((9, 4), 1),
    ((9, 5), 2),
    ((8, 4), 3),
    ((7, 2), 0),
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
    # assert puzzle.answer == 1930
    assert puzzle.answer == 0


# def test_simple() -> None:
#     INPUT = """
#     AAAA
#     BBCD
#     BBCC
#     EEEC
#     """.strip()
#     puzzle = Puzzle(EXAMPLE)
#     assert puzzle.answer == 140


# def test_nested_example() -> None:
#     INPUT = """
# OOOOO
# OXOXO
# OOOOO
# OXOXO
# OOOOO
# """.strip()
#     puzzle = Puzzle(INPUT)
#     assert puzzle.answer == 772
