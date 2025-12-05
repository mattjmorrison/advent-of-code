class Puzzle:

    def __init__(self, input):
        self.input: str = input

    def parse(self):
        fresh_range_section, available = self.input.split('\n\n')
        fresh_ranges = fresh_range_section.split('\n')

        fresh = []
        for item in fresh_ranges:
            fresh.append(tuple([int(a) for a in item.split('-')]))

        return fresh, [int(x) for x in available.split('\n')]

    def solve_part_one(self):
        fresh, available = self.parse()
        count = 0
        for item in available:
            print(f"Item: {item}")
            for low, high in fresh:
                if low <= item <= high:
                    print(f'low:{low} < item:{item} < high:{high}')
                    count += 1
                    break
        return count

    def solve_part_two(self):
        fresh_ranges, _ = self.parse()

        sorted_ranges = sorted(fresh_ranges)

        combined_ranges = []
        for low, high in sorted_ranges:
            for l2, h2 in sorted_ranges:
                if l2 < low < h2:
                    combined_ranges.append((low, h2))
                    break
            else:
                combined_ranges.append((low, high))

        print(combined_ranges)



        # for low in low_sorted_ranges:
        #     print(low)

        # for high in high_sorted_ranges:
        #     print(high)

        # for low, high in sorted_ranges:
        #     print(range(low, high+1))

        return 0
