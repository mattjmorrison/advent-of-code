import pytest
from data import DATA
from puzzle import Puzzle


EXAMPLE = """
2333133121414131402
""".strip()


def test_example() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.blocks == list(
        "00...111...2...333.44.5555.6666.777.888899"
    )


def test_defrag() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert ''.join(puzzle.defrag()).startswith(
        "0099811188827773336446555566"
    )


def test_checksum() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.get_checksum() == 1928


def test_part_one() -> None:
    puzzle = Puzzle(DATA)
    print(puzzle.defrag())
    # print(puzzle.get_checksum())

    # Part 1
    # 6_216_544_403_458


def test_part_two() -> None:
    puzzle = Puzzle(DATA)
    print(puzzle.defrag())
    # Part 2
    # 6_237_075_041_489

