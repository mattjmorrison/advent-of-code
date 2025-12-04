from textwrap import dedent
from puzzle import Puzzle
import pytest
from data import input

# def test_parse():
#     input = dedent("""
#         987654321111111
#         811111111111119
#         234234234234278
#         818181911112111
#     """).strip()

    # puzzle = Puzzle(input)
    # assert puzzle.parse() == [
    #     [9,8,7,6,5,4,3,2,1,1,1,1,1,1,1],
    #     [8,1,1,1,1,1,1,1,1,1,1,1,1,1,9],
    #     [2,3,4,2,3,4,2,3,4,2,3,4,2,7,8],
    #     [8,1,8,1,8,1,9,1,1,1,1,2,1,1,1],
    # ]


# @pytest.mark.parametrize('row, number', (
#     ([9,8,7,6,5,4,3,2,1,1,1,1,1,1,1], 9),
#     ([8,1,1,1,1,1,1,1,1,1,1,1,1,1,9], 8),
#     ([2,3,4,2,3,4,2,3,4,2,3,4,2,7,8], 7),
#     ([8,1,8,1,8,1,9,1,1,1,1,2,1,1,1], 9),
# ))
# def test_find_max_in_row(row, number):
#     puzzle = Puzzle("")
#     assert puzzle.find_max(row) == number


# @pytest.mark.parametrize('row, number', (
#     ([9,8,7,6,5,4,3,2,1,1,1,1,1,1,1], 0),
#     ([8,1,1,1,1,1,1,1,1,1,1,1,1,1,9], 0),
#     ([2,3,4,2,3,4,2,3,4,2,3,4,2,7,8], 13),
#     ([8,1,8,1,8,1,9,1,1,1,1,2,1,1,1], 6),
# ))
# def test_find_position_of_max(row, number):
#     puzzle = Puzzle("")
#     assert puzzle.find_max_pos(row) == number


# @pytest.mark.parametrize('row, number', (
#     ([9,8,7,6,5,4,3,2,1,1,1,1,1,1,1], 8),
#     ([8,1,1,1,1,1,1,1,1,1,1,1,1,1,9], 9),
#     ([2,3,4,2,3,4,2,3,4,2,3,4,2,7,8], 8),
#     ([8,1,8,1,8,1,9,1,1,1,1,2,1,1,1], 2),
# ))
# def test_find_max_after_max(row, number):
#     puzzle = Puzzle("")
#     assert puzzle.find_max_after_max(row) == number


# @pytest.mark.parametrize('row, number', (
#     ([9,8,7,6,5,4,3,2,1,1,1,1,1,1,1], 98),
#     ([8,1,1,1,1,1,1,1,1,1,1,1,1,1,9], 89),
#     ([2,3,4,2,3,4,2,3,4,2,3,4,2,7,8], 78),
#     ([8,1,8,1,8,1,9,1,1,1,1,2,1,1,1], 92),
# ))
# def test_get_joltage_for_row(row, number):
#     puzzle = Puzzle("")
#     assert puzzle.calc_joltage_for_row(row) == number


@pytest.mark.parametrize('data, result', (
    ("987654321111111", 987654321111),
    ("811111111111119", 811111111119),
    ("234234234234278", 434234234278),
    ("818181911112111", 888911112111),
))
def test_part_two_line_one_example(data, result):
    puzzle = Puzzle(data)
    assert puzzle.calc_total_joltage() == result


def test_calc_total_joltage():
    input = dedent("""
        987654321111111
        811111111111119
        234234234234278
        818181911112111
    """).strip()
    puzzle = Puzzle(input)
    # assert puzzle.calc_total_joltage() == 357
    assert puzzle.calc_total_joltage() == 3121910778619


# def test_part_one():
#     puzzle = Puzzle(input)
#     assert puzzle.calc_total_joltage() == 17443


def test_part_two():
    puzzle = Puzzle(input)
    assert puzzle.calc_total_joltage() == 172167155440541
