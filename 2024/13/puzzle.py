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

    @property
    def presses(self) -> tuple[int, int]:
        presses = self.get_presses(self.button_a, self.button_b)
        if presses == (0, 0):
            tmp = self.get_presses(self.button_b, self.button_a)
            presses = (tmp[1], tmp[0])
        return presses

    @property
    def tokens(self) -> int:
        a_press, b_press = self.presses
        return a_press * 3 + b_press * 1

    def get_presses(  # noqa: C901
        self, first: tuple[int, int], second: tuple[int, int]
    ) -> tuple[int, int]:
        x = self.location[0]
        one_x = first[0]
        two_x = second[0]
        first_adjust = 0
        second_press = 0
        while True:
            presses = int(x / one_x) - first_adjust
            result = x - (presses * one_x)
            second_adjust = 0
            while result > 0:
                second_press = int(result / two_x) + second_adjust
                result -= second_press * two_x
                second_adjust += 1
            if result == 0 or presses == 0:
                break
            first_adjust += 1
        if self.is_match(first, presses, second, second_press):
            return (presses, second_press)
        return (0, 0)

    def is_match(
        self,
        first: tuple[int, int], first_presses: int,
        second: tuple[int, int], second_presses: int
    ) -> bool:
        return all([
            sum([
                first[0] * first_presses,
                second[0] * second_presses
            ]) == self.location[0],
            sum([
                first[1] * first_presses,
                second[1] * second_presses
            ]) == self.location[1]
        ])


class Puzzle:

    def __init__(self, data: str):
        self.data = data

    @cached_property
    def answer(self) -> int:
        return sum(prize.tokens for prize in self.prizes)

    @cached_property
    def prizes(self) -> list[Prize]:
        prizes = []
        for prize_data in self.data.split('\n\n'):
            prizes.append(Prize(prize_data))
        return prizes