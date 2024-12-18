import re


class Puzzle:

    def __init__(self, data: str):
        self.data = data
        self._reg: dict[str, int] = {}
        self._output: list[int] = []
        self._commands: list[tuple[str, str]] = []
        self.next_instruction = 0
        self.original_program = ""
        self.opcode = {
            "0": self.adv,
            "1": self.bxl,
            "2": self.bst,
            "3": self.jnz,
            "4": self.bxc,
            "5": self.out,
            "6": self.bdv,
            "7": self.cdv,
        }

    def _parse_registers(self, register: str) -> int:
        if register not in self._reg:
            for item in self.data.split("\n\n")[0].split("\n"):
                result = re.search(rf"Register {register}: (\d+)", item)
                if result:
                    self._reg[register] = int(result.group(1))
        return self._reg[register]

    @property
    def commands(self) -> list[tuple[str, str]]:
        if not self._commands:
            item = self.data.split("\n\n")[1]
            self.original_program = item.split('Program: ')[-1]
            nums = iter(self.original_program.split(','))
            self._commands = list(zip(nums, nums))
        return self._commands

    @property
    def output(self) -> str:
        return ','.join(str(a) for a in self._output)

    @property
    def reg_a(self) -> int:
        return self._parse_registers("A")

    @reg_a.setter
    def reg_a(self, val: int) -> None:
        self._reg["A"] = val

    @property
    def reg_b(self) -> int:
        return self._parse_registers("B")

    @reg_b.setter
    def reg_b(self, val: int) -> None:
        self._reg['B'] = val

    @property
    def reg_c(self) -> int:
        return self._parse_registers("C")

    @reg_c.setter
    def reg_c(self, val: int) -> None:
        self._reg['C'] = val

    @property
    def answer(self) -> str:
        while self.next_instruction < len(self.commands):
            opcode, operand = self.commands[self.next_instruction]
            # print(f"Next: {self.next_instruction} Opscode: {opcode} Operand: {operand}")
            # print(f'''
            #     A: {self.reg_a} B: {self.reg_b} C: {self.reg_c} 
            #     O: {self.output}
            # ''')
            self.instruction(opcode, operand)
            # print(f'''
            #     A: {self.reg_a} B: {self.reg_b} C: {self.reg_c} 
            #     O: {self.output}
            # ''')
            self.next_instruction += 1
        return self.output

    def get_operand(self, raw: str) -> int:
        match raw:
            case "4":
                return self.reg_a
            case "5":
                return self.reg_b
            case "6":
                return self.reg_c
            case _:
                return int(raw)
        return int(raw)

    def instruction(self, opcode: str, operand: str) -> None:
        self.opcode[opcode](operand)

    def adv(self, operand: str) -> None:
        op = self.get_operand(operand)
        self.reg_a = int(self.reg_a / (2**op))

    def bxl(self, operand: str) -> None:
        self.reg_b = self.reg_b ^ int(operand)

    def bst(self, operand: str) -> None:
        self.reg_b = self.get_operand(operand) % 8

    def jnz(self, operand: str) -> None:
        if self.reg_a != 0:
            self.next_instruction = int(operand) - 1

    def bxc(self, operand: str) -> None:
        self.reg_b = self.reg_b ^ self.reg_c

    def out(self, operand: str) -> None:
        self._output.append(self.get_operand(operand) % 8)

    def bdv(self, operand: str) -> None:
        op = self.get_operand(operand)
        self.reg_b = int(self.reg_a / (2**op))

    def cdv(self, operand: str) -> None:
        op = self.get_operand(operand)
        self.reg_c = int(self.reg_a / (2**op))
