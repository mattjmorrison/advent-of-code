class Puzzle:

    def __init__(self, data: str):
        self.data = data
        self.keys: list[list[tuple[int, int]]] = []
        self.locks: list[list[tuple[int, int]]] = []
        self._parse()

    @property
    def answer(self) -> int:
        works = 0
        for key in self.keys:
            for lock in self.locks:
                max_key_pins = self.max_key_columns(key)
                max_lock_pins = self.max_lock_columns(lock)
                if self.key_works(max_key_pins, max_lock_pins):
                    works += 1
        return works

    def _build_coords(self, data: list[str]) -> list[tuple[int, int]]:
        result = []
        for rindex, row in enumerate(data):
            for cindex, col in enumerate(row):
                if col == '#':
                    result.append((rindex, cindex))
        return result

    def _parse(self) -> None:
        for item in self.data.split('\n\n'):
            rows = item.split('\n')
            coords = self._build_coords(rows)
            if all(c == '#' for c in rows[0]):
                self.locks.append(coords)
            if all(c == '#' for c in rows[-1]):
                self.keys.append(coords)

    def max_key_columns(self, grid: list[tuple[int, int]]) -> list[int]:
        top = {i: None for i in range(5)}
        for row in range(7):
            for col in [
                v for _, v in list(filter(lambda r: r[0] == row, grid))
            ]:
                if not top.get(col):
                    top[col] = row
        return list(top.values())

    def max_lock_columns(self, grid: list[tuple[int, int]]) -> list[int]:
        top = {i: None for i in range(5)}
        for row in range(7):
            for col in [
                v for _, v in list(filter(lambda r: r[0] == row, grid))
            ]:
                top[col] = row
        return list(top.values())

    def key_works(self, key: list[int], lock: list[int]) -> bool:
        for l, k in zip(lock, key):
            if l >= k:
                return False
        return True
