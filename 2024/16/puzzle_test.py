from puzzle import Puzzle
from puzzle2 import Puzzle2
from data import DATA


EXAMPLE = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
""".strip()

EXAMPLE_TWO = """
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
""".strip()


def test_part_one() -> None:
    puzzle = Puzzle2(DATA)
    assert puzzle.dijkstra()[0] == 122492


def test_part_two() -> None:
    puzzle = Puzzle2(DATA)
    # assert puzzle.dijkstra()[-1] == 524  # too high
    # assert puzzle.dijkstra()[-1] == 493  # too low
    assert puzzle.dijkstra()[-1] == 520


def test_puzzle2_dijkstra_example_two() -> None:
    puzzle = Puzzle2(EXAMPLE_TWO)
    result, direction, _ = puzzle.dijkstra()
    assert result == 11048
    assert direction == (0, -1)


def test_puzzle2_show_grid() -> None:
    puzzle = Puzzle2(EXAMPLE)
    assert puzzle.show_grid().strip() == EXAMPLE


def test_puzzle2_dijkstra() -> None:
    puzzle = Puzzle2(EXAMPLE)
    result, direction, _ = puzzle.dijkstra()
    assert result == 7036
    assert direction == (0, -1)


def test_puzzle2_part_2_example() -> None:
    puzzle = Puzzle2(EXAMPLE)
    result, direction, history = puzzle.dijkstra()
    assert history == 46


def test_puzzle2_part_2_example_2() -> None:
    puzzle = Puzzle2(EXAMPLE_TWO)
    result, direction, history = puzzle.dijkstra()
    assert history == 64


def test_puzzle2_init() -> None:
    puzzle = Puzzle2(EXAMPLE)
    assert puzzle.start == (1, 13)
    assert puzzle.end == (13, 1)
    assert puzzle.max_x == 14
    assert puzzle.max_y == 14


def test_puzzle2_is_valid() -> None:
    puzzle = Puzzle2(EXAMPLE)
    assert puzzle.is_valid(1, 1) == True
    assert puzzle.is_valid(0, 0) == False


def test_puzzle2_neighbors() -> None:
    puzzle = Puzzle2(EXAMPLE)
    assert puzzle.get_neighbors((1, 13), (1, 0)) == [
        (
            1,
            (
                (2, 13),
                (1, 0),
            ),
        ),
        (
            1001,
            (
                (1, 12),
                (0, -1),
            ),
        ),
    ]
    assert puzzle.get_neighbors((1, 13), (0, 1)) == [
        (1001, ((2, 13), (1, 0))),
    ]
    assert puzzle.get_neighbors((1, 13), (0, -1)) == [
        (
            1,
            ((1, 12), (0, -1)),
        ),
        (1001, ((2, 13), (1, 0))),
    ]


def test_get_neighbor_positions() -> None:
    puzzle = Puzzle2(EXAMPLE)
    assert puzzle.get_neighbor_positions((1, 13), (1, 0)) == [
        ((2, 13), (1, 0), 1),  # straight East
        ((1, 12), (0, -1), 1001),  # turn North
        ((1, 14), (0, 1), 1001),  # turn South
    ]
    assert puzzle.get_neighbor_positions((1, 13), (0, 1)) == [
        ((1, 14), (0, 1), 1),  # straight South
        ((0, 13), (-1, 0), 1001),  # turn East
        ((2, 13), (1, 0), 1001),  # turn West
    ]
    assert puzzle.get_neighbor_positions((1, 13), (-1, 0)) == [
        ((0, 13), (-1, 0), 1),  # straight West
        ((1, 14), (0, 1), 1001),  # turn North
        ((1, 12), (0, -1), 1001),  # turn South
    ]
    assert puzzle.get_neighbor_positions((1, 13), (0, -1)) == [
        ((1, 12), (0, -1), 1),  # straight North
        ((2, 13), (1, 0), 1001),  # turn East
        ((0, 13), (-1, 0), 1001),  # turn West
    ]


BIG_EXAMPLE = """
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
""".strip()


def test_parse() -> None:
    puzzle = Puzzle(EXAMPLE)
    grid = puzzle.grid
    assert grid.height == 15
    assert grid.width == 15
    assert grid.bot == (1, 13)
    assert grid.facing == (1, 0)


def test_space() -> None:
    data = """
#######
#.....#
#.S.E.#
#.....#
#######
    """.strip()
    puzzle = Puzzle(data)
    grid = puzzle.grid
    assert grid.spaces == [
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 1),
        (5, 1),
        (1, 2),
        (3, 2),
        (5, 2),
        (1, 3),
        (2, 3),
        (3, 3),
        (4, 3),
        (5, 3),
    ]


def test_missing_bot() -> None:
    puzzle = Puzzle("")
    assert puzzle.grid.bot == (-1, -1)


def test_show() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.grid.show().strip() == EXAMPLE


def test_get_moves() -> None:
    data = """
######
#...E#
#.S..#
#....#
######
    """.strip()
    puzzle = Puzzle(data)
    grid = puzzle.grid
    assert grid.get_moves(grid.bot) == {
        (2, 1): {
            "points": 1001,
        },
        (2, 3): {
            "points": 1001,
        },
        (3, 2): {
            "points": 1,
        },
        (1, 2): {
            "points": 2001,
        },
    }


def test_does_not_include_parent_moves_in_available_moves() -> None:
    data = """
######
#...E#
#.S..#
#....#
######
    """.strip()


def test_example() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.answer == 0
    # assert puzzle.answer == 7036


# def test_big_example() -> None:
#     puzzle = Puzzle(BIG_EXAMPLE)
#     assert puzzle.answer == 11048


def test_approach() -> None:
    grid = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
""".strip()
    steps = {
        (1, 13): {
            "free": {
                (2, 13): {
                    "parent": (1, 13),
                    "points": 1,
                    "free": {(3, 13): {"parent": (2, 13), "points": 1, "free": {}}},
                },
                (1, 12): {
                    "parent": (1, 13),
                    "points": 1001,
                    "free": {
                        (1, 11): {
                            "parent": (1, 12),
                            "points": 1,
                            "free": {
                                (1, 10): {
                                    "parent": (1, 11),
                                    "free": {
                                        (1, 9): {
                                            "parent": (1, 10),
                                            "points": 1,
                                            "free": {},
                                        }
                                    },
                                },
                                (2, 11): {
                                    "parent": (1, 11),
                                    "points": 1001,
                                    "free": {
                                        (3, 11): {
                                            "parent": (2, 11),
                                            "points": 1,
                                            "free": {},
                                        }
                                    },
                                },
                            },
                        }
                    },
                },
            }
        }
    }
