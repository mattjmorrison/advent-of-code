import pytest
from data import DATA
from puzzle import Puzzle, Point


def test_solution_one() -> None:
    puzzle = Puzzle(DATA)
    assert puzzle.answer == 557


def test_solution_two() -> None:
    puzzle = Puzzle(DATA, rating=True)
    assert puzzle.answer == 1062


EXAMPLE = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
""".strip()


def test_example_with_rating() -> None:
    puzzle = Puzzle(EXAMPLE, rating=True)
    assert puzzle.answer == 81


def test_example_without_rating() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.answer == 36


def test_finds_trail_heads() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.trail_heads == [
        Point(0, 0, 2),
        Point(0, 0, 4),
        Point(0, 2, 4),
        Point(0, 4, 6),
        Point(0, 5, 2),
        Point(0, 5, 5),
        Point(0, 6, 0),
        Point(0, 6, 6),
        Point(0, 7, 1),
    ]


def test_get_next_move_from_point() -> None:
    puzzle = Puzzle(EXAMPLE)
    moves = puzzle.get_next_moves(puzzle.trail_heads[0])
    assert moves == [
        Point(1, 1, 2),
        Point(1, 0, 3),
    ]


def test_creates_grid_of_points_from_input() -> None:
    puzzle = Puzzle("""
123
456
789
    """.strip())

    assert puzzle.grid == [
        [Point(1, 0, 0), Point(2, 0, 1), Point(3, 0, 2)],
        [Point(4, 1, 0), Point(5, 1, 1), Point(6, 1, 2)],
        [Point(7, 2, 0), Point(8, 2, 1), Point(9, 2, 2)],
    ]


#
# Point tests - this should be in it's own file, but nah
#

def test_point_has_value_and_coords() -> None:
    point = Point(value=1, row=2, column=3)
    assert point.value == 1
    assert point.row == 2
    assert point.column == 3


def test_points_are_equal_when_have_same_value_and_coords() -> None:
    point_one = Point(value=1, row=2, column=3)
    point_two = Point(value=1, row=2, column=3)
    assert point_one == point_two


@pytest.mark.parametrize('row, column, results', (
    (
        0, 0, (
            (1, 0),
            (0, 1),
        ),
    ),
    (
        1, 1, (
            (2, 1),
            (1, 2),
            (0, 1),
            (1, 0),
        )
    ),
))
def test_point_gets_neighbor_coords(
    row: int, column: int, results: tuple[tuple[int, int], ...]
) -> None:
    point = Point(0, row, column)
    assert point.neighbors == results


@pytest.mark.parametrize('row_1, column_1, row_2, column_2, result', (
    (0, 0, 0, 1, True),
    (0, 1, 0, 2, True),
    (0, 0, 2, 2, False),
    (1, 1, 0, 1, True),
    (1, 1, 1, 0, True),
    (1, 1, 1, 2, True),
    (1, 1, 2, 1, True),
    (1, 1, 3, 1, False),
))
def test_point_knows_if_another_point_is_neighbor(
    row_1: int, column_1: int, row_2: int, column_2: int, result: bool
) -> None:
    point = Point(0, row_1, column_1)
    assert point.is_neighbor(Point(0, row_2, column_2)) == result


@pytest.mark.parametrize('current, neighbor, result', (
    ((0, 0, 0), (2, 0, 1), False),
    ((0, 0, 1), (0, 0, 2), False),
    ((0, 0, 0), (1, 2, 2), False),
    ((0, 1, 1), (1, 0, 1), True),
    ((0, 1, 1), (1, 1, 0), True),
    ((0, 1, 1), (1, 1, 2), True),
    ((0, 1, 1), (1, 2, 1), True),
    ((0, 1, 1), (1, 3, 1), False),
))
def test_returns_next_neighbor(
    current: tuple[int, int, int],
    neighbor: tuple[int, int, int],
    result: bool
) -> None:
    point = Point(current[0], *current[1:])
    assert point.is_next_neighbor(
        Point(neighbor[0], *neighbor[1:])
    ) == result


def test_point_str_and_repr() -> None:
    point = Point(0, 1, 2)
    assert str(point) == repr(point) == '0-1-2'


def test_point_is_hashable() -> None:
    point = Point(0, 0, 0)
    assert 10001 == hash(point)
