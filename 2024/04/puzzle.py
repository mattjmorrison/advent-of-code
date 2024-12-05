class Puzzle:

    def __init__(self, data: str):
        self.data = data

    @property
    def answer(self) -> int:
        return self.horizonal + self.vertical + self.diagonal

    @property
    def answer_two(self) -> int:
        total = 0
        for grid in self.get_grids():
            if self.is_x_mas(grid):
                total += 1
        return total

    def count_horizonal(self, data: list[str]) -> int:
        total = 0
        for row in data:
            total += row.count('XMAS')
            total += row.count('SAMX')
        return total

    @property
    def horizonal(self) -> int:
        return self.count_horizonal(self.data.split('\n'))

    @property
    def vertical(self) -> int:
        flipped = self.transpose(self.data.split('\n'))
        return self.count_horizonal(flipped)

    @property
    def diagonal(self) -> int:
        rows: list[str] = []
        tlbr = self.tlbr_transpose(self.data.split('\n'))
        rows.extend(tlbr)
        trbl = self.trbl_transpose(self.data.split('\n'))
        rows.extend(trbl)
        return self.count_horizonal(rows)

    def transpose(self, input_data) -> list[str]:
        new_data: list[str] = [""] * len(input_data[0])
        for row in input_data:
            for index, item in enumerate(row):
                new_data[index] += item
        return new_data

    def tlbr_transpose(self, input_data: list[str]) -> list[str]:
        new_data: list[str] = []
        vstart = 0
        while vstart <= len(input_data) - 4:
            hstart = 0
            while hstart <= len(input_data[0]) - 4:
                new_data.append("")
                for i in range(4):
                    new_data[-1] += input_data[i + vstart][i + hstart]
                hstart += 1
            vstart += 1
        return new_data

    def trbl_transpose(self, input_data: list[str]) -> list[str]:
        new_data: list[str] = []
        vstart = 0
        while vstart <= len(input_data) - 4:
            hstart = 1
            while hstart * -1 >= (len(input_data[0]) - 3) * -1:
                new_data.append("")
                for i in range(4):
                    new_data[-1] += input_data[i + vstart][(i + hstart) * -1]
                hstart += 1
            vstart += 1
        return new_data

    def is_x_mas(self, grid: list[list[str]]) -> bool:
        goal = ('MAS', 'SAM')
        forward = f"{grid[2][0]}{grid[1][1]}{grid[0][2]}".upper()
        backward = f"{grid[0][0]}{grid[1][1]}{grid[2][2]}".upper()
        return forward in goal and backward in goal

    def get_grid(self) -> list[list[str]]:
        grid: list[list[str]] = []
        for row in self.data.split():
            grid.append(list(row))
        return grid

    def get_3_x_3(self, x: int, y: int) -> list[list[str]]:
        grid = self.get_grid()
        return [
            grid[x][y:y+3],
            grid[x+1][y:y+3],
            grid[x+2][y:y+3],
        ]
        
    def get_grids(self) -> list[list[str]]:
        grids: list[list[str]] = []
        rows = self.data.split()
        for x in range(len(rows[0]) - 2):
            for y in range(len(rows) - 2):
                grids.append(self.get_3_x_3(x, y))
        return grids

