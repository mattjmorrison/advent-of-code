
import pytest
from puzzle import Puzzle
from part_one_solution import part_one
from part_two_solution import part_two


def test_splits_apart_numbers_from_input() -> None:
    input = """3   4
4   3
2   5
1   3
3   9
3   3"""
    puzzle = Puzzle(input)
    assert tuple(puzzle.number_sets) == (
        (1, 3),
        (2, 3),
        (3, 3),
        (3, 4),
        (3, 5),
        (4, 9),
    )


@pytest.mark.parametrize('input, answer', (
    ("1  1", (0, )),
    ("1  2", (1, )),
    ("2  1", (1, )),
    ("""1  1
1  2
2  1""", (0, 0, 0)),
    ("""0  1
0  2
0  3""", (1, 2, 3))
))
def test_calculates_differences_for_each(input: str, answer: tuple[int]) -> None:
    puzzle = Puzzle(input)
    assert tuple(puzzle.number_diffs) == answer


@pytest.mark.parametrize('input, answer', (
    ("1  1", 0),
    ("2  1", 1),
    ("""3   4
4   3
2   5
1   3
3   9
3   3""", 11)
))
def test_adds_diffs(input: str, answer: int) -> None:
    puzzle = Puzzle(input)
    assert puzzle.diffs_sum == answer


@pytest.mark.parametrize('input, answer', (
    ("1  1", (1, )),
    ("""1  1
0  1
2  1
3  1""", (4, 0, 0, 0)),
    ("""9  9
0  9
1  9
2  9""", (36, 0, 0, 0)),
    )
)
def test_similarity_scores(input: str, answer: tuple[int]) -> None:
    puzzle = Puzzle(input)
    assert tuple(puzzle.similarity_scores) == answer


def test_sums_similarity_scores() -> None:
    input = """3   4
4   3
2   5
1   3
3   9
3   3"""
    puzzle = Puzzle(input)
    assert puzzle.similarity_sum == 31


def test_part_one_solution() -> None:
    assert part_one() == 2057374


def test_part_two_solution() -> None:
    assert part_two() == 23177084
