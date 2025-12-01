
START = 50
MAX = 99
MIN = 0


class Puzzle:

    def __init__(self, input: str):
        self.input = input
        self.zeroes = 0

    def get_moves(self):
        moves = []
        rows = self.input.strip().split('\n')
        for row in rows:
            row = row.strip()
            number = int(row[1:])
            if row.startswith('L'):
                moves.append(-1 * number)
            else:
                moves.append(number)
        return moves

    def solve(self):
        current = START
        for move in self.get_moves():
            current = self.find_spot(current + move)
            print(f"Move: {move} Current: {current}")
            if current == 0:
                self.zeroes += 1

    def find_spot(self, number):
        while number < 0 or number > 99:
            print(f"Adjusting {number}")
            if number < 0:
                number = 100 + number
                print(f"Adjusted < 0: {number}")
            if number > 99:
                number = number - 100
                print(f"Adjusted > 99: {number}")
        print(f"Done: {number}")
        return number
