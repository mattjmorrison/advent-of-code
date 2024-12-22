from puzzle import Puzzle, NumPad


EXAMPLE = ""


def test_example() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.answer == 0


#
# NumPad Tests
#


def test_password_pad_coords() -> None:
    pad = NumPad()
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
    pad = NumPad()
    assert pad.get_neighbors(1, 1) == [
        (0, 1, "^"),
        (2, 1, "v"),
        (1, 0, "<"),
        (1, 2, ">"),
    ]


def test_numpad_neighbors_excludes_out_of_bounds_neg() -> None:
    pad = NumPad()
    assert pad.get_neighbors(0, 0) == [
        (1, 0, 'v'),
        (0, 1, '>'),
    ]


def test_numpad_neighbors_excludes_out_of_bounds_pos() -> None:
    pad = NumPad()
    assert pad.get_neighbors(3, 2) == [
        (2, 2, '^'),
        (3, 1, '<')
    ]


def test_numpad_neighbors_skips_blank() -> None:
    pad = NumPad()
    assert pad.get_neighbors(3, 1) == [
        (2, 1, '^'),
        (3, 2, '>'),
    ]


def test_paths() -> None:
    pad = NumPad()
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


def test_exec_cmd() -> None:
    pad = NumPad()
    assert pad.exec_cmd('029A') == [
        '<A^A^^>AvvvA',
        '<A^A^>^AvvvA',
        '<A^A>^^AvvvA',
    ]
