from puzzle import Puzzle
from data import DATA


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
    assert puzzle.answer == 7


def test_part_one() -> None:
    puzzle = Puzzle(DATA)
    assert puzzle.answer == 1306


def test_part_two() -> None:
    puzzle = Puzzle(DATA)
    assert puzzle.part_two == 'bd,dk,ir,ko,lk,nn,ob,pt,te,tl,uh,wj,yl'


def test_part_two_example() -> None:
    puzzle = Puzzle(EXAMPLE)
    assert puzzle.part_two == 'co,de,ka,ta'


# def test_find_largest_set() -> None:
#     puzzle = Puzzle(EXAMPLE)
#     results = puzzle.find_largest_set('kh', set())
#     assert results == tuple(sorted(('co', 'de', 'ka', 'ta')))


def test_parse() -> None:
    puzzle = Puzzle(EXAMPLE)
    result = puzzle.triads
    for r in result:
        print(r)
    
    for expected in [
        ('co', 'de', 'ta'),
        ('co', 'ka', 'ta'),
        ('de', 'ka', 'ta'),
        ('qp', 'td', 'wh'),
        ('tb', 'vc', 'wq'),
        ('tc', 'td', 'wh'),
        ('td', 'wh', 'yn'),
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
