from itertools import permutations
from functools import cache, cached_property


class Puzzle:

    def __init__(self, data: str):
        self.data = data

    @property
    def answer(self) -> int:
        result = 0
        for desired in self.desired:
            if self.arrange(desired):
                result += 1
        return result

    @cached_property
    def available(self) -> list[str]:
        return self.data.split('\n\n')[0].split(', ')

    @property
    def desired(self) -> list[str]:
        return self.data.split('\n\n')[1].split('\n')

    def match(self, desired: str, available: list[str]) -> str:
        for avail in available:
            print(avail, desired)
            if desired.startswith(avail):
                return desired.replace(avail, '', 1)
        return desired

    def arrange(self, desired: str) -> bool:
        counter = 0
        for avail in permutations(self.available):
            des = desired
            while des := self.match(des, avail):
                counter += 1
                if counter > len(avail) * len(des) + 100000:
                    break
        return not des

    def part_one(self, desired):
        return len(self.solution_loop(desired))
    
    def part_two(self, desired):
        return sum(self.solution_loop(desired))
    
    def solution_loop(self, desired):
        return [r for r in map(self.count, desired) if r]

    @cache
    def count(self, desired):
        return sum(self.count(desired.replace(a, '', 1)) for a in self.available if desired.startswith(a)) or desired == ''
