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

    def show_graph(self) -> None:
        """
        AND -> OR/AND
        XOR -> XOR/AND
        XOR & XOR -> Z
        """
        self.answer
        results = self.part_two()
        self._setup_commands()
        print("```mermaid")
        print("flowchart TB")
        for command in self.commands:
            a = command[0]
            b = command[2]
            c = command[-1]
            label = '<span style="color:#f00">XOR</style>' if command[1] == 'XOR' else ''
            if c.startswith('z'):
                if self.state[c] == results[c]:
                    print(f'style {c} fill:#0f0,color:#000')
                else:
                    # print(f'{c} is wrong')
                    print(f'style {c} fill:#f00,color:#000')
            print(f'{a}[{a} - {self.state[a]}] --{label}--> {c}[{c} - {self.state[c]}]')
            print(f'{b}[{b} - {self.state[b]}] --{label}--> {c}[{c} - {self.state[c]}]')
        print("```")

    def print_graph(self, structure: list, indent: int = 0) -> None:
        for item in structure:
            print(" " * indent + f'{item[0]}')
            if item[1]:
                self.print_graph(item[1], indent + 4)

    def find_parent(self, command: tuple[str, ...]) -> tuple[str, ...]:
        if command[0][0] in 'xy' and command[2][0] in 'xy':
            return []
        parents = []
        for parent in self.commands:
            if parent[-1] == command[0]:
                parents.append((parent, self.find_parent(parent)))
            if parent[-1] == command[2]:
                parents.append((parent, self.find_parent(parent)))
        return parents

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
