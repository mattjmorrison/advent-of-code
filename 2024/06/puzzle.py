from itertools import chain
from copy import deepcopy
from datetime import datetime

class LoopDetected:

    def __bool__(self):
        return False


class Puzzle:

    def __init__(self, data: str):
        print("in init")
        self._original = data
        self.build_map()
        self.loops = 0

    def build_map(self):
        self.log = []
        self.map = [list(x) for x in self._original.split()]

    def clear_starting_position(self) -> None:
        for rindex, row in enumerate(self.map):
            for cindex, column in enumerate(row):
                if column in '<^v>':
                    self.map[rindex][cindex] = '.'
                    return

    def try_obsticles(self, input_map, start, block) -> None:
        new_map = deepcopy(input_map)
        new_map[start[0]][start[1]] = start[2]
        new_map[block[0]][block[1]] = '#'
        self.map = new_map
        self.answer
        if isinstance(self.keep_looping, LoopDetected):
            self.loops += 1

    @property
    def answer(self) -> str:
        while self.keep_looping:
            self.move()
        return self.visit_count

    @property
    def visit_count(self) -> int:
        total = 0
        for row in self.map:
            total += row.count('X')
        return total

    @property
    def keep_looping(self) -> tuple[int, int, str]:
        for rindex, row in enumerate(self.map):
            for cindex, column in enumerate(row):
                if column in '<^v>':
                    result = (rindex, cindex, column)
                    if self.log.count(result) > 1:
                        return LoopDetected()
                    return result

    def move(self) -> None:
        for row_index, row in enumerate(self.map):
            up = "^" in row and row.index("^")
            if up is not False:
                break
            down = 'v' in row and row.index('v')
            if down is not False:
                break
            right = '>' in row and row.index('>')
            if right is not False:
                break
            left = '<' in row and row.index('<')
            if left is not False:
                break

        if up is not False:
            if row_index - 1 < 0:
                self.map[row_index][up] = 'X'
            elif self.map[row_index - 1][up] == '#':
                self.log.append((row_index, up, '>'))
                self.map[row_index][up] = '>'
            else:
                self.log.append((row_index - 1, up, '^'))
                self.map[row_index][up] = 'X'
                self.map[row_index - 1][up] = '^'
        elif down is not False:
            if row_index + 1 >= len(self.map):
                self.map[row_index][down] = 'X'
            elif self.map[row_index + 1][down] == '#':
                self.log.append((row_index, down, '<'))
                self.map[row_index][down] = '<'
            else:
                self.log.append((row_index + 1, down, 'v'))
                self.map[row_index][down] = 'X'
                self.map[row_index + 1][down] = 'v'
        elif right is not False:
            if right + 1 >= len(self.map[row_index]):
                self.map[row_index][right] = 'X'
            elif self.map[row_index][right + 1] == '#':
                self.log.append((row_index, right, 'v'))
                self.map[row_index][right] = 'v'
            else:
                self.map[row_index][right] = 'X'
                self.log.append((row_index, right + 1, '>'))
                self.map[row_index][right + 1] = '>'
        elif left is not False:
            if left - 1 < 0:
                self.map[row_index][left] = 'X'
            elif self.map[row_index][left - 1] == '#':
                self.log.append((row_index, left, '^'))
                self.map[row_index][left] = '^'
            else:
                self.map[row_index][left] = 'X'
                self.log.append((row_index, left - 1, '<'))
                self.map[row_index][left - 1] = '<'
