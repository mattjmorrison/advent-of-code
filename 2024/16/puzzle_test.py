from puzzle import Puzzle


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
    assert puzzle.grid.get_moves() == {
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
