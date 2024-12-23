from puzzle import Puzzle
from data import DATA


DOCS = """

- Calculate the result of multiplying the secret number by 64.
- Then, mix this result into the secret number.
- Finally, prune the secret number.

- Calculate the result of dividing the secret number by 32.
- Round the result down to the nearest integer.
- Then, mix this result into the secret number.
- Finally, prune the secret number.

- Calculate the result of multiplying the secret number by 2048.
- Then, mix this result into the secret number.
- Finally, prune the secret number.


X To mix a value into the secret number, calculate the bitwise XOR
of the given value and the secret number.
X Then, the secret number becomes the result of that operation.
(If the secret number is 42 and you were to mix 15 into the secret number,
the secret number would become 37.)

X To prune the secret number, calculate the value of the secret number
modulo 16777216.
X Then, the secret number becomes the result of that operation.
(If the secret number is 100000000 and you were to prune the secret number,
the secret number would become 16113920.)

"""

EXAMPLE = """
1
10
100
2024
""".strip()


def test_part_one() -> None:
    puzzle = Puzzle(DATA)
    assert puzzle.answer == 0


def test_example() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.answer == 37327623


def test_prune() -> None:
    puzzle = Puzzle("")
    assert puzzle.prune(100000000) == 16113920


def test_mix() -> None:
    puzzle = Puzzle("")
    assert puzzle.mix(42, 15) == 37


def test_get_next_secret_number() -> None:
    puzzle = Puzzle("")
    secret_numbers = list(reversed([
        15887950,
        16495136,
        527345,
        704524,
        1553684,
        12683156,
        11100544,
        12249484,
        7753432,
        5908254,
    ]))
    test = 123
    while secret_numbers:
        next_secret = secret_numbers.pop()
        assert puzzle.get_next_secret(test) == next_secret
        test = next_secret


def test_example_for_buyers() -> None:
    data = """
1: 8685429
10: 4700978
100: 15273692
2024: 8667524
    """.strip()
    for start, end in [x.split(': ') for x in data.split('\n')]:
        puzzle = Puzzle("")
        secret = int(start)
        for _ in range(2000):
            secret = puzzle.get_next_secret(secret)
        assert secret == int(end)
