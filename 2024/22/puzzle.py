from functools import cache


class Puzzle:

    def __init__(self, data: str):
        self.data = data

    @property
    def answer(self) -> int:
        total = 0
        for secret in [int(x) for x in self.data.split('\n')]:
            for _ in range(2000):
                secret = self.get_next_secret(secret)
            total += secret
        return total

    @cache
    def prune(self, secret: int) -> int:
        return secret % 16777216

    @cache
    def mix(self, secret: int, given: int) -> int:
        return secret ^ given

    @cache
    def get_next_secret(self, secret: int) -> int:
        return self.step_three(self.step_two(self.step_one(secret)))

    @cache
    def step_one(self, secret: int) -> int:
        return self.prune(self.mix(secret, secret * 64))

    @cache
    def step_two(self, secret: int) -> int:
        return self.prune(self.mix(secret, secret // 32))

    @cache
    def step_three(self, secret: int) -> int:
        return self.prune(self.mix(secret, secret * 2048))
