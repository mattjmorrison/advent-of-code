
class Puzzle:

    def __init__(self, input):
        self.input: str = input

    def parse(self):
        results = {}
        for line in self.input.splitlines():
            device, devices = line.split(':')
            results[device] = devices.strip().split(' ')
        return results

    def solve_part_one(self):
        data = self.parse()

        def trace(start):
            paths = 0
            for new_start in data[start]:
                if new_start == 'out':
                    paths += 1
                    continue
                paths += trace(new_start)
            return paths

        return trace('you')

    def solve_part_two(self):
        data = self.parse()

        def trace(start, trail):
            paths = 0
            for new_start in data[start]:
                if new_start == 'out':
                    # if len(set(['fft', 'dac']).intersection(set(trail))) == 2:
                    paths += 1
                    continue
                if new_start in ('fft', 'dac'):
                    paths += trace(new_start, trail + [new_start])
                else:
                    paths += trace(new_start, trail)
            return paths

        return trace('svr', [])
            

    # similar depth first search
    # def part_two(self):
    #     input = [list(i) for i in self.input.split('\n')]
    #     max_row = len(input)
    #     max_col = len(input[0]) - 1
    #     paths = defaultdict(int)

    #     def beam(row, col):
    #         if paths[(row, col)]:
    #             return paths[(row, col)]

    #         while row < max_row and input[row][col] != '^':
    #             row += 1

    #         if row == max_row:
    #             return 1

    #         if paths[(row, col)]:
    #             return paths[(row, col)]

    #         if col > 0:
    #             paths[(row, col)] = beam(row, col - 1)
    #         if col < max_col:
    #             paths[(row, col)] += beam(row, col + 1)
    #         return paths[(row, col)]

    #     return beam(0, input[0].index('S'))