class Puzzle:

    def __init__(self, input):
        self.input = input

    def parse(self):
        results = []
        for row in self.input.split('\n'):
            results.append([int(a) for a in list(row)])
        return results

    def find_max(self, row):
        return max(row[:-1])

    def find_max_pos(self, row):
        return row.index(self.find_max(row))

    def find_max_after_max(self, row):
        index = self.find_max_pos(row)
        return max(row[index+1:])

    def calc_joltage_for_row(self, row):
        left = self.find_max(row)
        right = self.find_max_after_max(row)
        return int(f'{left}{right}')

    def calc_total_joltage(self):
        results = []
        for row in self.parse():
            results.append(self.calc_joltage_for_row(row))
        return sum(results)
