
from textwrap import dedent

import pytest

from puzzle import Puzzle
from data import input_data


def test_starting_position():
    puzzle = Puzzle("")
    assert puzzle.position == 50


@pytest.mark.parametrize('move, result', (
    ('R1', 51),
    ('L1', 49),
    ('R50', 0),
    ('L50', 0),
    ('L51', 99),
    ('R51', 1),
    ('L52', 98),
    ('R100', 50),
    ('R150', 0),
    ('L100', 50),
    ('L150', 0),
    ('R200', 50),
    ('L200', 50),
))
def test_move(move, result):
    puzzle = Puzzle("")
    puzzle.move(move)
    assert puzzle.position == result


def test_zeroes_counts():
    puzzle = Puzzle("")
    assert puzzle.zeroes == 0
    puzzle.move('R1000')
    assert puzzle.zeroes == 10


def test_part_two_example():
    puzzle = Puzzle(dedent("""
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
    """).strip())
    puzzle.solve()
    assert puzzle.zeroes == 6


def test_part_two():
    puzzle = Puzzle(input_data)
    puzzle.solve()
    assert puzzle.zeroes == 6738
