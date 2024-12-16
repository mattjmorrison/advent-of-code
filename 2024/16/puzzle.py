class Grid:
    mods = (
        (-1, 0),
        (0, -1),
        (1, 0),
        (0, 1),
    )

    def __init__(self, grid: list[list[str]]):
        self._grid = grid
        self.facing = (1, 0)

    @property
    def height(self) -> int:
        return len(self._grid)

    @property
    def bot(self) -> tuple[int, int]:
        for index, row in enumerate(self._grid):
            if "S" in row:
                return (row.index("S"), index)
        return (-1, -1)

    @property
    def width(self) -> int:
        return len(self._grid[0])

    def show(self) -> str:
        output = ""
        for row in self._grid:
            for column in row:
                output += column
            output += "\n"
        return output

    @property
    def spaces(self) -> list[tuple[int, int]]:
        spaces: list[tuple[int, int]] = []
        for rindex, row in enumerate(self._grid):
            for cindex, col in enumerate(row):
                if col == ".":
                    spaces.append((cindex, rindex))
        return spaces

    def get_moves(self, bot: tuple[int, int]) -> dict[tuple[int, int], dict[str, int]]:
        moves = {}
        for mod_x, mod_y in self.mods:
            move = (bot[0] + mod_x, bot[1] + mod_y)
            if move in self.spaces:
                if (mod_x, mod_y) == self.facing:
                    points = 1
                elif (mod_x * -1, mod_y * -1) == self.facing:
                    points = 2001
                else:
                    points = 1001
                moves[move] = {"points": points}
        return moves


class Puzzle:

    def __init__(self, data: str):
        self.data = data

    @property
    def answer(self) -> int:
        return 0

    @property
    def grid(self) -> Grid:
        return Grid([list(row) for row in self.data.split("\n")])
