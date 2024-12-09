from operator import add, mul

other = {
    add: mul,
    mul: add
}


class Puzzle:

    def __init__(self, data: str):
        self.data = data

    @property
    def answer(self) -> int:
        return 0

    def parse(self) -> list[int, tuple[int, ...]]:
        results = []
        for row in self.data.split('\n'):
            answer, nums = row.strip().split(": ")
            r = (int(answer), tuple(int(x) for x in nums.strip().split(' ')))
            print(r)
            results.append(r)
        return results

    def solve(self, answer: int, a: int, b: int, more: tuple[int, ...] = None, start=mul) -> bool:
        result = start(a, b)
        print(f"{a} {start} {b} = {result}")
        if result > answer:
            result = other[start](a, b)
            print(f"{a} {other[start]} {b} = {result}")
        if more:
            return self.solve(answer, result, more[0], more[1:])
        if answer != result and start != add:
            return self.solve(answer, a, b, more, start=add)
        return answer == result