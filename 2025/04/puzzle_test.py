from textwrap import dedent
from puzzle import Puzzle
from data import input

import pytest

# fewer than four

TEST_INPUT = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
""".strip()


def test_example():
    puzzle = Puzzle(TEST_INPUT)
    assert puzzle.solve_part_one() == 13


def test_parse():
    puzzle = Puzzle(dedent("""
    .@
    @@
    """).strip())
    assert puzzle.parse() == [
        ['.', '@'],
        ['@', '@']
    ]


@pytest.mark.parametrize('row, column, neighbors', (
    (0, 0, ['2', '3', '4']),
    (0, 1, ['1', '3', '4']),
    (1, 0, ['1', '2', '4']),
    (1, 1, ['1', '2', '3']),
))
def test_get_neighbors(row, column, neighbors):
    puzzle = Puzzle(dedent("""
    12
    34
    """).strip())
    grid = puzzle.parse()
    assert puzzle.get_neighbors(row, column, grid) == neighbors


def test_get_paper_roll_coords():
    puzzle = Puzzle(dedent("""
    @.
    .@
    """).strip())
    grid = puzzle.parse()
    assert puzzle.get_paper_rolls(grid) == [(0, 0), (1, 1)]


def test_part_one():
    puzzle = Puzzle(input)
    assert puzzle.solve_part_one() == 1437


def test_part_two():
    puzzle = Puzzle(input)
    assert puzzle.solve_part_two() == 8765