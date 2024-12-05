import pytest
from part_one_solution import part_one
from part_two_solution import part_two
from puzzle import Puzzle


def test_example_two() -> None:
    data = """.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
.........."""
    puzzle = Puzzle(data)
    assert puzzle.answer_two == 9


# @pytest.mark.skip("Wait")
def test_example() -> None:
    data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
    puzzle = Puzzle(data)
    assert puzzle.answer == 18


def test_find_horizonal() -> None:
    data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
    puzzle = Puzzle(data)
    assert puzzle.horizonal == 5


def test_find_vertical() -> None:
    data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
    puzzle = Puzzle(data)
    assert puzzle.vertical == 3


def test_find_diagonal() -> None:
    data = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".strip()
    puzzle = Puzzle(data)
    assert puzzle.diagonal == 10


def test_transpose():
    puzzle = Puzzle("")
    assert puzzle.transpose([
        "abcdefg",
        "hijklmn"
    ]) == [
        "ah",
        "bi",
        "cj",
        "dk",
        "el",
        "fm",
        "gn"
    ]


def test_tl_br_transpose() -> None:
    puzzle = Puzzle("")
    assert puzzle.tlbr_transpose([
        "abcd15",
        "efgh26",
        "ijkl37",
        "mnop48",
        "qrstuv",
    ]) == ["afkp", "bgl4", "ch38", "ejot", "fkpu", "gl4v"]


@pytest.mark.skip("not right")
def test_tr_bl_transpose() -> None:
    puzzle = Puzzle("")
    assert puzzle.trbl_transpose([
        "abcd15",
        "efgh26",
        "ijkl37",
        "mnop48",
        "qrstuv",
    ]) == ["52lo", "1hkn", "dgjm", "63ps", "2lor", "hknq"]


def test_part_one() -> None:
    assert part_one() == 2462


def test_part_two() -> None:
    assert part_two() == "Two"


@pytest.mark.parametrize("scenario, answer", (
    ([
        ['s', '.', 'm',],
        ['.', 'a', '.',],
        ['s', '.', 'm',],
    ], True),
    ([
        ['m', '.', 's',],
        ['.', 'a', '.',],
        ['m', '.', 's',],
    ], True),
    ([
        ['s', '.', 's',],
        ['.', 'a', '.',],
        ['m', '.', 'm',],
    ], True),
    ([
        ['m', '.', 'm',],
        ['.', 'a', '.',],
        ['s', '.', 's',],
    ], True),
    ([
        ['m', '.', '.',],
        ['.', 'a', '.',],
        ['.', '.', 's',],
    ], False),
    ([
        ['s', '.', '.',],
        ['.', 'a', '.',],
        ['.', '.', 'm',],
    ], False),
    ([
        ['.', '.', 's',],
        ['.', 'a', '.',],
        ['m', '.', '.',],
    ], False),
    ([
        ['m', 'a', 's',],
        ['.', '.', '.',],
        ['.', '.', '.',],
    ], False),
))
def test_spot_mas(scenario, answer) -> None:
    puzzle = Puzzle("")
    assert puzzle.is_x_mas(scenario) == answer


def test_convert_to_grid() -> None:
    data = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".strip()
    puzzle = Puzzle(data)
    assert puzzle.get_grid() == [
        ['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'],
        ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'],
        ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'],
        ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'],
        ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'],
        ['X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'],
        ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'],
        ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'],
        ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'],
        ['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X'],
    ]

def test_get_3_x_3() -> None:
    data = """
    MMMSXXMASM
    MSAMXMSMSA
    AMXSXMAAMM
    MSAMASMSMX
    XMASAMXAMM
    XXAMMXXAMA
    SMSMSASXSS
    SAXAMASAAA
    MAMMMXMMMM
    MXMXAXMASX""".strip()
    puzzle = Puzzle(data)
    assert puzzle.get_3_x_3(0, 0) == [
        ['M', 'M', 'M'],
        ['M', 'S', 'A'],
        ['A', 'M', 'X']
    ]

def test_create_3x3_grids() -> None:
    data = """
    MMMSXXMASM
    MSAMXMSMSA
    AMXSXMAAMM
    MSAMASMSMX
    XMASAMXAMM
    XXAMMXXAMA
    SMSMSASXSS
    SAXAMASAAA
    MAMMMXMMMM
    MXMXAXMASX""".strip()
    puzzle = Puzzle(data)
    grids = puzzle.get_grids()
    assert len(grids) == 64