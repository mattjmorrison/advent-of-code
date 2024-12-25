from functools import cached_property

class Puzzle:

    def __init__(self, data: str):
        self.data = data
        self.state = {}
        self._setup_state()
        self.commands = []
        self._setup_commands()

    def part_two(self) -> dict[str, int]:
        final_z = {}
        first_bin_number = ''
        second_bin_number = ''
        for first in range(99, -1, -1):
            if f'x{first:0>2}' in self.state:
                first_bin_number += str(self.state[f'x{first:0>2}'])
        for second in range(99, -1, -1):
            if f'y{second:0>2}' in self.state:
                second_bin_number += str(self.state[f'y{second:0>2}'])

        result = list(str(bin(int(first_bin_number, 2) + int(second_bin_number, 2)))[2:])

        for answer in range(100):
            if not result:
                break
            final_z[f'z{answer:0>2}'] = int(result.pop(-1))

        return final_z

    @property
    def answer(self) -> int:
        while command := self.commands and self.commands.pop(0):
            if command[0] in self.state and command[2] in self.state:
                self.command(command)
            else:
                self.commands.append(command)
        results = ''
        for i in range(99, -1, -1):
            key = f'z{i:0>2}'
            if key in self.state:
                results += str(self.state[key])
        return int(results, 2)

    def _setup_state(self) -> None:
        for row in self.data.split('\n\n')[0].split('\n'):
            key, val = row.split(': ')
            self.state[key] = int(val)

    def _setup_commands(self) -> None:
        for row in self.data.split('\n\n')[1].split('\n'):
            l, o, r, _, a = row.split(' ')
            self.commands.append((l, o, r, a))

    def command(self, command: tuple[str, ...]):
        if command[1] == 'AND':
            self.state[command[-1]] = self.state[command[0]] and self.state[command[2]]
        elif command[1] == 'OR':
            self.state[command[-1]] = self.state[command[0]] or self.state[command[2]]
        elif command[1] == 'XOR':
            self.state[command[-1]] = int(self.state[command[0]] != self.state[command[2]])
