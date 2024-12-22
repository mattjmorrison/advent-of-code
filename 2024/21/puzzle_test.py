from puzzle import Puzzle, Terminal, NUMBERS, ARROWS
from data import DATA


EXAMPLE = """
029A
980A
179A
456A
379A
""".strip()


def test_part_one() -> None:
    puzzle = Puzzle(DATA)
    assert puzzle.answer == 107934


def test_example() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.answer == 126384


#
# NumPad Tests
#


def test_password_pad_coords() -> None:
    pad = Terminal(NUMBERS)
    assert pad.coords == {
        '7': (0, 0),
        '8': (0, 1),
        '9': (0, 2),
        '4': (1, 0),
        '5': (1, 1),
        '6': (1, 2),
        '1': (2, 0),
        '2': (2, 1),
        '3': (2, 2),
        '0': (3, 1),
        'A': (3, 2),
    }


def test_numpad_dirs() -> None:
    pad = Terminal(NUMBERS)
    assert pad.get_neighbors(1, 1) == [
        (0, 1, "^"),
        (2, 1, "v"),
        (1, 0, "<"),
        (1, 2, ">"),
    ]


def test_numpad_neighbors_excludes_out_of_bounds_neg() -> None:
    pad = Terminal(NUMBERS)
    assert pad.get_neighbors(0, 0) == [
        (1, 0, 'v'),
        (0, 1, '>'),
    ]


def test_numpad_neighbors_excludes_out_of_bounds_pos() -> None:
    pad = Terminal(NUMBERS)
    assert pad.get_neighbors(3, 2) == [
        (2, 2, '^'),
        (3, 1, '<')
    ]


def test_numpad_neighbors_skips_blank() -> None:
    pad = Terminal(NUMBERS)
    assert pad.get_neighbors(3, 1) == [
        (2, 1, '^'),
        (3, 2, '>'),
    ]


def test_paths() -> None:
    pad = Terminal(NUMBERS)
    assert pad.paths[('8', '3')] == [
        'vv>A',  'v>vA', '>vvA',
    ]
    assert pad.paths[('A', '7')] == [
        '^^^<<A',
        '^^<^<A',
        '^^<<^A',
        '^<^^<A',
        '^<^<^A',
        '^<<^^A',
        '<^^^<A',
        '<^^<^A',
        '<^<^^A',
    ]


def test_terminal_with_number_pad() -> None:
    pad = Terminal(NUMBERS)
    assert pad.exec_cmd('029A') == [
        '<A^A^^>AvvvA',
        '<A^A^>^AvvvA',
        '<A^A>^^AvvvA',
    ]


def test_terminal_with_arrow_pad() -> None:
    pad = Terminal(ARROWS)
    assert pad.exec_cmd('<v^>A') == [
        'v<<A>A^Av>A^A',
        'v<<A>A^A>vA^A',
        '<v<A>A^Av>A^A',
        '<v<A>A^A>vA^A',
    ]
