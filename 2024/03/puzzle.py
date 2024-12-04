import re

PATTERN = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')


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
        sections = self.data.split("don't()")
        results.extend(self.get_results(sections[0]))
        for section in sections[1:]:
            good_section = section.split('do()')[1:]
            for good in good_section:
                results.extend(self.get_results(good))
        return results

    def get_results(self, section: str) -> list[tuple[int, int]]:
        start: int = 0
        results: list[tuple[int, int]] = []
        while match := PATTERN.search(section, start):
            start = match.start() + 1
            results.append((int(match.group(1)), int(match.group(2))))
        return results
