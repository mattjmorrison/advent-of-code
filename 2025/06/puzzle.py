import re
import operator
from functools import reduce

OPS = {
    '*': operator.mul,
    '+': operator.add
}


class Puzzle:

    def __init__(self, input):
        self.input: str = input

    def parse(self):
        rows = []
        data = self.input.split('\n')
        for row in data[:-1]:
            rows.append([int(x) for x in re.split('\s+', row.strip())])
        operators = re.split('\s+', data[-1:][0].strip())
        rows.append(operators)
        return list(zip(*rows))

    def calc_row(self, row):
        op = row[-1]
        return reduce(OPS[op], row[:-1])

    def solve_part_one(self):
        data = self.parse()
        total = []
        for row in data:
            total.append(self.calc_row(row))
        return sum(total)