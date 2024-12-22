from puzzle import Puzzle
from data import DATA


EXAMPLE = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
""".strip()


def test_grid() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert len(puzzle.grid) == 15
    assert len(puzzle.grid[0]) == 15


def test_default_start() -> None:
    puzzle = Puzzle("")
    assert puzzle.start == (0, 0)


def test_start() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.start == (3, 1)


def test_end() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.end == (7, 5)


def test_default_end() -> None:
    puzzle = Puzzle("")
    assert puzzle.end == (0, 0)


def test_initial_distances() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert len(puzzle.distances) == 15
    assert len(puzzle.distances[0]) == 15


def test_wall_distances_are_minus_one() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.distances[0][0] == -1


def test_cardinal_directions() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.dirs((0, 0)) == [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]


def test_cheat_positions() -> None:
    """
    (-2,  2) (-1,  2) (0,**2) (1,  2) (2,  2)
    (-2,  1) (-1,**1) (0,  1) (1,**1) (2,  1)
    (-2,**0) (-1,  0) (0,  0) (1,  0) (2,**0)
    (-2, -1) (-1,*-1) (0, -1) (1,*-1) (2, -1)
    (-2, -2) (-1, -2) (0,*-2) (1, -2) (2, -2)
    """
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.cheat_dirs((0, 0)) == [
        (2, 0),
        (1, 1),
        (0,  2),
        (-1, 1),

        (-2, 0),
        (-1, -1),
        (0, -2),
        (1, -1),
    ]


def test_distaince_display() -> None:
    puzzle = Puzzle(EXAMPLE)
    # for row in puzzle.grid:
    #     print(*row, sep='\t')
    for row in puzzle.distances:
        print(*row, sep='\t')


def test_original_path_seconds() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.distances[puzzle.end[0]][puzzle.end[1]] == 84


def test_outside_edge() -> None:
    puzzle = Puzzle("")
    assert puzzle.is_outside_grid(0, 9999999999) is True
    assert puzzle.is_outside_grid(0, -9999999999) is True
    assert puzzle.is_outside_grid(9999999999, 0) is True
    assert puzzle.is_outside_grid(-9999999999, 0) is True


def test_part_one() -> None:
    puzzle = Puzzle(DATA)
    assert puzzle.answer == 1387


def test_part_two() -> None:
    puzzle = Puzzle(DATA)
    assert puzzle.part_two == 1387
