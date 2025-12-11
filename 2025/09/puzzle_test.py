from puzzle import Puzzle

from data import input

TEST_INPUT = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
""".strip()


def test_part_one_example():
    puzzle = Puzzle(TEST_INPUT)
    assert puzzle.solve_part_one() == 50


def test_part_one():
    puzzle = Puzzle(input)
    assert puzzle.solve_part_one() == 4777409595


def test_part_two_example():
    puzzle = Puzzle(TEST_INPUT)
    assert puzzle.solve_part_two() == 24


def test_part_two():
    puzzle = Puzzle(input)
    assert puzzle.solve_part_two() == 999999999999999