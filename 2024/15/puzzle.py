import typing as t


class Item:
    default_char = "."

    def __init__(self, x: int, y: int, char: str | None = None):
        self.x = x
        self.y = y
        self.char = char or self.default_char

    @property
    def pos(self) -> tuple[int, int]:
        return (self.x, self.y)

    def __eq__(self, other: object) -> bool:
        return (self.x, self.y) == other

    def __iter__(self) -> t.Iterable[int]:
        yield self.x
        yield self.y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


class Robot(Item):
    default_char = "@"


class Wall(Item):
    default_char = "#"


class Box(Item):
    default_char = "O"


class Puzzle:

    def __init__(self, data: str, part_two: bool = False):
        self.data = data
        self._robot: tuple[int, int] | None = None
        self._boxes: list[tuple[int, int]] | None = None
        self._walls: list[tuple[int, int]] | None = None
        self.part_two = part_two
        self.part_one = not self.part_two

    def _parse_grid(self, char: str, obj: type) -> list[tuple[int, int]]:
        data = []
        for y, row in enumerate(self.data.split("\n\n")[0].split("\n")):
            for x, item in enumerate(row):
                if item == char:
                    data.append(obj(int(x), int(y), char))
        return data

    @property
    def grid_width(self) -> int:
        return len(self.data.split("\n\n")[0].split("\n")[0])

    @property
    def grid_height(self) -> int:
        return len(self.data.split("\n\n")[0].split("\n"))

    @property
    def answer(self) -> int:
        total = 0
        boxes = (
            self.boxes if self.part_one else [b for b in self.boxes if b.char == "["]
        )
        for box in boxes:
            x, y = box
            total += 100 * y + x
        return total

    def run(self) -> None:
        for direction in self.directions:
            self.move(direction)

    def move(self, symbol: str) -> None:
        x, y = self.robot
        direction = (0, 0)
        match symbol:
            case ">":
                direction = (1, 0)
            case "<":
                direction = (-1, 0)
            case "^":
                direction = (0, -1)
            case "v":
                direction = (0, 1)
        new_robot = (x + direction[0], y + direction[1])
        if new_robot not in self.walls:
            if self.move_boxes(new_robot, direction):
                self._robot = new_robot

    def move_boxes(
        self, robot: tuple[int, int], direction: tuple[int, int], dry_run: bool = False
    ) -> bool:
        if robot not in self.boxes:
            return True
        if self.part_one or direction[0] != 0:
            return self.part_one_move_boxes(robot, direction, dry_run)
        else:
            other_half = self.get_other_box_half(robot)
            if self.part_one_move_boxes(
                robot, direction, True
            ) and self.part_one_move_boxes(other_half.pos, direction, True):
                return self.part_one_move_boxes(
                    robot, direction
                ) and self.part_one_move_boxes(other_half.pos, direction)
            return False

    def get_other_box_half(self, box: tuple[int, int]) -> tuple[int, int]:
        box_half_one = self.boxes[self.boxes.index(box)]
        if box_half_one.char == "[":
            return Box(box_half_one.x + 1, box_half_one.y, "]")
        return Box(box_half_one.x - 1, box_half_one.y, "[]")

    def part_one_move_boxes(
        self, robot: tuple[int, int], direction: tuple[int, int], dry_run: bool = False
    ) -> bool:
        if robot in self.boxes:
            old_box = self.boxes[self.boxes.index(robot)]
            new_box = (robot[0] + direction[0], robot[1] + direction[1])
            if new_box in self.walls:
                return False
            elif new_box in self.boxes:
                if self.move_boxes(new_box, direction, dry_run):
                    if not dry_run:
                        self.boxes.remove(robot)
                        self.boxes.append(Box(new_box[0], new_box[1], old_box.char))
                else:
                    return False
            else:
                if not dry_run:
                    self.boxes.remove(robot)
                    self.boxes.append(Box(new_box[0], new_box[1], old_box.char))
        return True

    @property
    def directions(self) -> str:
        return self.data.split("\n\n")[1].replace("\n", "")

    @property
    def robot(self) -> tuple[int, int]:
        if self._robot is None:
            self._robot = self._parse_grid("@", Robot)[0]
        return self._robot

    @property
    def boxes(self) -> list[tuple[int, int]]:
        if self._boxes is None:
            if self.part_one:
                self._boxes = self._parse_grid("O", Box)
            else:
                self._boxes = self._parse_grid("[", Box)
                self._boxes += self._parse_grid("]", Box)
        return self._boxes

    @property
    def walls(self) -> list[tuple[int, int]]:
        if self._walls is None:
            self._walls = self._parse_grid("#", Wall)
        return self._walls

    def show_grid(self) -> str:
        grid = ""
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                if (x, y) == self.robot:
                    grid += Robot.default_char
                elif (x, y) in self.walls:
                    grid += Wall.default_char
                elif (x, y) in self.boxes:
                    grid += self.boxes[self.boxes.index((x, y))].char
                else:
                    grid += Item.default_char
            grid += "\n"
        return grid
