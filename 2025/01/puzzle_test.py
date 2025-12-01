
from textwrap import dedent

import pytest

from puzzle import Puzzle
from data import input_data


def test_splits_input() -> None:
    input = dedent(dedent("""
        L1
        R1
        L2
        R2
    """))
    puzzle = Puzzle(input)
    assert puzzle.get_moves() == [
        -1, 1, -2, 2
    ]


def test_splits_apart_numbers_from_input() -> None:
    input = dedent("""
        L68
        L30
        R48
        L5
        R60
        L55
        L1
        L99
        R14
        L82
    """.strip())
    puzzle = Puzzle(input)
    puzzle.solve()
    assert puzzle.zeroes == 3

# def test_two():
#     input = dedent("""
#         L454
#     """.strip())
#     puzzle = Puzzle(input)
#     puzzle.solve()
#     assert False


def test_part_one():
    puzzle = Puzzle(input_data)
    puzzle.solve()
    # assert puzzle.zeroes == 
    assert puzzle.zeroes == 1150


def test_looper():
    puzzle = Puzzle("")
    assert puzzle.find_spot(-51) == 49
    assert puzzle.find_spot(-100) == 0
    assert puzzle.find_spot(-150) == 50
    assert puzzle.find_spot(-200) == 0
    assert puzzle.find_spot(50) == 50
    assert puzzle.find_spot(100) == 0
    assert puzzle.find_spot(150) == 50
    assert puzzle.find_spot(200) == 0

