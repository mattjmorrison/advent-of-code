from puzzle import Puzzle

from data import input

TEST_INPUT = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
""".strip()


def test_part_one_example():
    puzzle = Puzzle(TEST_INPUT)
    assert puzzle.solve_part_one(10) == 40


def test_part_one():
    puzzle = Puzzle(input)
    assert puzzle.solve_part_one(1000) == 352584


def test_part_two_example():
    puzzle = Puzzle(TEST_INPUT)
    assert puzzle.solve_part_two() == 25272


def test_part_two():
    puzzle = Puzzle(input)
    assert puzzle.solve_part_two() == 9617397716