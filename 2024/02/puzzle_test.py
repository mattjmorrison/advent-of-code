import pytest
from part_one_solution import part_one
from part_two_solution import part_two
from puzzle import Puzzle


def test_example() -> None:
    data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
    puzzle = Puzzle(data)
    assert puzzle.count_safe() == 2


@pytest.mark.parametrize("scenario, answer", (
    ([7, 6, 4, 2, 1], True),
    ([1, 2, 7, 8, 9], False),
    ([9, 7, 6, 2, 1], False),
    ([1, 3, 2, 4, 5], False),
    ([8, 6, 4, 4, 1], False),
    ([1, 3, 6, 7, 9], True),
))
def test_is_safe(scenario: list[int], answer: bool) -> None:
    puzzle = Puzzle("")
    assert puzzle.is_safe(scenario) == answer


@pytest.mark.parametrize("scenario, answer", (
    ([7, 6, 4, 2, 1], True),
    ([1, 2, 7, 8, 9], False),
    ([9, 7, 6, 2, 1], False),
    ([1, 3, 2, 4, 5], True),
    ([8, 6, 4, 4, 1], True),
    ([1, 3, 6, 7, 9], True),
    ([0, 1, 5, 9, 9], False),
    ([0, 0, 0, 0, 0], False),
    ([0, 1, 0, 1, 0], False),
    ([0, 0, 1, 2, 3], True),
    ([9, 9, 8, 7, 6], True),
    ([81, 83, 86, 88, 89], True),
    ([86, 83, 81, 80, 77, 74], True),
    ([15, 15, 17, 19, 21, 22, 24, 28], False),
    ([0, 5, 7, 9, 11], True),
    ([5, 0, 6, 7, 9, 11], True),
    ([1, 2, 3, 4, 0], True),
    ([1, 2, 3, 0, 4], True),  # 17
    ([1, 2, 0, 3, 4], True),  # 18
    ([1, 0, 2, 3, 4], True),  # 19
    ([0, 1, 2, 3, 4], True),
))
def test_is_safe_two(scenario: list[int], answer: bool) -> None:
    puzzle = Puzzle("")
    assert puzzle.is_safe_two(scenario) == answer


@pytest.mark.parametrize("scenario, answer", (
    ([7, 6, 4, 2, 1], [-1, -2, -2, -1]),
    ([1, 2, 3, 4, 0], [1, 1, 1, -4]),
    ([1, 2, 3, 0, 4], [1, 1, -3, 4]),
    ([1, 2, 0, 3, 4], [1, -2, 3, 1]),
    ([1, 0, 2, 3, 4], [-1, 2, 1, 1]),
    ([0, 1, 2, 3, 4], [1, 1, 1, 1]),
    ([0, 4, 5, 6, 7], [4, 1, 1, 1]),
))
def test_ranks_each(scenario: list[int], answer: list[int]) -> None:
    puzzle = Puzzle("")
    assert puzzle.rank(scenario) == answer


@pytest.mark.parametrize("scenario, answer", (
    ([7, 6, 4, 2, 1], [7, 6, 4, 2, 1]),
    ([1, 2, 3, 4, 0], [1, 2, 3, 4]),
    ([1, 2, 3, 0, 4], [1, 2, 3, 4]),
    ([1, 2, 0, 3, 4], [1, 2, 3, 4]),
    ([1, 0, 2, 3, 4], [0, 2, 3, 4]),
    ([0, 1, 2, 3, 4], [0, 1, 2, 3, 4]),
    ([0, 4, 5, 6, 7], [4, 5, 6, 7]),
))
def test_find_good_rank(scenario: list[int], answer: list[int]) -> None:
    puzzle = Puzzle("")
    assert puzzle.find_good_rank(scenario) == answer


@pytest.mark.parametrize("scenario, answer", (
    ([-1, -2, -2, -1], True),
    ([1, 1, 1, -4], False),
    ([1, 1, -3, 4], False),
    ([1, -2, 3, 1], False),
    ([-1, 2, 1, 1], False),
    ([1, 1, 1, 1], True),
    ([4, 1, 1, 1], False),
))
def test_good_rank(scenario: list[int], answer: bool) -> None:
    puzzle = Puzzle("")
    assert puzzle.is_good_rank(scenario) == answer


def test_solution_one() -> None:
    assert part_one() == 680


def test_solution_two() -> None:
    assert part_two() == 710
