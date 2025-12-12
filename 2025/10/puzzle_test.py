from puzzle import Puzzle, Machine, Button

import pytest

from data import input


TEST_INPUT = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
""".strip()


@pytest.mark.parametrize('lights, result', (
    ('1,3', [0, 1, 0, 1]),
    ('0,2', [1, 0, 1, 0]),
    ('0,2,3', [1, 0, 1, 1]),
))
def test_button_joltage(lights, result):
    button = Button(lights)
    assert button.update_joltage([0, 0, 0, 0]) == result


def test_parse_machine_lights():
    puzzle = Puzzle(TEST_INPUT)
    machines = puzzle.build_machines()
    assert len(machines) == 3
    assert machines[0].lights == [False, True, True, False]
    assert machines[1].lights == [False, False, False, True, False]
    assert machines[2].lights == [False, True, True, True, False, True]


def test_parse_joltage():
    puzzle = Puzzle(TEST_INPUT)
    machines = puzzle.build_machines()
    assert len(machines) == 3
    assert machines[0].joltage == [3, 5, 4, 7]
    assert machines[1].joltage == [7, 5, 12, 7, 2]
    assert machines[2].joltage == [10, 11, 11, 5, 10, 5]


def test_parse_machine_buttons():
    puzzle = Puzzle(TEST_INPUT)
    machines = puzzle.build_machines()
    assert len(machines) == 3
    assert len(machines[0].buttons) == 6
    assert machines[0].buttons[0].lights == [3]
    assert machines[0].buttons[1].lights == [1, 3]
    assert machines[0].buttons[2].lights == [2]
    assert machines[0].buttons[3].lights == [2, 3]
    assert machines[0].buttons[4].lights == [0, 2]
    assert machines[0].buttons[5].lights == [0, 1]

    assert len(machines[1].buttons) == 5
    assert machines[1].buttons[0].lights == [0, 2, 3, 4]
    assert machines[1].buttons[1].lights == [2, 3]
    assert machines[1].buttons[2].lights == [0, 4]
    assert machines[1].buttons[3].lights == [0, 1, 2]
    assert machines[1].buttons[4].lights == [1, 2, 3, 4]

    assert len(machines[2].buttons) == 4
    assert machines[2].buttons[0].lights == [0, 1, 2, 3, 4]
    assert machines[2].buttons[1].lights == [0, 3, 4]
    assert machines[2].buttons[2].lights == [0, 1, 2, 4, 5]
    assert machines[2].buttons[3].lights == [1, 2]


def test_machine_lights():
    machine = Machine('[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {2}')
    assert machine.press(0) == [False, False, False, True]
    assert machine.press(1) == [False, True, False, True]
    assert machine.press(2) == [False, False, True, False]
    assert machine.press(3) == [False, False, True, True]
    assert machine.press(4) == [True, False, True, False]
    assert machine.press(5) == [True, True, False, False]


@pytest.mark.parametrize('input, count', (
    ('[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}', 2),
    ('[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}', 3),
    ('[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}', 2),
))
def test_machine_on(input, count):
    machine = Machine(input)
    presses = machine.turn_on()
    assert presses == count


@pytest.mark.parametrize('input, count', (
    ('[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}', 10),
    ('[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}', 12),
    ('[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}', 11),
))
def test_machine_joltage(input, count):
    machine = Machine(input)
    presses = machine.configure_joltage()
    assert presses == count


def test_part_one_example():
    puzzle = Puzzle(TEST_INPUT)
    assert puzzle.solve_part_one() == 7


def test_solve_part_one():
    puzzle = Puzzle(input)
    assert puzzle.solve_part_one() == 514


def test_part_two_example():
    puzzle = Puzzle(TEST_INPUT)
    assert puzzle.solve_part_two() == 33


def test_solve_part_two():
    puzzle = Puzzle(input)
    assert puzzle.solve_part_two() == 0
