class Puzzle:

    def __init__(self, data: str):
        self.data = data

    @property
    def blocks(self) -> list[str]:
        result: list[str] = []
        current = 0
        space = False
        for item in self.data:
            length = int(item)
            result.extend(('.' if space else str(current)) * length)
            if not space:
                current += 1
            space = not space
        return result

    def defrag(self) -> list[str]:
        result = self.blocks
        for i in range(1, len(result) + 1):
            if not self.has_gaps(result):
                break
            item = result[i * -1]
            if item != '.':
                result[result.index('.')] = item
                result[i * -1] = '.'
        return result

    def has_gaps(self, data: list[str]) -> bool:
        return len(set(data[data.index('.'):])) > 1

    def get_checksum(self) -> int:
        results = 0
        defragged = self.defrag()
        for index, value in enumerate(defragged):
            if value == '.':
                break
            results += index * int(value)
            print(f'{results} += ({index} * {value})')
        return results
