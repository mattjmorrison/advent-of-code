class Region:

    def __init__(self, data):
        self.data = data
        self.parse()

    def parse(self):
        size, presents = self.data.split(':')
        self.width, self.length = map(int, size.split('x'))

    @property
    def area(self):
        return self.width * self.length


class Present:

    def __init__(self, data):
        self.data = data

    @property
    def area(self):
        print(self.data)
        return ''.join(self.data).count('#')

    def rotate(self):
        return str(self)

    def __str__(self):
        return ''.join((
            '\n',
            '\n'.join(self.data),
            '\n'
        ))

    def __repr__(self):
        return str(self)

class Puzzle:

    def __init__(self, input):
        self.input: str = input
        self.presents = {}
        self.regions = []

    def parse(self):
        sections = self.input.split('\n\n')
        for section in sections[:-1]:
            key, *data = section.split('\n')
            self.presents[int(key.split(':')[0])] = Present(data)

        for region in sections[-1].split('\n'):
            self.regions.append(Region(region))
