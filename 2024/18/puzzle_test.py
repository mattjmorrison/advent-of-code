from puzzle import Puzzle, Maze
from data import DATA

EXAMPLE = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
"""

# def test_example() -> None:
#     puzzle = Puzzle(EXAMPLE)
#     assert puzzle.answer == 0


def test_create_grid() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.grid.strip() == """
S..#...
..#..#.
....#..
...#..#
..#..#.
.#..#..
#.#...E
    """.strip()


def test_with_day_16_solution() -> None:
    puzzle = Puzzle(EXAMPLE)
    maze = Maze(puzzle.grid.strip())
    maze.dijkstra()
    for h in maze.history:
        print(h)
    print(len(maze.history))
    print(maze.get_solution_path(maze.end))


def test_part_one() -> None:
    puzzle = Puzzle(DATA)
    print(puzzle.grid.strip())
    assert False
