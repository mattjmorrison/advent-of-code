from textwrap import dedent
from puzzle import Puzzle
from data import input


TEST_INPUT = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
""".strip()

def test_parse():
    puzzle = Puzzle(TEST_INPUT)
    data = puzzle.parse()
    assert data == {
        "aaa": ["you",  "hhh"],
        "you": ["bbb",  "ccc"],
        "bbb": ["ddd",  "eee"],
        "ccc": ["ddd",  "eee", "fff"],
        "ddd": ["ggg"],
        "eee": ["out"],
        "fff": ["out"],
        "ggg": ["out"],
        "hhh": ["ccc", "fff", "iii"],
        "iii": ["out"],
    }


def test_solve_part_one_example():
    puzzle = Puzzle(TEST_INPUT)
    assert puzzle.solve_part_one() == 5


def test_solve_part_one():
    puzzle = Puzzle(input)
    assert puzzle.solve_part_one() == 683


def test_solve_part_two_example():
    data = dedent("""
        svr: aaa bbb
        aaa: fft
        fft: ccc
        bbb: tty
        tty: ccc
        ccc: ddd eee
        ddd: hub
        hub: fff
        eee: dac
        dac: fff
        fff: ggg hhh
        ggg: out
        hhh: out
    """).strip()
    puzzle = Puzzle(data)
    assert puzzle.solve_part_two() == 2

def test_solve_part_two():
    puzzle = Puzzle(input)
    assert puzzle.solve_part_two() == 0
