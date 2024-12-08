import pytest
from part_one_solution import part_one
from part_two_solution import part_two
from puzzle import Puzzle, LoopDetected

EXAMPLE = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
""".strip()


def test_example() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.answer == 41


@pytest.mark.skip("Not Yet")
def test_move() -> None:
    puzzle = Puzzle(EXAMPLE)
    puzzle.move()
    assert puzzle.map == """....#.....
.........#
..........
..#.......
.......#..
....^.....
.#..X.....
........#.
#.........
......#..."""


def test_move_up() -> None:
    puzzle = Puzzle("""
    ...
    .^.
    """.strip())
    puzzle.move()
    assert puzzle.map == [
        ['.', '^', '.'],
        ['.', 'X', '.']
    ]


def test_move_down() -> None:
    puzzle = Puzzle("""
    .v.
    ...
    """.strip())
    puzzle.move()
    assert puzzle.map == [
        ['.', 'X', '.'],
        ['.', 'v', '.']
    ]


def test_move_right() -> None:
    puzzle = Puzzle("""
    .>.
    """.strip())
    puzzle.move()
    assert puzzle.map == [
        ['.', 'X', '>'],
    ]


def test_move_left() -> None:
    puzzle = Puzzle("""
    .<.
    """.strip())
    puzzle.move()
    assert puzzle.map == [
        ['<', 'X', '.'],
    ]


def test_up_obsticle() -> None:
    puzzle = Puzzle("""
    .#.
    .^.
    """.strip())
    puzzle.move()
    assert puzzle.map == [
        ['.', '#', '.'],
        ['.', '>', '.']
    ]


def test_down_obsticle() -> None:
    puzzle = Puzzle("""
    .v.
    .#.
    """.strip())
    puzzle.move()
    assert puzzle.map == [
        ['.', '<', '.'],
        ['.', '#', '.']
    ]


def test_right_obsticle() -> None:
    puzzle = Puzzle("""
    .>#
    """.strip())
    puzzle.move()
    assert puzzle.map == [
        ['.', 'v', '#'],
    ]


def test_left_obsticle() -> None:
    puzzle = Puzzle("""
    #<.
    """.strip())
    puzzle.move()
    assert puzzle.map == [
        ['#', '^', '.'],
    ]


def test_up_edge() -> None:
    puzzle = Puzzle("""
    .^.
    """.strip())
    puzzle.move()
    assert puzzle.map == [
        ['.', 'X', '.'],
    ]


def test_down_edge() -> None:
    puzzle = Puzzle("""
    .v.
    """.strip())
    puzzle.move()
    assert puzzle.map == [
        ['.', 'X', '.'],
    ]


def test_right_edge() -> None:
    puzzle = Puzzle("""
    ..>
    """.strip())
    puzzle.move()
    assert puzzle.map == [
        ['.', '.', 'X'],
    ]


def test_left_edge() -> None:
    puzzle = Puzzle("""
    <..
    """.strip())
    puzzle.move()
    assert puzzle.map == [
        ['X', '.', '.'],
    ]

def test_keep_looping_when_left_on_map() -> None:
    puzzle = Puzzle("""
    <..
    """.strip())
    assert puzzle.keep_looping == (0, 0, '<')


def test_keep_looping_when_right_on_map() -> None:
    puzzle = Puzzle("""
    >..
    """.strip())
    assert puzzle.keep_looping == (0, 0, '>')


def test_keep_looping_when_up_on_map() -> None:
    puzzle = Puzzle("""
    ^..
    """.strip())
    assert puzzle.keep_looping == (0, 0, '^')


def test_keep_looping_when_down_on_map() -> None:
    puzzle = Puzzle("""
    v..
    """.strip())
    assert puzzle.keep_looping == (0, 0, 'v')


def test_stop_looping_when_not_on_map() -> None:
    puzzle = Puzzle("""
    XXX
    """.strip())
    assert puzzle.keep_looping == None


@pytest.mark.parametrize('map,count', (
    ('XXX', 3),
    ('X..', 1),
    ('X.X', 2),
    ("""X..
...
.X.""", 2)
))
def test_count_visited_spots(map: str, count: int) -> None:
    puzzle = Puzzle(map)
    assert puzzle.visit_count == count


def test_logs_turn_left() -> None:
    puzzle = Puzzle("""
    v
    #
    """.strip())
    assert puzzle.answer == 1
    assert puzzle.log == [
        (0, 0, '<'),
    ]


def test_logs_left() -> None:
    puzzle = Puzzle("""
    ..<
    """.strip())
    assert puzzle.answer == 3
    assert puzzle.log == [
        (0, 1, '<'),
        (0, 0, '<')
    ]


def test_logs_turn_right() -> None:
    puzzle = Puzzle("""
    #
    ^
    """.strip())
    assert puzzle.answer == 1
    assert puzzle.log == [
        (1, 0, '>'),
    ]


def test_logs_right() -> None:
    puzzle = Puzzle("""
    >..
    """.strip())
    assert puzzle.answer == 3
    assert puzzle.log == [
        (0, 1, '>'),
        (0, 2, '>')
    ]


def test_logs_turn_down() -> None:
    puzzle = Puzzle("""
    >#
    """.strip())
    assert puzzle.answer == 1
    assert puzzle.log == [
        (0, 0, 'v'),
    ]


def test_logs_down() -> None:
    puzzle = Puzzle("""
    v
    .
    .
    """.strip())
    assert puzzle.answer == 3
    assert puzzle.log == [
        (1, 0, 'v'),
        (2, 0, 'v')
    ]


def test_logs_turn_up() -> None:
    puzzle = Puzzle("""
    #<
    """.strip())
    assert puzzle.answer == 1
    assert puzzle.log == [
        (0, 1, '^'),
    ]


def test_logs_up() -> None:
    puzzle = Puzzle("""
    .
    .
    ^
    """.strip())
    assert puzzle.answer == 3
    assert puzzle.log == [
        (1, 0, '^'),
        (0, 0, '^'),
    ]


def test_stops_when_loop() -> None:
    puzzle = Puzzle("""
    ###
    #^#
    ###
    """.strip())
    assert puzzle.answer == 0
    assert puzzle.log == [
        (1, 1, '>'),
        (1, 1, 'v'),
        (1, 1, '<'),
        (1, 1, '^'),
        (1, 1, '>'),
    ]
    assert isinstance(puzzle.keep_looping, LoopDetected)

@pytest.mark.parametrize('scenario, count', [
    ("""....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""", 6)
])
def test_add_obsticles(scenario, count) -> None:
    puzzle = Puzzle(scenario)
    puzzle.try_obsticles()
    assert puzzle.loops == count


def test_clear_starting_position() -> None:
    scenario = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
""".strip()
    puzzle = Puzzle(scenario)
    puzzle.clear_starting_position()
    assert puzzle.map[6][4] == '.'


@pytest.mark.skip("good")
def test_part_one() -> None:
    assert part_one() == 4883


def test_part_two() -> None:
    assert part_two() == "X"
