import pytest
from puzzle import Puzzle
from data import input


test_input = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
""".strip()


def test_parse():
    puzzle = Puzzle(test_input)
    results = puzzle.parse()
    assert results == [
        (11, 22),
        (95, 115),
        (998, 1012),
        (1188511880, 1188511890),
        (222220, 222224),
        (1698522, 1698528),
        (446443, 446449),
        (38593856, 38593862),
        (565653, 565659),
        (824824821, 824824827),
        (2121212118, 2121212124),
    ]

@pytest.mark.parametrize('number, repeat', (
    (123123, True),
    (10001, False),
    (1221, False),
    (1212, True),
    (123123123123123123, True),
))
def test_is_repeated(number, repeat):
    puzzle = Puzzle("")
    assert puzzle.is_repeat(number) == repeat

@pytest.mark.parametrize('start, end, matches', (
    (11, 22, [11, 22]),
    (95, 115, [99]),
    (998, 1012, [1010]),
    (1188511880, 1188511890, [1188511885]),
    (222220, 222224, [222222]),
    (1698522, 1698528, []),
    (446443, 446449, [446446]),
    (38593856, 38593862, [38593859]),
    (565653, 565659, []),
    (824824821, 824824827, []),
    (2121212118, 2121212124, []),
))
def test_checks_for_repeats_in_ranges(start, end, matches):
    puzzle = Puzzle("")
    results = puzzle.get_repeats_in_range(start, end)
    assert results == matches


def test_total_invalid_numbers():
    puzzle = Puzzle(test_input)
    assert puzzle.solve() == 1227775554


def test_part_one():
    puzzle = Puzzle(input)
    assert puzzle.solve() == 23701357374