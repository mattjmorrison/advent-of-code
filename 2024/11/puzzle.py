from typing import Self
from functools import cache


class Stone:

    def __init__(self, number: int):
        self.number = number

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Stone) and self.number == other.number

    def __str__(self) -> str:
        return str(self.number)

    def __repr__(self) -> str:
        return str(self)

    def __hash__(self) -> int:
        return self.number

    @property
    def is_even(self) -> bool:
        return len(str(self.number)) % 2 == 0

    def split(self) -> list[Self]:
        if self.is_even:
            index = int(len(str(self.number)) / 2)
            return [
                type(self)(int(str(self.number)[:index])),
                type(self)(int(str(self.number)[index:]))
            ]
        return [self]

    def blink(self) -> list[Self]:
        new_stones: list[Self] = []
        if self.number == 0:
            new_stones.append(type(self)(1))
        elif self.is_even:
            new_stones.extend(self.split())
        else:
            new_stones.append(type(self)(self.number * 2024))
        return new_stones


class Puzzle:

    def __init__(self, data: str):
        self.data = data
        self.state: list[Stone] = []
        self.parse()

    def answer(self, times: int) -> int:
        for _ in range(times):
            self.blink()
        return len(self.state)

    def parse(self) -> None:
        for item in self.data.split(' '):
            self.state.append(Stone(int(item)))

    def blink(self) -> None:
        new_line = []
        for stone in self.state:
            new_line.extend(self.get_new_stones(stone))
        self.state = new_line

    # def blink(self) -> None:
    #     index = 0
    #     while True:
    #         print(index)
    #         if index >= len(self.state):
    #             break
    #         current_stone = self.state[index]
    #         new_stones = self.get_new_stones(current_stone)
    #         for new_index, new_stone in enumerate(new_stones, 1):
    #             self.state.insert(index + new_index, new_stone)
    #         index += 1 + len(new_stones)
    #         if index > 1000:
    #             break

    @cache
    def get_new_stones(self, stone: Stone) -> list[Stone]:
        return stone.blink()
