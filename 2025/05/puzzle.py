class Puzzle:

    def __init__(self, input):
        self.input: str = input

    def parse(self):
        fresh_range_section, available = self.input.split('\n\n')
        fresh_ranges = fresh_range_section.split('\n')

        fresh = []
        for item in fresh_ranges:
            fresh.append([int(a) for a in item.split('-')])

        return fresh, [int(x) for x in available.split('\n')]

    def solve_part_one(self):
        fresh, available = self.parse()
        count = 0
        for item in available:
            for low, high in fresh:
                if low <= item <= high:
                    count += 1
                    break
        return count

    def combine(self, items):
        items.sort(key=lambda i: i[0])
        combined = [items[0]]
        for current in items[1:]:
            end = combined[-1]
            if current[0] <= end[1]:
                end[1] = max(end[1], current[1])
            else:
                combined.append(current)
        return combined

    def solve_part_two(self):
        fresh_ranges, _ = self.parse()
        total = 0
        for start, end in self.combine(fresh_ranges):
            total += end + 1 - start
        return total
