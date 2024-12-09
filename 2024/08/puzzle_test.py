import pytest
# from part_one_solution import part_one
# from part_two_solution import part_two
from puzzle import Puzzle


EXAMPLE = """
......#....#
...#....0...
....#0....#.
..#....0....
....0....#..
.#....A.....
...#........
#......#....
........A...
.........A..
..........#.
..........#.
""".strip()


@pytest.mark.skip("Not Yet")
def test_example() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert EXAMPLE == ""
    # assert puzzle.answer == 10


def test_parse() -> None:
    puzzle = Puzzle(EXAMPLE)
    results = puzzle.parse()
    assert results == [
        list('......#....#'),
        list('...#....0...'),
        list('....#0....#.'),
        list('..#....0....'),
        list('....0....#..'),
        list('.#....A.....'),
        list('...#........'),
        list('#......#....'),
        list('........A...'),
        list('.........A..'),
        list('..........#.'),
        list('..........#.'),
    ]


def test_coords() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.coords == {
        '#': [
            (0, 6),
            (0, 11),
            (1, 3),
            (2, 4),
            (2, 10),
            (3, 2),
            (4, 9),
            (5, 1),
            (6, 3),
            (7, 0),
            (7, 7),
            (10, 10),
            (11, 10),
        ],
        'A': [
            (5, 6),
            (8, 8),
            (9, 9),
        ],
        '0': [
            (1, 8),
            (2, 5),
            (3, 7),
            (4, 4),
        ]
    }


def test_diagonals() -> None:
    puzzle = Puzzle(EXAMPLE)
    results = puzzle.parse()
    import numpy
    ar = numpy.array(results)
    for row in range(len(results)):
        for column in range(len(results[0])):
            print(row * -1, column)
            print(numpy.diagonal(ar, axis1=row * -1, axis2=column))
    # for i in range(len(results[0])):
    #     print(numpy.diagonal(ar, i))
    # for i in range(-1 * len(results), 0):
    #     print(numpy.diagonal(ar, i))

    assert False
