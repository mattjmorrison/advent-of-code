from functools import cached_property
from itertools import product
from collections import deque


class NumPad:
    PAD = (
        ('7', '8', '9'),
        ('4', '5', '6'),
        ('1', '2', '3'),
        ('', '0', 'A'),
    )

    @cached_property
    def coords(self) -> dict[str, tuple[int, int]]:
        coords = {}
        for rindex, row in enumerate(self.PAD):
            for cindex, col in enumerate(row):
                if col:
                    coords[col] = (rindex, cindex)
        return coords

    @cached_property
    def paths(self) -> dict[tuple[str, str], list[str]]:
        paths: dict[tuple[str, str], list[str]] = {}
        for start_button, start_coords in self.coords.items():
            for end_button, end_coords in self.coords.items():
                if start_button == end_button:
                    paths[(start_button, end_button)] = ["A"]
                    continue
                queue = deque([(start_coords, "")])
                best = float('inf')
                options = []
                while queue:
                    (row, col), cmds = queue.popleft()
                    for nrow, ncol, cmd in self.get_neighbors(row, col):
                        if (nrow, ncol) == end_coords:
                            new_best = len(cmds) + 1
                            if best < new_best:
                                break
                            best = new_best
                            options.append(cmds + cmd + 'A')
                        else:
                            queue.append(((nrow, ncol), cmds + cmd))
                    else:
                        continue
                    break
                paths[(start_button, end_button)] = options
        return paths

    def exec_cmd(self, command: str) -> list[list[str]]:
        paths = []
        for start, end in zip('A' + command, command):
            paths.append(self.paths[(start, end)])
        return ["".join(path) for path in product(*paths)]

    def get_neighbors(self, row: int, col: int) -> list[tuple[int, int, str]]:
        mods = (
            (-1, 0, '^'),
            (1, 0, 'v'),
            (0, -1, '<'),
            (0, 1, '>'),
        )
        neighbors = []
        for mod_x, mod_y, cmd in mods:
            new_row = row + mod_x
            new_col = col + mod_y
            if self.should_skip_neighbor(new_row, new_col):
                continue
            neighbors.append((new_row, new_col, cmd))
        return neighbors

    def should_skip_neighbor(self, row: int, col: int) -> bool:
        if row < 0 or row >= len(self.PAD):
            return True
        if col < 0 or col >= len(self.PAD[0]):
            return True
        if not self.PAD[row][col]:
            return True
        return False


DIR_PAD = [
    ['', '^', 'A'],
    ['<', 'V', '>'],
]


# class Robot:

#     def __init__(self) -> None:
#         pass


class Puzzle:

    def __init__(self, data: str):
        self.data = data

    @property
    def answer(self) -> int:
        return 0
