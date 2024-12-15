import pytest
from data import DATA
from puzzle import Puzzle, Bot, ParseError


EXAMPLE = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
""".strip()


# def test_part_one() -> None:
#     puzzle = Puzzle(DATA)
#     # assert puzzle.answer == 498
#     assert puzzle.answer == 205_746_897
#   Part 1: 218_965_032
#   Part 2: 7037


def test_example() -> None:
    puzzle = Puzzle(EXAMPLE, 11, 7)
    for i in range(5):
        for bot in puzzle.bots:
            bot.move()
    # puzzle.answer
    print(puzzle.top_left_bots)
    print(puzzle.top_right_bots)
    print(puzzle.bottom_left_bots)
    print(puzzle.bottom_left_bots)
    assert False


def test_parses_example() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert len(puzzle.bots) == 12


def test_quadrants() -> None:
    puzzle = Puzzle("")
    assert puzzle.top_left[0] == (0, 0)
    assert puzzle.top_left[-1] == (49, 50)
    assert len(puzzle.top_left) == 2550

    assert puzzle.top_right[0] == (0, 52)
    assert puzzle.top_right[-1] == (49, 102)
    assert len(puzzle.top_right) == 2550

    assert puzzle.bottom_left[0] == (52, 0)
    assert puzzle.bottom_left[-1] == (100, 50)
    assert len(puzzle.bottom_left) == 2550

    assert puzzle.bottom_right[0] == (52, 52)
    assert puzzle.bottom_right[-1] == (101, 102)
    assert len(puzzle.bottom_right) == 2550


def test_count_bots_in_quad() -> None:
    data = """
p=0,0 v=0,0
p=1,1 v=0,0
p=0,55 v=0,0
p=1,55 v=0,0
p=55,0 v=0,0
p=55,1 v=0,0
p=55,55 v=0,0
p=55,56 v=0,0
    """.strip()
    puzzle = Puzzle(data)
    assert puzzle.top_left_bots == 2
    assert puzzle.top_right_bots == 2
    assert puzzle.bottom_left_bots == 2
    assert puzzle.bottom_right_bots == 2


#
# Bot Tests
#


def test_bot() -> None:
    bot = Bot("p=0,4 v=3,-3")
    assert bot.pos_x == 0
    assert bot.pos_y == 4
    assert bot.vel_x == 3
    assert bot.vel_y == -3


def test_invalid_parse_raises_exception() -> None:
    with pytest.raises(ParseError, match="this is invalid") as e:
        bot = Bot("this is invalid")
        bot.pos_x


@pytest.mark.parametrize(
    "data,position",
    (
        (
            "p=3,3 v=-3,-3",
            (0, 0),
        ),
        (
            "p=0,0 v=-1,-1",
            (100, 102),
        ),
        (
            "p=101,0 v=1,-1",
            (1, 102),
        ),
        (
            "p=101,0 v=3,-3",
            (3, 100),
        ),
        (
            "p=101,103 v=3,3",
            (3, 3),
        ),
        (
            "p=0,50 v=-3,0",
            (98, 50),
        ),
        (
            "p=101,50 v=3,0",
            (3, 50),
        ),
        (
            "p=50,0 v=0,-3",
            (50, 100),
        ),
        (
            "p=50,103 v=0,3",
            (50, 3),
        ),
    ),
)
def test_bot_move(data: str, position: tuple[int, int]) -> None:
    bot = Bot(data)
    bot.move()
    assert bot.pos == position


def test_can_tell_if_bot_in_list_of_coords() -> None:
    bot = Bot("p=0,0 v=1,1")
    assert bot in [(0, 0), (1, 0), (0, 1), (1, 1)]


def test_bot_is_hashable() -> None:
    bot = Bot("p=0,0 v=1,1")
    assert hash(bot) == 10000


def test_movement_example() -> None:
    bot = Bot("p=2,4 v=2,-3", 10, 6)
    bot.move()
    assert bot.pos == (4, 1)
    bot.move()
    assert bot.pos == (6, 4)
    bot.move()
    assert bot.pos == (8, 1)
    bot.move()
    assert bot.pos == (0, 4)
    bot.move()
    assert bot.pos == (2, 1)


def test_show_grid() -> None:
    """
    initial state
    1.12.......
    ...........
    ...........
    ......11.11
    1.1........
    .........1.
    .......1...

    after 100 seconds
    ......2..1.
    ...........
    1..........
    .11........
    .....1.....
    ...12......
    .1....1....
    """
    data = EXAMPLE.split("\n")[0]
    puzzle = Puzzle(data, 11, 7)
    display(puzzle)
    for _ in range(100):
        for bot in puzzle.bots:
            bot.move()
            if bot.pos_x >= 11 or bot.pos_x < 0 or bot.pos_y >= 7 or bot.pos_y < 0:
                print(bot.pos)
                display(puzzle)
    assert False


def display(puzzle: Puzzle) -> None:
    for y in range(puzzle.max_y):
        for x in range(puzzle.max_x):
            print(puzzle.bots.count((x, y)) or ".", end="")
        print("\n")
    print("=" * 80)


# def test_grid() -> None:
#     puzzle = Puzzle(DATA)
#     for y in range(puzzle.max_y):
#         for x in range(puzzle.max_x):
#             print(puzzle.bots.count((x, y)) or ".", end="")
#         print("\n")
#     assert False
