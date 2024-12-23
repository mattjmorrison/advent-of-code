from functools import cache, cached_property


class Puzzle:

    def __init__(self, data: str):
        self.data = data

    @cached_property
    def buyers(self) -> list[int]:
        return [int(x) for x in self.data.split('\n')]

    @property
    def answer(self) -> int:
        total = 0
        for secret in self.buyers:
            for _ in range(2000):
                secret = self.get_next_secret(secret)
            total += secret
        return total
    
    def get_best_buyer_prices(self) -> int:
        sequence_for_prices = {}
        for secret in self.buyers:
            buyer = []
            for _ in range(2000):
                secret = self.get_next_secret(secret)
                buyer.append(secret % 10)
            counted = set()
            for index in range(len(buyer) - 4):
                one, two, three, four, five = buyer[index:index + 5]
                sequence = (two - one, three - two, four - three, five - four)
                if sequence in counted:
                    continue
                counted.add(sequence)
                if sequence not in sequence_for_prices:
                    sequence_for_prices[sequence] = 0
                sequence_for_prices[sequence] += five
        return max(sequence_for_prices.values())
    
    @cache
    def prune(self, secret: int) -> int:
        return secret % 16777216

    @cache
    def mix(self, secret: int, given: int) -> int:
        return secret ^ given

    @cache
    def get_next_secret(self, secret: int) -> int:
        secret = (secret ^ (secret * 64)) % 16777216
        secret = (secret ^ (secret // 32)) % 16777216
        secret = (secret ^ (secret * 2048)) % 16777216
        return secret
    #     return self.step_three(self.step_two(self.step_one(secret)))

    # @cache
    # def step_one(self, secret: int) -> int:
    #     return self.prune(self.mix(secret, secret * 64))

    # @cache
    # def step_two(self, secret: int) -> int:
    #     return self.prune(self.mix(secret, secret // 32))

    # @cache
    # def step_three(self, secret: int) -> int:
    #     return self.prune(self.mix(secret, secret * 2048))
