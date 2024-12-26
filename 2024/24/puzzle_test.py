from puzzle import Puzzle
from data import DATA


EXAMPLE = """
x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02
""".strip()


BIG_EXAMPLE = """
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
""".strip()


def test_part_one() -> None:
    puzzle = Puzzle(DATA)
    assert puzzle.answer == 47666458872582


def test_part_two() -> None:
    puzzle = Puzzle(DATA)
    puzzle.answer
    new_state = puzzle.part_two()
    for i in range(100):
        key = f'z{i:0>2}'
        if key in puzzle.state and key in new_state:
            if puzzle.state[key] != new_state[key]:
                print(f'{key}: {puzzle.state[key]} & {new_state[key]}')


    # swap one
    # y05 AND x05 -> sgt
    # y05 XOR x05 -> tvp
    # ggh XOR tvp -> jst # swap
    # ggh AND tvp -> bhb # swap
    # sgt OR bhb -> z05


    # swap two
    """
    xor -> and + or
    or -> and + and
    and -> or + xor


    mcm XOR tdw -> z10
        x10 AND y10 -> mcm - x
        mcc OR hrq -> tdw - x
            y09 AND x09 -> hrq - x
            mnk AND cgq -> mcc - x
                x09 XOR y09 -> mnk - x
                njs OR njd -> cgq - x
                    y08 AND x08 -> njd - x 
                    vbk AND mnn -> njs - x
                        x08 XOR y08 -> mnn - x
                        qrm OR hpv -> vbk - x
                            x07 AND y07 -> qrm - x
                            wht AND shw -> hpv - x
                                y07 XOR x07 -> wht - x
                                fsb OR vvg -> shw - x
                                    y06 AND x06 -> fsb - x
                                    vjh AND jst -> vvg - x
                                        y06 XOR x06 -> vjh
                                        ggh AND tvp -> jst
                                            y05 XOR x05 -> tvp
                                            rkg OR kff -> ggh
                                                x04 AND y04 -> kff
                                                bjc AND tkj -> rkg
                                                    y04 XOR x04 -> bjc
                                                    vvj OR mkv -> tkj
                                                        x03 AND y03 -> vvj
                                                        whn AND vmd -> mkv
                                                            x03 XOR y03 -> vmd
                                                            vbm OR vgh -> whn
                                                                x02 AND y02 -> vgh
                                                                mdw AND gsh -> vbm
                                                                    y02 XOR x02 -> mdw
                                                                    gpt OR bkg -> gsh
                                                                        y01 AND x01 -> bkg
                                                                        rpj AND nsc -> gpt
                                                                            y01 XOR x01 -> nsc
                                                                            y00 AND x00 -> rpj




                                
                            
            y09 AND x09 -> hrq


    """

    #- tdw AND mcm -> pqq
    
    
    #- tdw AND mcm -> pqq
    
    # y06 AND x06 -> fsb
    # y07 XOR x07 -> wht
    # vjh AND jst -> vvg
    # fsb OR vvg -> shw
    # x09 XOR y09 -> mnk
    # x07 AND y07 -> qrm
    # wht AND shw -> hpv
    # qrm OR hpv -> vbk
    # x08 XOR y08 -> mnn
    # vbk AND mnn -> njs
    # 
    # y08 AND x08 -> njd
    # njs OR njd -> cgq
    # mnk AND cgq -> mcc
    # y09 AND x09 -> hrq
    # 

    


    # for key, value in puzzle.state.items():
    #     if key.startswith('z') and key in new_state:
    #         if value != new_state[key]:
    #             print(key, value, new_state[key])
    assert False


# def test_part_two_example() -> None:
#     data = """
# x00: 0
# x01: 1
# x02: 0
# x03: 1
# x04: 0
# x05: 1
# y00: 0
# y01: 0
# y02: 1
# y03: 1
# y04: 0
# y05: 1

# x00 AND y00 -> z05
# x01 AND y01 -> z02
# x02 AND y02 -> z01
# x03 AND y03 -> z03
# x04 AND y04 -> z04
# x05 AND y05 -> z00
#     """.strip()
#     puzzle = Puzzle(data)
#     puzzle.answer
#     new_state = puzzle.part_two()
#     for key, value in puzzle.state.items():
#         if key.startswith('z') and key in new_state:
#             if value != new_state[key]:
#                 print(key, value, new_state[key])
#     assert False


def test_example() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.answer == 4


def test_big_example() -> None:
    puzzle = Puzzle(BIG_EXAMPLE)
    assert puzzle.answer == 2024


def test_load_state() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.state == {
        'x00': 1,
        'x01': 1,
        'x02': 1,
        'y00': 0,
        'y01': 1,
        'y02': 0,
    }


def test_load_commands() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.commands == [
        ('x00', 'AND', 'y00', 'z00'),
        ('x01', 'XOR', 'y01', 'z01'),
        ('x02', 'OR', 'y02', 'z02'),
    ]


def test_and_command() -> None:
    puzzle = Puzzle(EXAMPLE)
    puzzle.command(('x00', 'AND', 'y00', 'z00'))
    assert puzzle.state['z00'] == 0


def test_xor_command() -> None:
    puzzle = Puzzle(EXAMPLE)
    puzzle.command(('x01', 'XOR', 'y01', 'z01'))
    assert puzzle.state['z01'] == 0


def test_or_command() -> None:
    puzzle = Puzzle(EXAMPLE)
    puzzle.command(('x02', 'OR', 'y02', 'z02'))
    assert puzzle.state['z02'] == 1


def test_create_part_two_commands() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.answer == 4
    assert puzzle.state == {
        'x00': 1,
        'x01': 1,
        'x02': 1,

        'y00': 0,
        'y01': 1,
        'y02': 0,

        'z00': 0,
        'z01': 0,
        'z02': 1,
    }

    # 0: 1 & 0 == 0
    # 1: 1 & 1 == 1
    # 2: 1 & 0 == 0

def test_binary_addition() -> None:
    puzzle = Puzzle(EXAMPLE)
    puzzle.state = {
        'x00': 1,
        'x01': 1,
        'x02': 1,
        'x03': 1,
        'x04': 1,
        'x05': 1,

        'y00': 1,
        'y01': 1,
        'y02': 1,
        'y03': 1,
        'y04': 1,
        'y05': 1,
    }

    state = puzzle.part_two()

    assert state['z00'] == 0
    assert state['z01'] == 1
    assert state['z02'] == 1
    assert state['z03'] == 1
    assert state['z04'] == 1
    assert state['z05'] == 1
    assert state['z06'] == 1


def test_graph() -> None:
    puzzle = Puzzle(DATA)
    puzzle.show_graph()
    assert False