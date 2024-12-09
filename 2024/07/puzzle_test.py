import pytest
# from part_one_solution import part_one
# from part_two_solution import part_two
from puzzle import Puzzle

EXAMPLE = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


@pytest.mark.skip("Wait")
def test_example() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.answer == 3749


def test_parses_example() -> None:
    puzzle = Puzzle(EXAMPLE)
    results = puzzle.parse()
    assert results == [
        (190, (10, 19)),
        (3267, (81, 40, 27)),
        (83, (17, 5)),
        (156, (15, 6)),
        (7290, (6, 8, 6, 15)),
        (161011, (16, 10, 13)),
        (192, (17, 8, 14)),
        (21037, (9, 7, 18, 13)),
        (292, (11, 6, 16, 20)),
    ]


@pytest.mark.parametrize('answer, scenario, result', (
    (190, (10, 19), True),
    (3267, (81, 40, (27,)), True),
    (83, (17, 5), False),
    (156, (15, 6), False),
    (7290, (6, 8, (6, 15)), False),
    (161011, (16, 10, (13,)), False),
    (192, (17, 8, (14,)), False),
    (21037, (9, 7, (18, 13)), False),
    (292, (11, 6, (16, 20)), True),
))
def test_multiplies(answer, scenario, result) -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.solve(answer, *scenario) is result
