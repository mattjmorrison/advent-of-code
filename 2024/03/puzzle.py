import re

class Puzzle:

    def __init__(self, data: str):
        self.data = data

    @property
    def answer(self) -> int:
        total = 0
        for a, b in self.strip:
            total += a * b
        return total

    @property
    def strip(self) -> list[tuple[int, int]]:
        results: list[tuple[int, int]] = []
        pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
        start = 0
        while match := pattern.search(self.data, start):
            start = match.start() + 1
            results.append((int(match.group(1)), int(match.group(2))))
        return results
