from collections import defaultdict
from functools import cached_property


class Puzzle:

    def __init__(self, data: str):
        self.data = data

    @property
    def answer(self) -> int:
        return len(self.triads)
    
    @property
    def part_two(self) -> str:
        answer = set()
        # answer.add(('ka', 'co', 'ta', 'de'))
        # answer.add(('a', 'b', 'c'))

        for computer in self.split_computers:
            self.find_connected_sets(computer, {computer}, answer)

        return ",".join(sorted(max(answer, key=len)))

    @cached_property
    def split_computers(self) -> dict[set[str]]:
        computers = defaultdict(set)
        for row in self.data.split('\n'):
            first, second = row.split('-')
            computers[first].add(second)
            computers[second].add(first)
        return computers

    @property
    def triads(self) -> list[set[str, str, str]]:
        results = set()
        for computer1 in self.split_computers:
            for computer2 in self.split_computers[computer1]:
                for computer3 in self.split_computers[computer2]:
                    if computer1 != computer3 and computer1 in self.split_computers[computer3]:
                        triad = (computer1, computer2, computer3)
                        if any(t.startswith('t') for t in triad):
                            results.add(tuple(sorted((computer1, computer2, computer3))))
        return results

    def find_connected_sets(self, computer: str, connected: set[str], answer: set[str]) -> None:
        connections = tuple(sorted(connected))
        if connections in answer:
            return
        answer.add(connections)
        for other in self.split_computers[computer]:
            if other in connected:
                continue
            if not connected <= self.split_computers[other]:
                continue
            self.find_connected_sets(other, {*connected, other}, answer)
