import re
from functools import cached_property


class ParseError(Exception):
    pass


class Bot:

    def __init__(self, data: str, max_x: int = 101, max_y: int = 103):
        self.data = data
        self.max_x = max_x
        self.max_y = max_y
        self._pos_x: int | None = None
        self._pos_y: int | None = None

    def __hash__(self) -> int:
        return int(f"100{self.pos_x}{self.pos_y}")

    def __eq__(self, other: object) -> bool:
        return (self.pos_x, self.pos_y) == other

    def move(self) -> None:
        self.pos_x += self.vel_x
        if self.pos_x < 0:
            self.pos_x = self.max_x + self.pos_x
        elif self.pos_x >= self.max_x:
            self.pos_x = self.pos_x - self.max_x
        self.pos_y += self.vel_y
        if self.pos_y < 0:
            self.pos_y = self.max_y + self.pos_y
        elif self.pos_y >= self.max_y:
            self.pos_y = self.pos_y - self.max_y

    def _parse(self, field: str) -> int:
        match = re.search(
            "p=(?P<px>-?\d+),(?P<py>-?\d+) v=(?P<vx>-?\d+),(?P<vy>-?\d+)", self.data
        )
        if not match:
            raise ParseError(self.data)
        return int(match.group(field))

    @property
    def pos(self) -> tuple[int, int]:
        return (self.pos_x, self.pos_y)

    @property
    def pos_x(self) -> int:
        if self._pos_x is None:
            self._pos_x = self._parse("px")
        return self._pos_x

    @pos_x.setter
    def pos_x(self, value: int) -> None:
        self._pos_x = value

    @property
    def pos_y(self) -> int:
        if self._pos_y is None:
            self._pos_y = self._parse("py")
        return self._pos_y

    @pos_y.setter
    def pos_y(self, value: int) -> None:
        self._pos_y = value

    @property
    def vel_x(self) -> int:
        return self._parse("vx")

    @property
    def vel_y(self) -> int:
        return self._parse("vy")


class Puzzle:

    def __init__(self, data: str, max_x: int = 101, max_y: int = 103):
        self.data = data
        self.max_x = max_x
        self.max_y = max_y

    @property
    def answer(self) -> int:
        for i in range(100):
            for bot in self.bots:
                bot.move()

        return (
            self.top_left_bots
            * self.top_right_bots
            * self.bottom_left_bots
            * self.bottom_left_bots
        )

    @cached_property
    def bots(self) -> list[Bot]:
        bots = []
        for row in self.data.split("\n"):
            bots.append(Bot(row, self.max_x, self.max_y))
        return bots

    @property
    def top_right_bots(self) -> int:
        count = 0
        for bot in self.bots:
            count += self.top_right.count(bot.pos)
        return count

    @property
    def top_left_bots(self) -> int:
        count = 0
        for bot in self.bots:
            count += self.top_left.count(bot.pos)
        return count

    @property
    def bottom_left_bots(self) -> int:
        count = 0
        for bot in self.bots:
            count += self.bottom_left.count(bot.pos)
        return count

    @property
    def bottom_right_bots(self) -> int:
        count = 0
        for bot in self.bots:
            count += self.bottom_right.count(bot.pos)
        return count

    @cached_property
    def top_left(self) -> list[tuple[int, int]]:
        grid = []
        for y in range(0, int((self.max_y - 1) / 2)):
            for x in range(0, int((self.max_x - 1) / 2)):
                grid.append((x, y))
        return grid

    @cached_property
    def top_right(self) -> list[tuple[int, int]]:
        grid = []
        for y in range(int((self.max_y - 1) / 2) + 1, self.max_y):
            for x in range(0, int((self.max_x - 1) / 2)):
                grid.append((x, y))
        return grid

    @cached_property
    def bottom_left(self) -> list[tuple[int, int]]:
        grid = []
        for y in range(0, int((self.max_y - 1) / 2)):
            for x in range(int((self.max_y - 1) / 2) + 1, self.max_x):
                grid.append((x, y))
        return grid

    @cached_property
    def bottom_right(self) -> list[tuple[int, int]]:
        grid = []
        for y in range(int((self.max_y - 1) / 2) + 1, self.max_y):
            for x in range(int((self.max_x - 1) / 2) + 1, self.max_x):
                grid.append((x, y))
        return grid
