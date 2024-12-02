from puzzle import Puzzle
from data import DATA


def part_one() -> int:
    puzzle = Puzzle(DATA)
    return puzzle.count_safe()
