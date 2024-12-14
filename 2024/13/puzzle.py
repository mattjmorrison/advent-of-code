import re
from functools import cached_property


class Prize:

    def __init__(self, data: str, part_two: bool = False):
        self.data = data
        self.part_two = part_two

    def _parse(self, label: str, split: str) -> tuple[int, int]:
        split = '\\' + split if split == '+' else split
        for row in self.data.split('\n'):
            match = re.search(
                fr'{label}: X{split}(\d+), Y{split}(\d+)', row
            )
            if match:
                return (int(match.group(1)), int(match.group(2)))
        return (0, 0)

    @cached_property
    def button_a(self) -> tuple[int, int]:
        return self._parse('Button A', '+')

    @cached_property
    def button_b(self) -> tuple[int, int]:
        return self._parse('Button B', '+')

    @cached_property
    def location(self) -> tuple[int, int]:
        x, y = self._parse('Prize', '=')
        inc = 10000000000000 if self.part_two else 0
        return (x + inc, y + inc)

    @property
    def presses(self) -> tuple[int, int]:
        diagonal = self.button_a[0] * self.button_b[1] - self.button_a[1] * self.button_b[0]
        diagonal_x = self.location[0] * self.button_b[1] - self.location[1] * self.button_b[0]
        diagonal_y = self.button_a[0] * self.location[1] - self.button_a[1] * self.location[0]
        x = diagonal_x / diagonal
        y = diagonal_y / diagonal
        if x >= 0 and x == int(x) and y >= 0 and y == int(y):
            return (int(x), int(y))
        return (0, 0)

    def calc(self, presses: tuple[int, int]) -> int:
        return presses[0] * 3 + presses[1] * 1

    @property
    def tokens(self) -> int:
        return self.calc(self.presses)


class Puzzle:

    def __init__(self, data: str, part_two: bool = False):
        self.data = data
        self.part_two = part_two

    @cached_property
    def answer(self) -> int:
        return sum(prize.tokens for prize in self.prizes)

    @cached_property
    def prizes(self) -> list[Prize]:
        prizes = []
        for prize_data in self.data.split('\n\n'):
            prizes.append(Prize(prize_data, part_two=self.part_two))
        return prizes
