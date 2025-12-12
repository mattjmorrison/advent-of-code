from textwrap import dedent
from puzzle import Puzzle, Present, Region
from data import input


TEST_INPUT = """
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
""".strip()


def test_region_parse():
    region = Region('4x4: 0 0 0 0 2 0')
    assert region.area == 16


def test_parse_presents():
    puzzle = Puzzle(TEST_INPUT)
    puzzle.parse()
    assert len(puzzle.presents) == 6


def test_parse_regions():
    puzzle = Puzzle(TEST_INPUT)
    puzzle.parse()
    assert len(puzzle.regions) == 3


# def test_present_rotation():
#     present = Present (['#..', '#..', '#..'])
#     assert present.rotate().strip() == dedent("""
#     ###
#     ...
#     ...
#     """).strip()


def test_present_area():
    puzzle = Puzzle(TEST_INPUT)
    puzzle.parse()
    assert puzzle.presents[0].area == 7


"""
[
    ['#', '.', '.'],
    ['#', '.', '.'],
    ['#', '.', '.'],
]
(0, 0),
(0, 1),
(0, 2),


90 degree clockwise
[
    ['#', '#', '#'],
    ['.', '.', '.'],
    ['.', '.', '.'],
]
(0, 0),
(1, 0),
(2, 0),

(0, 0) -> +2, +0 -> (2, 0)
(0, 1) -> +1, -1 -> (1, 0)
(0, 2) -> +0, -2 -> (0, 0)


180 degree flip
[
    ['.', '.', '#'],
    ['.', '.', '#'],
    ['.', '.', '#'],
]

(0, 0) -> +2, 0 ->  (2, 0)
(0, 1) -> +2, 0 ->  (2, 1)
(0, 2) -> +2, 0 ->  (2, 2)


90 degree counterclockwise
[
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['#', '#', '#'],
]
(0, 2) -> +0, +2
(1, 2) -> +1, +1
(2, 2) -> +2, +0
"""

