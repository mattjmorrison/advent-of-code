import re
from functools import cached_property


class Prize:

    def __init__(self, data: str):
        self.data = data

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
        return self._parse('Prize', '=')

    @cached_property
    def x_first(self) -> bool:
        return self.location and self.location[0] > self.location[1]

    @cached_property
    def first_button(self) -> tuple[int, int]:
        if self.x_first and self.button_a[0] > self.button_b[0]:
            return self.button_a
        return self.button_b

    @cached_property
    def second_button(self) -> tuple[int, int]:
        if self.x_first and self.button_a[0] > self.button_b[0]:
            return self.button_b
        return self.button_a

    @cached_property
    def presses(self) -> int:
        search = True
        if self.x_first:
            x = self.location[0]
            one_x = self.first_button[0]
            two_x = self.second_button[0]
            first_adjust = 0
            while search:
                presses = int(x / one_x) - first_adjust
                result = x - (presses * one_x)
                second_adjust = 0
                while result > 0:
                    second_press = int(result / two_x) + second_adjust
                    result -= second_press * two_x
                    second_adjust += 1
                if result == 0:
                    search = False
                else:
                    first_adjust += 1
                if presses == 0:
                    break
        if all([
            sum([
                self.first_button[0] * presses,
                self.second_button[0] * second_press
            ]) == self.location[0],
            sum([
                self.first_button[1] * presses,
                self.second_button[1] * second_press
            ]) == self.location[1]
        ]):
            return (presses, second_press)


class Puzzle:

    def __init__(self, data: str):
        self.data = data

    @cached_property
    def answer(self) -> int:
        return 0

    @cached_property
    def prizes(self) -> list[Prize]:
        prizes = []
        for prize_data in self.data.split('\n\n'):
            prizes.append(Prize(prize_data))
        return prizes
