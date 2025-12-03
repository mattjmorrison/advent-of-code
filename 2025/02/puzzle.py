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
        length = len(string)

        for divisor in self.get_group_sizes(length):
            if string[:divisor] * (length//divisor) == string:
                return True
        else:
            return False


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

    def get_group_sizes(self, size):
        results = []
        for divisor in range(1, size // 2 + 1):
            if size % divisor == 0:
                results.append(divisor)
        return results
