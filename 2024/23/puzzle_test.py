from puzzle import Puzzle


EXAMPLE = """
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
""".strip()


def test_example() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.answer == 0


def test_parse() -> None:
    puzzle = Puzzle(EXAMPLE)
    result = puzzle.triads
    for r in result:
        print(r)
    
    for expected in [
        # {'aq', 'cg', 'yn'},
        # {'aq', 'vc', 'wq'},
        # {'co', 'de', 'ka'},
        {'co', 'de', 'ta'},
        {'co', 'ka', 'ta'},
        {'de', 'ka', 'ta'},
        # {'kh', 'qp', 'ub'},
        {'qp', 'td', 'wh'},
        {'tb', 'vc', 'wq'},
        {'tc', 'td', 'wh'},
        {'td', 'wh', 'yn'},
        # {'ub', 'vc', 'wq'},
    ]:
        assert expected in result

"""
{'ub', 'qp', 'kh'}
{'td', 'kh', 'wh'}
{'tc', 'td', 'wh'}
{'qp', 'td', 'wh'}
{'yn', 'aq', 'cg'}
{'yn', 'td', 'wh'}
{'wq', 'vc', 'cg'}
{'aq', 'vc', 'wq'}
{'ub', 'vc', 'wq'}
{'wq', 'vc', 'tb'}

['tc', 'qp', 'ub', 'ta', 'kh']
['kh', 'wh', 'td', 'co', 'tc']
['kh', 'ub', 'td', 'wh', 'qp']
['cg', 'co', 'ta', 'ka', 'de'] co ka de
['de', 'tb', 'yn', 'aq', 'cg']
['co', 'tb', 'ta', 'de', 'ka'] co de ka
['ka', 'ta', 'de', 'tc', 'co'] co de ka
['aq', 'cg', 'wh', 'td', 'yn']
['yn', 'vc', 'cg', 'wq', 'aq']
['qp', 'kh', 'wq', 'vc', 'ub']
['cg', 'ka', 'wq', 'vc', 'tb']
['aq', 'ub', 'wq', 'tb', 'vc']
['tc', 'td', 'yn', 'qp', 'wh']
['co', 'ka', 'de', 'kh', 'ta']
['tc', 'wh', 'qp', 'yn', 'td']
['tb', 'ub', 'aq', 'vc', 'wq']
"""