from puzzle import Puzzle
from data import DATA

EXAMPLE = """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
""".strip()

EXAMPLE_PART_TWO = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
""".strip()


def test_part_two_example() -> None:
    puzzle = Puzzle(EXAMPLE_PART_TWO)
    puzzle.reg_a = 117440
    assert puzzle.answer == puzzle.original_program


def test_part_two(start=0) -> None:
    puzzle = Puzzle(DATA)
    puzzle.answer
    program = puzzle.original_program.split(',')

    def run_program(a):
        p = Puzzle(DATA)
        p.reg_a = a
        return p.answer

    def check(count, start):
        for i in range(8):
            reg_a = start * 8 + i
            result = run_program(reg_a)
            print(f'Result: {result} - Count: {",".join(program[count:])}')
            if result == ",".join(program[count:]):
                if count == 0:
                    return reg_a
                r = check(count - 1, reg_a)
                if r is not None:
                    return r

    assert check(len(program) - 1, 0) == 202991746427434
    assert False


def test_part_one() -> None:
    puzzle = Puzzle(DATA)
    # assert puzzle.answer == "6,7,5,2,1,2,1,1,1"  # incorrect
    assert puzzle.answer == '7,4,2,0,5,0,5,3,7'


def test_example_one() -> None:
    data = """
Register A: 0
Register B: 0
Register C: 9

Program: 2,6
    """.strip()
    puzzle = Puzzle(data)
    puzzle.answer
    assert puzzle.reg_b == 1


def test_example_two() -> None:
    data = """
Register A: 10
Register B: 0
Register C: 0

Program: 5,0,5,1,5,4
    """.strip()
    puzzle = Puzzle(data)
    assert puzzle.answer == '0,1,2'


def test_example_three() -> None:
    data = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
    """.strip()
    puzzle = Puzzle(data)
    assert puzzle.answer == '4,2,5,6,7,7,7,7,3,1,0'
    assert puzzle.reg_a == 0


def test_example_four() -> None:
    data = """
Register A: 0
Register B: 29
Register C: 0

Program: 1,7
    """.strip()
    puzzle = Puzzle(data)
    puzzle.answer
    assert puzzle.reg_b == 26


def test_example_five() -> None:
    data = """
Register A: 0
Register B: 2024
Register C: 43690

Program: 4,0
    """.strip()
    puzzle = Puzzle(data)
    puzzle.answer
    assert puzzle.reg_b == 44354


def test_example() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.answer == "4,6,3,5,6,3,5,2,1,0"


def test_parse_commands() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.commands == [
        ('0', '1'),
        ('5', '4'),
        ('3', '0'),
    ]
    assert puzzle.next_instruction == 0


def test_parse_example() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.reg_a == 729
    assert puzzle.reg_b == 0
    assert puzzle.reg_c == 0


# @pytest.mark.parametrize(
#     "opcode, opcode_func",
#     (
#         ("0", Puzzle("").adv),
#         ("1", Puzzle("").bxl),
#         ("2", Puzzle("").bst),
#         ("3", Puzzle("").jnz),
#         ("4", Puzzle("").bxc),
#         ("5", Puzzle("").out),
#         ("6", Puzzle("").bdv),
#         ("7", Puzzle("").cdv),
#     ),
#         # 0,1,5,4,3,0
#         # adv(1) - out(4) - jnz(0)
# )
# def test_opcode_lookup(opcode: str, opcode_func: Callable) -> None:
#     puzzle = Puzzle("")
#     assert puzzle.opcode[opcode] == opcode_func


def test_operands() -> None:
    data = """
Register A: 9
Register B: 8
Register C: 7
    """.strip()
    puzzle = Puzzle(data)
    assert puzzle.get_operand("0") == 0
    assert puzzle.get_operand("1") == 1
    assert puzzle.get_operand("2") == 2
    assert puzzle.get_operand("3") == 3
    assert puzzle.get_operand("4") == 9
    assert puzzle.get_operand("5") == 8
    assert puzzle.get_operand("6") == 7


def test_adv() -> None:
    """
    The adv instruction (opcode 0) performs division. The numerator is the value in
    the A register. The denominator is found by raising 2 to the power of the
    instruction's combo operand. (So, an operand of 2 would divide A by 4 (2^2); an
    operand of 5 would divide A by 2^B.) The result of the division operation is
    truncated to an integer and then written to the A register.
    """
    data = """
Register A: 2
Register B: 1
Register C: 0
    """.strip()
    puzzle = Puzzle(data)
    puzzle.adv("2")
    assert puzzle.reg_a == 0
    puzzle = Puzzle(data)
    puzzle.adv("5")
    assert puzzle.reg_a == 1
    puzzle = Puzzle(data)
    puzzle.adv("6")
    assert puzzle.reg_a == 2
    puzzle = Puzzle(data)
    puzzle.instruction("0", "5")
    assert puzzle.reg_a == 1


def test_bxl() -> None:
    """
    The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the
    instruction's literal operand, then stores the result in register B.
    """
    data = """
Register B: 1
    """.strip()
    puzzle = Puzzle(data)
    puzzle.bxl("1")
    assert puzzle.reg_b == 0
    puzzle.bxl("2")
    assert puzzle.reg_b == 2
    puzzle.bxl("5")
    assert puzzle.reg_b == 7


def test_bst() -> None:
    """
    The bst instruction (opcode 2) calculates the value of its combo operand modulo 8
    (thereby keeping only its lowest 3 bits), then writes that value to the B register.
    """
    data = """
Register B: 999
    """.strip()
    puzzle = Puzzle(data)
    puzzle.bst("8")
    assert puzzle.reg_b == 0
    puzzle.bst("9")
    assert puzzle.reg_b == 1
    puzzle.bst("13")
    assert puzzle.reg_b == 5


def test_jnz() -> None:
    """
    The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the
    A register is not zero, it jumps by setting the instruction pointer to the value of
    its literal operand; if this instruction jumps, the instruction pointer is not
    increased by 2 after this instruction.
    """
    data = """
Register A: 0
Register B: 1
Register C: 2
    """.strip()
    puzzle = Puzzle(data)
    puzzle.jnz("3")
    assert puzzle.reg_a == 0
    assert puzzle.reg_b == 1
    assert puzzle.reg_c == 2


def test_bxc() -> None:
    """
    The bxc instruction (opcode 4) calculates the bitwise XOR of register B and
    register C, then stores the result in register B. (For legacy reasons, this
    instruction reads an operand but ignores it.)
    """
    data = """
Register A: 1
Register B: 1
Register C: 2
    """.strip()
    puzzle = Puzzle(data)
    puzzle.bxc("0")
    assert puzzle.reg_b == 3
    puzzle.reg_c = 4
    puzzle.bxc("0")
    assert puzzle.reg_b == 7


def test_out() -> None:
    """
    The out instruction (opcode 5) calculates the value of its combo operand modulo 8,
    then outputs that value. (If a program outputs multiple values, they are separated
    by commas.)
    """
    puzzle = Puzzle("")
    puzzle.out("0")
    assert puzzle.output == "0"
    puzzle.out("11")
    assert puzzle.output == "0,3"
    puzzle.out("41")
    assert puzzle.output == "0,3,1"


def test_bdv() -> None:
    """
    The bdv instruction (opcode 6) works exactly like the adv instruction except that
    the result is stored in the B register. (The numerator is still read from the A
    register.)
    """
    data = """
Register A: 2
Register B: 1
Register C: 0
    """.strip()
    puzzle = Puzzle(data)
    puzzle.bdv("2")
    assert puzzle.reg_b == 0
    puzzle = Puzzle(data)
    puzzle.bdv("5")
    assert puzzle.reg_b == 1
    puzzle = Puzzle(data)
    puzzle.bdv("6")
    assert puzzle.reg_b == 2
    puzzle = Puzzle(data)
    puzzle.instruction("6", "5")
    assert puzzle.reg_b == 1


def test_cdv() -> None:
    """
    The cdv instruction (opcode 7) works exactly like the adv instruction except that
    the result is stored in the C register. (The numerator is still read from the A
    register.)
    """
    data = """
Register A: 2
Register B: 1
Register C: 0
    """.strip()
    puzzle = Puzzle(data)
    puzzle.cdv("2")
    assert puzzle.reg_c == 0
    puzzle = Puzzle(data)
    puzzle.cdv("5")
    assert puzzle.reg_c == 1
    puzzle = Puzzle(data)
    puzzle.cdv("6")
    assert puzzle.reg_c == 2
    puzzle = Puzzle(data)
    puzzle.instruction("7", "5")
    assert puzzle.reg_c == 1
