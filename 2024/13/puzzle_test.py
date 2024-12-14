from puzzle import Puzzle, Prize
from data import DATA


EXAMPLE = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
""".strip()


def test_parse() -> None:
    puzzle = Puzzle(EXAMPLE)
    prize1 = puzzle.prizes[0]
    assert prize1.button_a == (94, 34)
    assert prize1.button_b == (22, 67)
    assert prize1.location == (8400, 5400)
    prize2 = puzzle.prizes[1]
    assert prize2.button_a == (26, 66)
    assert prize2.button_b == (67, 21)
    assert prize2.location == (12748, 12176)
    prize3 = puzzle.prizes[2]
    assert prize3.button_a == (17, 86)
    assert prize3.button_b == (84, 37)
    assert prize3.location == (7870, 6450)
    prize4 = puzzle.prizes[3]
    assert prize4.button_a == (69, 23)
    assert prize4.button_b == (27, 71)
    assert prize4.location == (18641, 10279)


def test_parse_default() -> None:
    puzzle = Puzzle("")
    prize = puzzle.prizes[0]
    assert prize.button_a == (0, 0)
    assert prize.button_b == (0, 0)
    assert prize.location == (0, 0)


def test_prize_one() -> None:
    data = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400
    """.strip()
    prize = Prize(data)
    assert prize.presses == (80, 40)
    assert prize.tokens == 280


def test_prize_one_part_two() -> None:
    data = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400
    """.strip()
    prize = Prize(data, part_two=True)
    assert prize.tokens == 0


def test_prize_two() -> None:
    data = """
Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176
    """.strip()
    prize = Prize(data)
    assert prize.tokens == 0


def test_prize_two_part_two() -> None:
    data = """
Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176
    """.strip()
    prize = Prize(data, part_two=True)
    assert prize.tokens == 459_236_326_669


def test_prize_three() -> None:
    data = """
Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450
    """.strip()
    prize = Prize(data)
    assert prize.tokens == 200


def test_prize_three_part_two() -> None:
    data = """
Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450
    """.strip()
    prize = Prize(data, part_two=True)
    assert prize.tokens == 0


def test_prize_four() -> None:
    data = """
Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
    """.strip()
    prize = Prize(data)
    assert prize.tokens == 0


def test_prize_four_part_two() -> None:
    data = """
Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
    """.strip()
    prize = Prize(data, part_two=True)
    assert prize.tokens == 416_082_282_239


def test_example() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.answer == 480


def test_part_one() -> None:
    puzzle = Puzzle(DATA)
    # assert puzzle.answer == 15_974  # too low
    # assert puzzle.answer == 23_417  # too low
    assert puzzle.answer == 31065


def test_part_two() -> None:
    puzzle = Puzzle(DATA, part_two=True)
    assert puzzle.answer == 93866170395343
