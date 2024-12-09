class Puzzle:

    def __init__(self, data: str):
        self._data = data
        self.data = self.parse()

    @property
    def answer(self) -> int:
        return 0

    def parse(self):
        return [list(x) for x in self._data.split("\n")]

    @property
    def coords(self):
        indexes = {}
        for r_index, row in enumerate(self.data):
            for c_index, column in enumerate(row):
                if column == '.':
                    continue
                if column not in indexes:
                    indexes[column] = []
                indexes[column].append((r_index, c_index))
        return indexes
