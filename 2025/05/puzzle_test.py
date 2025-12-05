from textwrap import dedent
from puzzle import Puzzle
from data import input

TEST_INPUT: str = dedent(text="""
    3-5
    10-14
    16-20
    12-18

    1
    5
    8
    11
    17
    32
""").strip()

def test_parse():
    puzzle: Puzzle = Puzzle(TEST_INPUT)
    fresh, available = puzzle.parse()
    assert fresh == [
        (3, 5),
        (10, 14),
        (16, 20),
        (12, 18),
    ]
    assert available == [
        1, 5, 8, 11, 17, 32
    ]


def test_part_one_example():
    puzzle: Puzzle = Puzzle(TEST_INPUT)
    assert puzzle.solve_part_one() == 3


def test_part_two_example():
    puzzle: Puzzle = Puzzle(TEST_INPUT)
    assert puzzle.solve_part_two() == 14


def test_solve_part_one():
    puzzle: Puzzle = Puzzle(input)
    assert puzzle.solve_part_one() == 848


# def test_solve_part_two():
#     puzzle: Puzzle = Puzzle(input)
#     assert puzzle.solve_part_two() == ""
