class Puzzle:

    def __init__(self, input):
        self.input = input
        self.position = 50
        self.zeroes = 0

    def solve(self):
        for input in self.input.split('\n'):
            self.move(input)

    def move(self, instruction):
        direction = instruction[0]
        number = int(instruction[1:])
        while number > 0:
            if direction == 'R':
                if self.position + 1 == 100:
                    self.zeroes += 1
                    self.position = 0
                else:
                    self.position += 1
            else:
                if self.position - 1 == -1:
                    self.position = 99
                else:
                    self.position -= 1
                    if self.position == 0:
                        self.zeroes += 1
            number -= 1