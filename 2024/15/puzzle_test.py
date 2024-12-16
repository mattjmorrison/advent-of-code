from puzzle import Puzzle
from data import DATA
from part_two_data import DATA as PART_TWO_DATA

BIG_EXAMPLE_TWO = """
####################
##....[]....[]..[]##
##............[]..##
##..[][]....[]..[]##
##....[]@.....[]..##
##[]##....[]......##
##[]....[]....[]..##
##..[][]..[]..[][]##
##........[]......##
####################

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


def test_part_two() -> None:
    puzzle = Puzzle(PART_TWO_DATA, part_two=True)
    puzzle.run()
    print(puzzle.show_grid())
    assert puzzle.answer < 1539130  # too high


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


def test_parse_big_example_part_two() -> None:
    result = """
####################
##[].......[].[][]##
##[]...........[].##
##[]........[][][]##
##[]......[]....[]##
##..##......[]....##
##..[]............##
##..@......[].[][]##
##......[][]..[]..##
####################
""".strip()
    puzzle = Puzzle(BIG_EXAMPLE_TWO, part_two=True)
    puzzle.run()
    assert puzzle.show_grid().strip() == result
    assert puzzle.answer == 9021


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


def test_part_two_move() -> None:
    data = """
##############
##......##..##
##..........##
##....[][]@.##
##....[]....##
##..........##
##############
    """.strip()
    puzzle = Puzzle(data, part_two=True)
    for _ in range(10):
        puzzle.move("<")
    assert (
        puzzle.show_grid().strip()
        == """
##############
##......##..##
##..........##
##[][]@.....##
##....[]....##
##..........##
##############
""".strip()
    )


def test_part_two_new_grid() -> None:
    data = """
##############
##......##..##
##..........##
##....[][]@.##
##....[]....##
##..........##
##############
    """.strip()
    puzzle = Puzzle(data, part_two=True)
    assert puzzle.robot == (10, 3)
    assert puzzle.boxes == [
        (6, 3),
        (8, 3),
        (6, 4),
        (7, 3),
        (9, 3),
        (7, 4),
    ]
    assert puzzle.walls == [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (5, 0),
        (6, 0),
        (7, 0),
        (8, 0),
        (9, 0),
        (10, 0),
        (11, 0),
        (12, 0),
        (13, 0),
        (0, 1),
        (1, 1),
        (8, 1),
        (9, 1),
        (12, 1),
        (13, 1),
        (0, 2),
        (1, 2),
        (12, 2),
        (13, 2),
        (0, 3),
        (1, 3),
        (12, 3),
        (13, 3),
        (0, 4),
        (1, 4),
        (12, 4),
        (13, 4),
        (0, 5),
        (1, 5),
        (12, 5),
        (13, 5),
        (0, 6),
        (1, 6),
        (2, 6),
        (3, 6),
        (4, 6),
        (5, 6),
        (6, 6),
        (7, 6),
        (8, 6),
        (9, 6),
        (10, 6),
        (11, 6),
        (12, 6),
        (13, 6),
    ]
    # assert puzzle.show_grid().strip() == data


def test_long_part_two_example() -> None:
    states = [
        """
##############
##......##..##
##..........##
##....[][]@.##
##....[]....##
##..........##
##############

<vv<<^^<<^^
    """.strip(),
        """
##############
##......##..##
##..........##
##...[][]@..##
##....[]....##
##..........##
##############
""".strip(),
        """
##############
##......##..##
##..........##
##...[][]...##
##....[].@..##
##..........##
##############
    """.strip(),
        """
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.......@..##
##############
    """.strip(),
        """
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##......@...##
##############
    """.strip(),
        """
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.....@....##
##############
""".strip(),
        """
##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############
""".strip(),
        """
##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############
""".strip(),
        """
##############
##......##..##
##...[][]...##
##....[]....##
##....@.....##
##..........##
##############
""".strip(),
        """
##############
##......##..##
##...[][]...##
##....[]....##
##...@......##
##..........##
##############
""".strip(),
        """
##############
##......##..##
##...[][]...##
##...@[]....##
##..........##
##..........##
##############
""".strip(),
        """
##############
##...[].##..##
##...@.[]...##
##....[]....##
##..........##
##..........##
##############
""".strip(),
    ]
    counter = 0
    puzzle = Puzzle(states[counter], part_two=True)
    for direction in puzzle.directions:
        counter += 1
        puzzle.move(direction)
        assert puzzle.show_grid().strip() == states[counter]
