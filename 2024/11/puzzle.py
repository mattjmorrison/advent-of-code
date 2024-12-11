from typing import Self
from collections import Counter


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
        self.counter: Counter = Counter()
        self.parse()

    def answer(self, times: int) -> int:
        for _ in range(times):
            self.blink()
        return sum(self.counter.values())

    def parse(self) -> None:
        for item in self.data.split(' '):
            self.counter[Stone(int(item))] += 1

    def blink(self) -> None:
        new_counter: Counter = Counter()
        for stone, amount in self.counter.items():
            for new_stone in stone.blink():
                new_counter[new_stone] += amount
        self.counter = new_counter
