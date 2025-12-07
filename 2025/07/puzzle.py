from time import sleep
from collections import deque, defaultdict

class Puzzle:

    def __init__(self, input):
        self.input: str = input

    def get_indexes(self, row):
        return [i for i, chr in enumerate(row) if chr == '^']

    def part_one(self):
        rows = self.input.split('\n')
        beams = [rows[0].index('S')]

        splits = 0
        for row in rows[1:]:
            new_beams = []
            for beam in beams:
                if row[beam] == '.':
                    new_beams.append(beam)
                elif row[beam] == '^':
                    splits += 1
                    if row[beam-1] == '.':
                        new_beams.append(beam-1)
                    if row[beam+1] == '.':
                        new_beams.append(beam+1)
            beams = list(sorted(list(set(new_beams))))
        return splits

    def part_two(self):
        input = [list(i) for i in self.input.split('\n')]
        max_row = len(input)
        max_col = len(input[0]) - 1
        paths = defaultdict(int)

        def beam(row, col):
            if paths[(row, col)]:
                return paths[(row, col)]

            while row < max_row and input[row][col] != '^':
                row += 1

            if row == max_row:
                return 1

            if paths[(row, col)]:
                return paths[(row, col)]

            if col > 0:
                paths[(row, col)] = beam(row, col - 1)
            if col < max_col:
                paths[(row, col)] += beam(row, col + 1)
            return paths[(row, col)]

        return beam(0, input[0].index('S'))
