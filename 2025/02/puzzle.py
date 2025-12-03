class Puzzle:

    def __init__(self, input):
        self.input = input

    def parse(self):
        results = []
        for result in self.input.split(','):
            a, b = result.split('-')
            results.append((int(a), int(b)))
        return results

    def is_repeat(self, number):
        string = str(number)
        if len(string) % 2 != 0:
            # odds will never match
            return False

        size = len(string) // 2
        return string[:size] == string[size:]

    def get_repeats_in_range(self, start, end):
        results = []
        for number in range(start, end + 1):
            if self.is_repeat(number):
                results.append(number)
        return results

    def solve(self):
        total = 0
        for start, end in self.parse():
            total += sum(self.get_repeats_in_range(start, end))
        return total