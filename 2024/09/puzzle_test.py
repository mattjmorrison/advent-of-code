import pytest
from data import DATA
# from part_one_solution import part_one
# from part_two_solution import part_two
from puzzle import Puzzle


EXAMPLE = """
2333133121414131402
""".strip()


def test_example() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.blocks == list(
        "00...111...2...333.44.5555.6666.777.888899"
    )


def test_defrag() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.defrag() == list(
        "0099811188827773336446555566.............."
    )


def test_checksum() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.get_checksum() == 1928


@pytest.mark.parametrize('scenario, result', (
    ('0..1..2..3', True),
    ('0123......', False),
))
def test_has_gaps_true(scenario: str, result: bool) -> None:
    puzzle = Puzzle("")
    assert puzzle.has_gaps(list(scenario)) == result


# @pytest.mark.skip("Very Slow")
def test_part_one() -> None:
    puzzle = Puzzle(DATA)
    assert puzzle.get_checksum() == 6_216_544_403_458
