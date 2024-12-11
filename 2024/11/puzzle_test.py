import pytest
from data import DATA
from puzzle import Puzzle, Stone


EXAMPLE = "125 17"


@pytest.mark.parametrize('starting, blinks, answer', (
    ("0", 10, 39),
    ("1", 10, 62),
    ("2", 10, 57),
    ("4", 10, 47),
    ("6", 10, 54),
    ("8", 10, 48),
    ("9", 10, 54),
))
def test_simple_scenarios(starting: str, blinks: int, answer: int) -> None:
    puzzle = Puzzle(starting)
    assert puzzle.answer(blinks) == answer


def test_part_two() -> None:
    puzzle = Puzzle(DATA)
    assert puzzle.answer(75) == 248967696501656


def test_part_one() -> None:
    puzzle = Puzzle(DATA)
    assert puzzle.answer(25) == 209_412


def test_example() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.answer(25) == 55_312


def test_puzzle_blink() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.counter == {
        Stone(125): 1,
        Stone(17): 1,
    }
    puzzle.blink()
    assert puzzle.counter == {
        Stone(253000): 1,
        Stone(1): 1,
        Stone(7): 1
    }
    puzzle.blink()
    assert puzzle.counter == {
        Stone(253): 1,
        Stone(0): 1,
        Stone(2024): 1,
        Stone(14168): 1,
    }
    puzzle.blink()
    assert puzzle.counter == {
        Stone(512072): 1,
        Stone(1): 1,
        Stone(20): 1,
        Stone(24): 1,
        Stone(28676032): 1,
    }
    puzzle.blink()
    assert puzzle.counter == {
        Stone(512): 1,
        Stone(72): 1,
        Stone(2024): 1,
        Stone(0): 1,
        Stone(2): 2,
        Stone(4): 1,
        Stone(2867): 1,
        Stone(6032): 1,
    }
    puzzle.blink()
    assert puzzle.counter == {
        Stone(1036288): 1,
        Stone(7): 1,
        Stone(2): 1,
        Stone(20): 1,
        Stone(24): 1,
        Stone(1): 1,
        Stone(4048): 2,
        Stone(8096): 1,
        Stone(28): 1,
        Stone(67): 1,
        Stone(60): 1,
        Stone(32): 1,
    }
    puzzle.blink()
    assert puzzle.counter == {
        Stone(2097446912): 1,
        Stone(14168): 1,
        Stone(4048): 1,
        Stone(2): 4,
        Stone(0): 2,
        Stone(4): 1,
        Stone(40): 2,
        Stone(48): 2,
        Stone(2024): 1,
        Stone(80): 1,
        Stone(96): 1,
        Stone(8): 1,
        Stone(6): 2,
        Stone(7): 1,
        Stone(3): 1,
    }


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
