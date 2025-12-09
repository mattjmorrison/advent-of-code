from collections import defaultdict
from math import sqrt


class Puzzle:

    def __init__(self, input):
        self.input: str = input

    def parse(self):
        point_rows = self.input.split('\n')
        point_row_tuples = [row.split(',') for row in point_rows]
        return [(int(x), int(y), int(z)) for x, y, z in point_row_tuples]

    def solve_part_one(self, counter=1000):
        points = self.parse()
        parents = {i: i for i in range(len(points))}
        distances = self.calc_distances(points)
        distances.sort()
        for point in range(counter):
            distnace, first, second = distances[point]
            if self.find(parents, first) == self.find(parents, second):
                continue
            self.combine(parents, first, second)

        lens = defaultdict(int)
        for parent in parents.values():
            point = self.find(parents, parent)
            lens[point] += 1

        result = 1
        for x in sorted(lens.values())[-3:]:
            result *= x
        return result

    def solve_part_two(self):
        points = self.parse()
        parents = {i: i for i in range(len(points))}
        distances = self.calc_distances(points)
        distances.sort()
        for distance, first, second in distances:
            if self.find(parents, first) == self.find(parents, second):
                continue
            self.combine(parents, first, second)

            if all(self.find(parents, 0) == self.find(parents, point) for point in range(len(points))):
                break

        x1, y1, z1 = points[first]
        x2, y2, z2 = points[second]
        return x1 * x2
    
    def calc_distances(self, points):
        distances = []
        for first in range(len(points) - 1):
            for second in range(first + 1, len(points)):
                x1, y1, z1 = points[first]
                x2, y2, z2 = points[second]
                distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
                distances.append((distance, first, second))
        return distances

    def combine(self, parents, point_one, point_two):
        parents_of_one = self.find(parents, point_one)
        parent_of_two = self.find(parents, point_two)
        parents[parent_of_two] = parents_of_one
        
    def find(self, parents, point):
        if parents[point] == point:
            return point
        parents[point] = self.find(parents, parents[point])
        return parents[point]