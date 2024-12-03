import pytest
from part_one_solution import part_one
# from part_two_solution import part_two
from puzzle import Puzzle


def test_example() -> None:
    data = """
    xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
    """
    puzzle = Puzzle(data)
    assert puzzle.answer == 161


def test_example_two() -> None:
    data = """
    xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
    """
    puzzle = Puzzle(data)
    # (2*4 + 8*5)
    assert puzzle.answer == 48


@pytest.mark.parametrize("example, answer", (
    ("xmul(2,4)", [(2, 4)]),
    (
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))",
        [
            (2, 4),
            (5, 5),
            (11, 8),
            (8, 5),
        ]
    ),
    (
        "mul(1,1)don't()mul(2,2)",
        [
            (1, 1),
        ]
    ),
    (
        "mul(1,1)don't()*%&&mul(2,2)do()mul(3,3)",
        [
            (1, 1),
            (3, 3),
        ]
    ),
))
def test_replaces_bad_characters(example, answer) -> None:
    puzzle = Puzzle(example)
    assert puzzle.strip == answer


def test_part_one() -> None:
    assert part_one() == 157621318
    # part 2              79845780
