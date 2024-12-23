from functools import cached_property, cache
from itertools import product
from collections import deque


NUMBERS = (
    ('7', '8', '9'),
    ('4', '5', '6'),
    ('1', '2', '3'),
    ('', '0', 'A'),
)


ARROWS = (
    ('', '^', 'A'),
    ('<', 'v', '>'),
)


class Keypad:

    def __init__(self, keys: tuple[tuple[str, str, str], ...]):
        self.keys = keys

    @cached_property
    def coords(self) -> dict[str, tuple[int, int]]:
        coords = {}
        for rindex, row in enumerate(self.keys):
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
                paths[(start_button, end_button)] = self.get_options_for_path(
                    start_coords, end_coords
                )
        return paths

    def should_skip_neighbor(self, row: int, col: int) -> bool:
        if row < 0 or row >= len(self.keys):
            return True
        if col < 0 or col >= len(self.keys[0]):
            return True
        if not self.keys[row][col]:
            return True
        return False

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

    def get_options_for_path(
        self,
        start_coords: tuple[int, int],
        end_coords: tuple[int, int]
    ) -> list[str]:
        options = []
        queue = deque([(start_coords, "")])
        best = float('inf')
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
        return options

    @cache
    def get_length(self, start_button: str, end_button: str) -> int:
        return len(self.paths[(start_button, end_button)][0])


class Terminal:

    def __init__(self, keypad: Keypad):
        self.keypad = keypad

    def exec_cmd(self, command: str) -> list[str]:
        paths = []
        for start, end in zip('A' + command, command):
            paths.append(self.keypad.paths[(start, end)])
        return ["".join(path) for path in product(*paths)]

    @cache
    def find_length(self, command: str, depth: int = 2) -> int:
        if depth == 1:
            return sum(
                self.keypad.get_length(b1, b2)
                for b1, b2 in zip('A' + command, command)
            )
        length = 0
        for b1, b2 in zip('A' + command, command):
            length += min(
                self.find_length(
                    cmd, depth - 1
                ) for cmd in self.keypad.paths[(b1, b2)]
            )
        return length


class Puzzle:

    def __init__(self, data: str, robots: int = 2):
        self.data = data
        self.robots = robots

    @property
    def answer(self) -> int:
        number_pad = Keypad(NUMBERS)
        arrow_pad = Keypad(ARROWS)
        total = 0
        for command in self.data.split('\n'):
            number_bot = Terminal(number_pad)
            options = number_bot.exec_cmd(command)
            for _ in range(self.robots):
                options = self.get_options_for_robot(
                    Terminal(arrow_pad), options
                )
            total += len(options[0]) * int(command[:-1])
        return total

    @property
    def answer_part_two(self) -> int:
        number_pad = Keypad(NUMBERS)
        arrow_pad = Terminal(Keypad(ARROWS))
        total = 0
        for command in self.data.split('\n'):
            number_bot = Terminal(number_pad)
            cmds = number_bot.exec_cmd(command)
            length = min(
                [arrow_pad.find_length(cmd, self.robots) for cmd in cmds]
            )
            total += length * int(command[:-1])
        return total

    def get_options_for_robot(
        self,
        terminal: Terminal,
        options: list[str]
    ) -> list[str]:
        new_options = []
        for option in options:
            new_options.extend(terminal.exec_cmd(option))
        shortest_len = min(map(len, new_options))
        return [cmd for cmd in new_options if len(cmd) == shortest_len]
