class Puzzle:

    def __init__(self, input):
        self.input = input

    def parse(self):
        results = []
        for row in self.input.split('\n'):
            results.append([int(a) for a in list(row)])
        return results

    def calc_joltage_for_row(self, row):
        result = ''
        index = 0
        for end in range(-11, 0, 1):
            current = row[index:end]
            highest = max(current)
            index = row.index(highest, index) + 1
            result += str(highest)
        result += str(max(row[index:]))
        return int(result)

    def calc_total_joltage(self):
        results = []
        for row in self.parse():
            results.append(self.calc_joltage_for_row(row))
        return sum(results)
