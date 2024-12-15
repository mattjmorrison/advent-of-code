from puzzle import Puzzle
from data import DATA

BIG_EXAMPLE = """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
""".strip()

EXAMPLE = """
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
""".strip()


def test_part_one() -> None:
    puzzle = Puzzle(DATA)
    puzzle.run()
    assert puzzle.answer == 1514353


def test_parse_big_example() -> None:
    result = """
##########
#.O.O.OOO#
#........#
#OO......#
#OO@.....#
#O#.....O#
#O.....OO#
#O.....OO#
#OO....OO#
##########
""".strip()
    puzzle = Puzzle(BIG_EXAMPLE)
    puzzle.run()
    assert puzzle.show_grid().strip() == result
    assert puzzle.answer == 10092


def test_parse() -> None:
    puzzle = Puzzle(EXAMPLE)

    assert puzzle.robot == (2, 2)
    assert puzzle.boxes == [(3, 1), (5, 1), (4, 2), (4, 3), (4, 4), (4, 5)]
    assert puzzle.walls == [
        # Row
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (5, 0),
        (6, 0),
        (7, 0),
        # Row
        (0, 1),
        (7, 1),
        # Row
        (0, 2),
        (1, 2),
        (7, 2),
        # Row
        (0, 3),
        (7, 3),
        # Row
        (0, 4),
        (2, 4),
        (7, 4),
        # Row
        (0, 5),
        (7, 5),
        # Row
        (0, 6),
        (7, 6),
        # Row
        (0, 7),
        (1, 7),
        (2, 7),
        (3, 7),
        (4, 7),
        (5, 7),
        (6, 7),
        (7, 7),
    ]
    assert puzzle.directions == "<^^>>>vv<v>>v<<"


def test_show_grid() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.show_grid().strip() == EXAMPLE.split("\n\n")[0].strip()


def test_basic_instructions() -> None:
    data = """
...
.@.
...
""".strip()
    puzzle = Puzzle(data)
    assert puzzle.robot == (1, 1)
    puzzle.move(">")
    assert puzzle.robot == (2, 1)
    puzzle.move("<")
    assert puzzle.robot == (1, 1)
    puzzle.move("^")
    assert puzzle.robot == (1, 0)
    puzzle.move("v")
    assert puzzle.robot == (1, 1)


def test_instructions_with_walls() -> None:
    data = """
.#.
#@#
.#.
""".strip()
    puzzle = Puzzle(data)
    assert puzzle.robot == (1, 1)
    puzzle.move(">")
    assert puzzle.robot == (1, 1)
    puzzle.move("<")
    assert puzzle.robot == (1, 1)
    puzzle.move("^")
    assert puzzle.robot == (1, 1)
    puzzle.move("v")
    assert puzzle.robot == (1, 1)
    assert puzzle.walls == [(1, 0), (0, 1), (2, 1), (1, 2)]


def test_instructions_with_boxes() -> None:
    data = """
.....
..O..
.O@O.
..O..
.....
""".strip()
    puzzle = Puzzle(data)
    # right and back
    puzzle.move(">")
    puzzle.move("<")
    # left and back
    puzzle.move("<")
    puzzle.move(">")
    # up and back
    puzzle.move("^")
    puzzle.move("v")
    # down
    puzzle.move("v")

    assert (
        puzzle.show_grid().strip()
        == """
..O..
.....
O...O
..@..
..O..
""".strip()
    )


def test_moves_boxes_multiple_spots() -> None:
    data = ".@O.."
    puzzle = Puzzle(data)
    puzzle.move(">")
    assert puzzle.show_grid().strip() == "..@O."
    puzzle.move(">")
    assert puzzle.show_grid().strip() == "...@O"


def test_box_against_wall_does_not_move() -> None:
    data = ".@O#"
    puzzle = Puzzle(data)
    puzzle.move(">")
    assert puzzle.show_grid().strip() == ".@O#"


def test_moves_multiple_boxes_multiple_spots() -> None:
    data = ".@...O.O.O.#"
    puzzle = Puzzle(data)
    for i in range(10):
        puzzle.move(">")
    assert puzzle.show_grid().strip() == ".......@OOO#"


def test_long_example() -> None:
    states = [
        """
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
""".strip(),
        """
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########
""".strip(),
        """
########
#.@O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########
""".strip(),
        """
########
#.@O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########
""".strip(),
        """
########
#..@OO.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########
""".strip(),
        """
########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########
""".strip(),
        """
########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########
""".strip(),
        """
########
#....OO#
##..@..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########
""".strip(),
        """
########
#....OO#
##..@..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########
""".strip(),
        """
########
#....OO#
##.@...#
#...O..#
#.#.O..#
#...O..#
#...O..#
########
""".strip(),
        """
########
#....OO#
##.....#
#..@O..#
#.#.O..#
#...O..#
#...O..#
########
""".strip(),
        """
########
#....OO#
##.....#
#...@O.#
#.#.O..#
#...O..#
#...O..#
########
""".strip(),
        """
########
#....OO#
##.....#
#....@O#
#.#.O..#
#...O..#
#...O..#
########
""".strip(),
        """
########
#....OO#
##.....#
#.....O#
#.#.O@.#
#...O..#
#...O..#
########
""".strip(),
        """
########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########
""".strip(),
        """
########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########
""".strip(),
    ]
    puzzle = Puzzle(states[0])
    for counter, direction in enumerate(puzzle.directions, 1):
        puzzle.move(direction)
        assert puzzle.show_grid().strip() == states[counter]
    assert puzzle.answer == 2028
