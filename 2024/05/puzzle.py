class Puzzle:

    def __init__(self, data: str):
        self.data = data

    @property
    def answer(self) -> int:
        total = 0
        for update in self.updates:
            if self.check_rules(update):
                total += self.find_middle(update)
        return total

    @property
    def corrected_answer(self) -> int:
        total = 0
        for update in self.updates:
            if not self.check_rules(update):
                new_row = self.reorder(update)
                total += self.find_middle(new_row)
        return total

    @property
    def rules(self) -> tuple[tuple[int, int]]:
        rule_data = self.data.split('\n\n')[0]
        data: list[tuple[int, int]] = []
        for row in rule_data.split():
            a, b = row.split("|")
            data.append((int(a), int(b)))
        return tuple(data)

    @property
    def updates(self) -> tuple[tuple[int, ...]]:
        rule_data = self.data.split('\n\n')[-1]
        data: list[tuple[int, ...]] = []
        for row in rule_data.split():
            data.append(tuple([int(x) for x in row.split(',')]))
        return tuple(data)

    def reorder(self, update: tuple[int, ...]) -> tuple[int, ...]:
        new_order = [None] * len(update)
        for number in update:
            pos = self.get_max_position(number, update)
            new_order[pos] = number
        return tuple(n for n in new_order if n is not None)

    def get_max_position(self, number: int, update: tuple[int, ...]) -> int:
        positions: list[int] = [0]
        for a, b in self.rules:
            if a in update and b in update:
                if b == number:
                    positions.append(1)
        return sum(positions)

    def check_rules(self, update: tuple[int, ...]) -> bool:
        for a, b in self.rules:
            if a in update and b in update:
                if update.index(a) > update.index(b):
                    return False
        return True

    def find_middle(self, update: tuple[int, ...]) -> int:
        return update[len(update) // 2]