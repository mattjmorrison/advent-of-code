import pytest
from data import DATA
from puzzle import Puzzle, Stone


EXAMPLE = "125 17"


"""
idea, have a cache, keyed by the integer with a value of the children.. then have a separate list that maintains the order and uses the id of
the cached object, so no objects are duplicated
"""

@pytest.mark.parametrize('starting, blinks, answer', (
    ("0", 10, 39),
    ("1", 10, 62),
    ("2", 10, 57),
    ("4", 10, 47),
    ("6", 10, 54),
    ("8", 10, 48),
    ("9", 10, 54),
    ("20", 10, 50),
    ("24", 10, 60),
    ("26", 10, 62),
    ("80", 10, 51),
    ("96", 10, 64),
    ("2024", 10, 81),
    ("2608", 10, 72),
    ("3277", 10, 89),
    ("3686", 10, 92),
    ("4048", 10, 92),
    ("8096", 10, 82),
    ("9184", 10, 91),
    ("16192", 10, 69),
    ("18216", 10, 70),
    ("32772608", 10, 103),
    ("36869184", 10, 103),
))
def test_simple_scenarios(starting: str, blinks: int, answer: int) -> None:
    puzzle = Puzzle(starting)
    assert puzzle.answer(blinks) == answer


def test_x() -> None:
    puzzle = Puzzle("0")
    puzzle.blink()
    assert puzzle.state == [Stone(1)]
    puzzle.blink()
    assert puzzle.state == [Stone(2024)]
    puzzle.blink()
    assert puzzle.state == [Stone(20), Stone(24)]
    puzzle.blink()
    assert puzzle.state == [Stone(2), Stone(0), Stone(2), Stone(4)]
    puzzle.blink()
    assert puzzle.state == [Stone(4048), Stone(1), Stone(4048), Stone(8096)]
    puzzle.blink()
    assert puzzle.state == [Stone(40), Stone(48), Stone(2024), Stone(40), Stone(48), Stone(80), Stone(96)]
    puzzle.blink()
    assert puzzle.state == [
        Stone(4), Stone(0), Stone(4), Stone(8), Stone(20), Stone(24), Stone(4),
        Stone(0), Stone(4), Stone(8), Stone(8), Stone(0), Stone(9), Stone(6)
    ]
    puzzle.blink()
    assert puzzle.state == [
        Stone(8096), Stone(1), Stone(8096), Stone(16192), Stone(2), Stone(0), Stone(2),
        Stone(4), Stone(8096), Stone(1), Stone(8096), Stone(16192), Stone(16192), Stone(1), Stone(18216), Stone(12144)
    ]
    puzzle.blink()
    assert puzzle.state == [
        Stone(80), Stone(96), Stone(2024), Stone(80), Stone(96), Stone(32_772_608), Stone(4048), Stone(1), Stone(4048),
        Stone(8096), Stone(80), Stone(96), Stone(2024), Stone(80), Stone(96), Stone(32_772_608), Stone(32_772_608), Stone(2024), 
        Stone(36_869_184), Stone(24_579_456)
    ]
    puzzle.blink()
    assert puzzle.state == [
        Stone(8), Stone(0), Stone(9), Stone(6), Stone(20), Stone(24), Stone(8), Stone(0), Stone(9), Stone(6), Stone(3277), Stone(2608), 
        Stone(40), Stone(48), Stone(2024), Stone(40), Stone(48), Stone(80), Stone(96), Stone(8), Stone(0), Stone(9), Stone(6), Stone(20),
        Stone(24), Stone(8), Stone(0), Stone(9), Stone(6), Stone(3277), Stone(2608), Stone(3277), Stone(2608), Stone(20), Stone(24), 
        Stone(3686), Stone(9184), Stone(2457), Stone(9456)
    ]
    assert len(puzzle.state) == 39  # after 10 blinks


def test_part_two() -> None:
    puzzle = Puzzle(DATA)
    assert puzzle.answer(40) == 110_194_241
    # 103.74s call     puzzle_test.py::test_part_two (40)


def test_part_one() -> None:
    puzzle = Puzzle(DATA)
    assert puzzle.answer(25) == 209_412


def test_example() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.answer(25) == 55_312


def test_puzzle_blink() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.state == [
        Stone(125),
        Stone(17),
    ]
    puzzle.blink()
    assert puzzle.state == [
        Stone(253000),
        Stone(1),
        Stone(7)
    ]
    puzzle.blink()
    assert puzzle.state == [
        Stone(253),
        Stone(0),
        Stone(2024),
        Stone(14168),
    ]
    puzzle.blink()
    assert puzzle.state == [
        Stone(512072),
        Stone(1),
        Stone(20),
        Stone(24),
        Stone(28676032),
    ]
    puzzle.blink()
    assert puzzle.state == [
        Stone(512),
        Stone(72),
        Stone(2024),
        Stone(2),
        Stone(0),
        Stone(2),
        Stone(4),
        Stone(2867),
        Stone(6032),
    ]
    puzzle.blink()
    assert puzzle.state == [
        Stone(1036288),
        Stone(7),
        Stone(2),
        Stone(20),
        Stone(24),
        Stone(4048),
        Stone(1),
        Stone(4048),
        Stone(8096),
        Stone(28),
        Stone(67),
        Stone(60),
        Stone(32),
    ]
    puzzle.blink()
    assert puzzle.state == [
        Stone(2097446912),
        Stone(14168),
        Stone(4048),
        Stone(2),
        Stone(0),
        Stone(2),
        Stone(4),
        Stone(40),
        Stone(48),
        Stone(2024),
        Stone(40),
        Stone(48),
        Stone(80),
        Stone(96),
        Stone(2),
        Stone(8),
        Stone(6),
        Stone(7),
        Stone(6),
        Stone(0),
        Stone(3),
        Stone(2),
    ]


#
# Stone Tests
#


@pytest.mark.parametrize('number, results', (
    (0, [1]),
    (1, [2024]),
    (10, [1, 0]),
    (101, [204_424]),
))
def test_blink(number: int, results: list[int]) -> None:
    stone = Stone(number)
    new_stones = stone.blink()
    assert results == [n.number for n in new_stones]


@pytest.mark.parametrize('number, result', (
    (1, False),
    (10, True),
    (123, False),
    (1000, True),
    (12345, False),
    (123456, True),
    (1234567, False),
    (12345678, True),
))
def test_is_even(number: int, result: bool) -> None:
    assert Stone(number).is_even == result


@pytest.mark.parametrize('number, numbers', (
    (10, [1, 0]),
    (1, [1]),
    (100, [100]),
    (100001, [100, 1])
))
def test_even_digits_split(
    number: int, numbers: list[int]
) -> None:
    stone = Stone(number)
    new_stones = stone.split()
    assert numbers == [s.number for s in new_stones]


def test_stones_with_same_number_are_same() -> None:
    one = Stone(1)
    two = Stone(1)
    assert one == two


def test_stone_str_and_repr() -> None:
    one = Stone(1)
    assert str(one) == repr(one) == str(one.number)


def test_stone_is_hashed_by_number() -> None:
    one = Stone(1)
    assert hash(one) == 1
