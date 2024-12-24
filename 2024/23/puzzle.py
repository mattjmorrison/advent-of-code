from collections import defaultdict
from functools import cached_property


class Puzzle:

    def __init__(self, data: str):
        self.data = data

    @property
    def answer(self) -> int:
        return 0

    @cached_property
    def split_computers(self) -> list[list[str]]:
        computers = defaultdict(list)
        for row in self.data.split('\n'):
            first, second = row.split('-')
            computers[first].append(second)
            computers[second].append(first)
        results = []
        for k, v in computers.items():
            if any([x.startswith('t') for x in v]):
                results.append(set(v + [k]))
        return results

    @property
    def triads(self) -> list[set[str, str, str]]:
        results = []
        for set_one in self.split_computers:
            for set_two in self.split_computers:
                if set_one == set_two:
                    continue
                combo = set_one.intersection(set_two)
                if len(combo) == 3 and combo not in results:
                    results.append(combo)
        return results
