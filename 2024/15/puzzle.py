class Puzzle:

    def __init__(self, data: str):
        self.data = data
        self._robot: tuple[int, int] | None = None
        self._boxes: list[tuple[int, int]] | None = None
        self._walls: list[tuple[int, int]] | None = None

    def _parse_grid(self, char: str) -> list[tuple[int, int]]:
        data = []
        for y, row in enumerate(self.data.split("\n\n")[0].split("\n")):
            for x, item in enumerate(row):
                if item == char:
                    data.append((int(x), int(y)))
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
        for box in self.boxes:
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

    def move_boxes(self, robot: tuple[int, int], direction: tuple[int, int]) -> bool:
        if robot in self.boxes:
            new_box = (robot[0] + direction[0], robot[1] + direction[1])
            if new_box in self.walls:
                return False
            elif new_box in self.boxes:
                if self.move_boxes(new_box, direction):
                    self.boxes.remove(robot)
                    self.boxes.append(new_box)
                else:
                    return False
            else:
                self.boxes.remove(robot)
                self.boxes.append(new_box)
        return True

    @property
    def directions(self) -> str:
        return self.data.split("\n\n")[1].replace("\n", "")

    @property
    def robot(self) -> tuple[int, int]:
        if self._robot is None:
            self._robot = self._parse_grid("@")[0]
        return self._robot

    @property
    def boxes(self) -> list[tuple[int, int]]:
        if self._boxes is None:
            self._boxes = self._parse_grid("O")
        return self._boxes

    @property
    def walls(self) -> list[tuple[int, int]]:
        if self._walls is None:
            self._walls = self._parse_grid("#")
        return self._walls

    def show_grid(self) -> str:
        grid = ""
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                if (x, y) == self.robot:
                    grid += "@"
                elif (x, y) in self.walls:
                    grid += "#"
                elif (x, y) in self.boxes:
                    grid += "O"
                else:
                    grid += "."
            grid += "\n"
        return grid
