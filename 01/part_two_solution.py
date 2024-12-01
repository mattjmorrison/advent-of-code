from data import input
from puzzle import Puzzle


def part_two() -> int:
    puzzle = Puzzle(input)
    return puzzle.similarity_sum