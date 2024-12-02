from collections import Counter


class Puzzle:

    def __init__(self, data: str):
        self.data = data

    def count_safe(self) -> int:
        results = []
        for row in self.data.split('\n'):
            result = self.is_safe([int(a) for a in row.split()])
            # if not result:
            #     print(row, result)
            results.append(result)
        return Counter(results)[True]

    def count_safe_two(self) -> int:
        results = []
        for row in self.data.split('\n'):
            result = self.is_safe_two([int(a) for a in row.split()])
            # if not result:
            #     print("HERE:", row, result)
            results.append(result)
        return Counter(results)[True]

    def is_safe(self, report: list[int]) -> bool:
        results = []
        direction = 0
        for a, b in zip(report, report[1:]):
            diff = b - a

            if direction == 0:
                direction = -1 if diff < 0 else 1

            if diff > 0 > direction or diff < 0 < direction:
                results.append(False)

            results.append(abs(diff) in (1, 2, 3))
        return all(results)

    def is_safe_two(self, report: list[int]) -> bool:
        return bool(self.find_good_rank(report))

    def rank(self, report: list[int]) -> list[int]:
        result: list[int] = []
        for a, b in zip(report, report[1:]):
            result.append(b - a)
        return result

    def is_good_rank(self, rank: list[int]) -> bool:
        direction = all(x > 0 for x in rank) or all(x < 0 for x in rank)
        return direction and all(abs(x) in (1, 2, 3) for x in rank)

    def find_good_rank(self, report: list[int]) -> list[int]:
        if self.is_good_rank(self.rank(report)):
            return report
        for i in range(len(report)):
            z = report[::]
            z.pop(i)
            if self.is_good_rank(self.rank(z)):
                return z
