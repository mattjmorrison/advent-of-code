from puzzle import Puzzle
from data import DATA


EXAMPLE = """
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
""".strip()


def test_part_one() -> None:
    puzzle = Puzzle(DATA)
    assert puzzle.answer == 3483


def test_example() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.answer == 3


def test_find_keys() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert len(puzzle.keys) == 3
    assert len(puzzle.locks) == 2


def test_keys_contain_coords() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.keys[0] == [
        (1, 0),
        (2, 0),
        (3, 0),
        (3, 4),
        (4, 0),
        (4, 2),
        (4, 4),
        (5, 0),
        (5, 2),
        (5, 3),
        (5, 4),
        (6, 0),
        (6, 1),
        (6, 2),
        (6, 3),
        (6, 4),
    ]


def test_max_key_columns() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.max_key_columns(puzzle.keys[0]) == [
        1, 6, 4, 5, 3,
    ]
    assert puzzle.max_key_columns(puzzle.keys[1]) == [
        2, 3, 2, 6, 4
    ]
    assert puzzle.max_key_columns(puzzle.keys[2]) == [
        3, 6, 4, 6, 5
    ]


def test_max_lock_columns() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.max_lock_columns(puzzle.locks[0]) == [
        0, 5, 3, 4, 3
    ]
    assert puzzle.max_lock_columns(puzzle.locks[1]) == [
        1, 2, 0, 5, 3
    ]


def test_key_works_in_lock() -> None:
    puzzle = Puzzle(EXAMPLE)
    k = puzzle.max_key_columns(puzzle.keys[0])
    l = puzzle.max_lock_columns(puzzle.locks[0])
    assert puzzle.key_works(k, l) == False

    k = puzzle.max_key_columns(puzzle.keys[0])
    l = puzzle.max_lock_columns(puzzle.locks[1])
    assert puzzle.key_works(k, l) == False

    k = puzzle.max_key_columns(puzzle.keys[1])
    l = puzzle.max_lock_columns(puzzle.locks[0])
    assert puzzle.key_works(k, l) == False

    k = puzzle.max_key_columns(puzzle.keys[1])
    l = puzzle.max_lock_columns(puzzle.locks[1])
    assert puzzle.key_works(k, l) == True
    
    k = puzzle.max_key_columns(puzzle.keys[2])
    l = puzzle.max_lock_columns(puzzle.locks[0])
    assert puzzle.key_works(k, l) == True

    k = puzzle.max_key_columns(puzzle.keys[2])
    l = puzzle.max_lock_columns(puzzle.locks[1])
    assert puzzle.key_works(k, l) == True
