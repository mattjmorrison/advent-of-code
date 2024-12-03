import pytest
from part_one_solution import part_one
from part_two_solution import part_two
from puzzle import Puzzle


def test_example() -> None:
    data = """
    """
    puzzle = Puzzle(data)
    assert puzzle.answer == 'x'


@pytest.mark.skip("Wait")
def test_part_one() -> None:
    assert part_one() == "One"


@pytest.mark.skip("Wait")
def test_part_two() -> None:
    assert part_two() == "Two"
