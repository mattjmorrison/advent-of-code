from puzzle import Puzzle
from textwrap import dedent
import pytest
from data import input

def test_example_part_one():
    input = dedent("""
        123 328  51 64 
         45 64  387 23 
          6 98  215 314
        *   +   *   +  
    """).strip()

    puzzle = Puzzle(input)
    assert puzzle.parse() == [
        (123, 45, 6, '*'),
        (328, 64, 98, '+'),
        (51, 387, 215, '*'),
        (64, 23, 314, '+'),
    ]

@pytest.mark.parametrize('row, result', [
    [(123, 45, 6, '*'), 33210],
    [(328, 64, 98, '+'), 490],
    [(51, 387, 215, '*'), 4243455],
    [(64, 23, 314, '+'), 401],
])
def test_calc_row(row, result):
    puzzle = Puzzle(input)
    assert puzzle.calc_row(row) == result

def test_example_one():
    input = dedent("""
        123 328  51 64 
         45 64  387 23 
          6 98  215 314
        *   +   *   +  
    """).strip()
    puzzle = Puzzle(input)
    assert puzzle.solve_part_one() == 4277556

def test_example_two():
    input = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """[1:]
    puzzle = Puzzle(input)
    assert puzzle.solve_part_two() == 3263827


def test_example_two_parse():
    input = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """.lstrip()
    puzzle = Puzzle(input)
    results = puzzle.parse_two()
    assert results == [
        [4, 431, 623, '+'],
        [175, 581, 32, '*'],
        [8, 248, 369, '+'],
        [356, 24, 1, '*'],
    ]


def test_part_one():
    puzzle = Puzzle(input)
    assert puzzle.solve_part_one() == 3525371263915


def test_part_two():
    puzzle = Puzzle(input)
    assert puzzle.solve_part_two() == 3525371263915
