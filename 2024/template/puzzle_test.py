from puzzle import Puzzle


EXAMPLE = ""


def test_example() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.answer == 0
