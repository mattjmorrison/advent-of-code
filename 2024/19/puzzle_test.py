import pytest

from puzzle import Puzzle
from data import DATA


EXAMPLE = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
""".strip()


def test_part_one() -> None:
    p = Puzzle(DATA)
    assert p.part_one(p.desired) == 311


def test_part_two() -> None:
    p = Puzzle(DATA)
    assert p.part_two(p.desired) == 616_234_236_468_263


# def test_parse_available_towels() -> None:
#     puzzle = Puzzle(EXAMPLE)
#     assert puzzle.available == [
#         'r',
#         'wr',
#         'b',
#         'g',
#         'bwu',
#         'rb',
#         'gb',
#         'br'
#     ]


# def test_parse_desired_towels() -> None:
#     puzzle = Puzzle(EXAMPLE)
#     assert puzzle.desired == [
#         'brwrr',
#         'bggr',
#         'gbbr',
#         'rrbgbr',
#         'ubwu',
#         'bwurrg',
#         'brgr',
#         'bbrgwb',
#     ]


# def test_example() -> None:
#     puzzle = Puzzle(EXAMPLE)
#     assert puzzle.answer == 6  # should be 6 for example


# @pytest.mark.parametrize('start, result', (
#         ('abcde', 'bcde'),
#         ('bcde', 'cde'),
#         ('cde', 'de'),
#         ('de', 'e'),
#         ('e', '')
# ))
# def test_match(start: str, result: str) -> None:
#     data = """
# a, b, c, d, e

# abcde
# """.strip()
#     puzzle = Puzzle(data)
#     assert puzzle.match(start, puzzle.available) == result


# @pytest.mark.parametrize('start, result', (
#     ('abcde', True),
#     ('abaaaa', True),
# ))
# def test_arrange(start: str, result: bool) -> None:
#     data = """
# a, b, c, d, e

# abcde
# """.strip()
#     puzzle = Puzzle(data)
#     assert puzzle.arrange(start) is result


# def test_arrange_2() -> None:
#     data = """
# a, c, abaaaa

# abaaaaa
# """.strip()
#     puzzle = Puzzle(data)
#     assert puzzle.arrange('abaaaaa') is True


# def test_arrange_3() -> None:
#     data = """
# a, ac, b, abaaaa

# abaaaac
# """.strip()
#     puzzle = Puzzle(data)
#     assert puzzle.arrange('abaaaac') is True


# def test_no_match() -> None:
#     data = """
# a, b, c, d, e

# zyxw
# """.strip()
#     puzzle = Puzzle(data)
#     assert puzzle.match('zyxw', puzzle.available) == 'zyxw'
