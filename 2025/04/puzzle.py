class Puzzle:

    def __init__(self, input):
        self.input = input

    def parse(self):
        results = []
        for row in self.input.split('\n'):
            results.append(list(row))
        return results

    def solve_part_one(self):
        count = 0
        grid = self.parse()
        for roll_row, roll_column in self.get_paper_rolls(grid):
            neighbors = self.get_neighbors(roll_row, roll_column, grid)
            if neighbors.count('@') < 4:
                count += 1
        return count

    def show_grid(self, grid):
        for row in grid:
            print(row)


    def solve_part_two(self):
        count = 0
        grid = self.parse()
        while True:
            starting_count = count
            for roll_row, roll_column in self.get_paper_rolls(grid):
                neighbors = self.get_neighbors(roll_row, roll_column, grid)
                if neighbors.count('@') < 4:
                    count += 1
                    grid[roll_row][roll_column] = 'X'
            print(f"Starting Count: {starting_count} Count: {count}")
            if starting_count == count:
                break
        return count


    def get_paper_rolls(self, grid):
        results = []
        for row_index, row in enumerate(grid):
            for column_index, column in enumerate(row):
                if column == '@':
                    results.append((row_index, column_index))
        return results


    def get_neighbors(self, row, column, grid):
        neighbors = []
        for r_index in (-1, 0, 1):
            for c_index in (-1, 0, 1):
                if r_index == c_index == 0:
                    continue
                row_index = row + r_index
                column_index = column + c_index
                if row_index < 0 or column_index < 0:
                    continue
                try:
                    neighbors.append(grid[row_index][column_index])
                except IndexError:
                    pass
        return neighbors
