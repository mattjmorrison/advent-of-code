import pytest
from part_one_solution import part_one
from part_two_solution import part_two
from puzzle import Puzzle

EXAMPLE = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


def test_example() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.answer == 143


def test_example_two() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.corrected_answer == 123


def test_parses_rules() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.rules == (
        (47, 53),
        (97, 13),
        (97, 61),
        (97, 47),
        (75, 29),
        (61, 13),
        (75, 53),
        (29, 13),
        (97, 29),
        (53, 29),
        (61, 53),
        (97, 53),
        (61, 29),
        (47, 13),
        (75, 47),
        (97, 75),
        (47, 61),
        (75, 61),
        (47, 29),
        (75, 13),
        (53, 13),   
    )


def test_parses_updates() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.updates == (
        (75, 47, 61, 53, 29),
        (97, 61, 53, 29, 13),
        (75, 29, 13),
        (75, 97, 47, 61, 53),
        (61, 13, 29),
        (97, 13, 75, 29, 47),
    )


@pytest.mark.parametrize('scenario, answer', (
    ((75, 47, 61, 53, 29), True),
    ((97, 61, 53, 29, 13), True),
    ((75, 29, 13), True),
    ((75, 97, 47, 61, 53), False),
    ((61, 13, 29), False),
    ((97, 13, 75, 29, 47), False),
))
def test_passes_rules(scenario, answer) -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.check_rules(scenario) == answer


@pytest.mark.parametrize('scenario, answer', (
    ((75, 97, 47, 61, 53), (97, 75, 47, 61, 53)),
    ((61, 13, 29), (61, 29, 13)),
    ((97, 13, 75, 29, 47), (97, 75, 47, 29, 13)),
))
def test_reorder(scenario, answer) -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.reorder(scenario) == answer


@pytest.mark.parametrize('scenario, answer', (
    ((75, 47, 61, 53, 29), 61),
    ((97, 61, 53, 29, 13), 53),
    ((75, 29, 13), 29),
))
def test_find_middle_number(scenario, answer) -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.find_middle(scenario) == answer


@pytest.mark.parametrize('scenario, number, answer', (
    ((75, 47, 61, 53, 29), 75, 0), # not after any
    ((75, 47, 61, 53, 29), 47, 1), # after 75
    ((75, 47, 61, 53, 29), 61, 2), # after 47
    ((75, 47, 61, 53, 29), 53, 3), # after 61
    ((75, 47, 61, 53, 29), 29, 4), # after 47, 61, 75, 53
))
def test_get_max_pos(scenario, number, answer) -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.get_max_position(number, scenario) == answer


def test_part_one() -> None:
    assert part_one() == 4814


def test_part_two() -> None:
    assert part_two() == "X"
