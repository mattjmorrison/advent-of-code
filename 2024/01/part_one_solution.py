from puzzle import Puzzle
from data import input


def part_one() -> int:
    puzzle = Puzzle(input)
    return puzzle.diffs_sum