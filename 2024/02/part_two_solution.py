from data import DATA
from puzzle import Puzzle


def part_two() -> int:
    puzzle = Puzzle(DATA)
    return puzzle.count_safe_two()
