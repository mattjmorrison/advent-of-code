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
        blocks = self.blocks
        while '.' in blocks:
            while blocks[-1] == '.':
                blocks.pop()
            blocks[blocks.index('.')] = blocks.pop()
        return blocks

    def get_checksum(self) -> int:
        results = 0
        defragged = self.defrag()
        for index, value in enumerate(defragged):
            results += index * int(value)
        return results

    def new_checksum(self) -> int:
        result = 0
        defragged = self.defrag()
        pass
