import re
from typing import Optional


class Prize:

    def __init__(self, data: str):
        self.data = data

    def _parse(self, label: str, split: str) -> Optional[tuple[int, int]]:
        split = '\\' + split if split == '+' else split
        for row in self.data.split('\n'):
            match = re.search(
                fr'{label}: X{split}(\d+), Y{split}(\d+)', row
            )
            if match:
                return (int(match.group(1)), int(match.group(2)))
        return None

    @property
    def button_a(self) -> Optional[tuple[int, int]]:
        return self._parse('Button A', '+')

    @property
    def button_b(self) -> Optional[tuple[int, int]]:
        return self._parse('Button B', '+')

    @property
    def location(self) -> Optional[tuple[int, int]]:
        return self._parse('Prize', '=')


class Puzzle:

    def __init__(self, data: str):
        self.data = data

    @property
    def answer(self) -> int:
        return 0

    @property
    def prizes(self) -> list[Prize]:
        prizes = []
        for prize_data in self.data.split('\n\n'):
            prizes.append(Prize(prize_data))
        return prizes
