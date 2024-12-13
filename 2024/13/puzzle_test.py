from puzzle import Puzzle


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


def test_example() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.answer == 0

    # 1st
    # A button 80 times and the B button 40 times
    # X axis (because 80*94 + 40*22 = 8400)
    # Y axis (because 80*34 + 40*67 = 5400)
    # 80*3 tokens for the A presses
    # 40*1 for the B presses
    # total of 280 tokens

    # 2nd
    # no prize

    # 3rd
    # A button 38 times
    # B button 86 times
    # 200 tokens

    # 4th
    # no prize

    # all (two) prizes is 480
