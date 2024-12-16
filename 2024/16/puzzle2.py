import time
from heapq import heappop, heappush
from collections import defaultdict
from math import inf


class Puzzle2:

    def __init__(self, data, pause=0):
        self.pause = pause
        self.visited = []
        self.grid = {}
        for y, row in enumerate(data.split('\n')):
            for x, char in enumerate(row):
                self.grid[(x, y)] = char
        self.start = ''
        self.end = ''
        for k, v in self.grid.items():
            if v == 'S':
                self.start = k
            elif v == 'E':
                self.end = k
        self.max_x = x
        self.max_y = y

    def get_neighbor_positions(self, pos: tuple[int, int], direction: tuple[int, int]) -> list[tuple[int, int]]:
        return [
            ((pos[0] + direction[0], pos[1] + direction[1]), direction, 1),
            ((pos[0] + (direction[1] * -1), pos[1] + (direction[0] * -1)), (direction[1] * -1, direction[0] * -1), 1001),
            ((pos[0] + direction[1], pos[1] + direction[0]), (direction[1], direction[0]), 1001),
        ]

    def get_neighbors(self, pos: tuple[int, int], direction: tuple[int, int]):
        neighbors = []
        neighbor_positions = self.get_neighbor_positions(pos, direction)
        for new_pos, new_dir, score in neighbor_positions:
            if self.is_valid(new_pos[0], new_pos[1]):
                neighbors.append((score, (new_pos, new_dir)))
        return neighbors

    def is_valid(self, x: int, y: int):
        return 0 <= x < self.max_y and 0 <= y < self.max_x and self.grid[(x, y)] in ('.', 'E')

    def dijkstra(self):
        start = (self.start, (1, 0))
        queue = [(0, start)]
        dists = {start: 0}

        while len(queue) > 0:
            if self.pause > 0:
                print(self.show_grid())
            dist, (position, direction) = heappop(queue)

            if position == self.end:
                return dist

            for (cost, (npos, ndir)) in self.get_neighbors(position, direction):
                dist_cost = dist + cost

                if dist_cost <= dists.get((npos, ndir), inf):
                    dists[(npos, ndir)] = dist_cost
                    self.visited = [k for (k, v) in dists.keys()]
                    print(dist_cost)
                    heappush(queue, (dist_cost, (npos, ndir)))

    def show_grid(self) -> str:
        output = ""
        for row_index in range(self.max_x + 1):
            for col_index in range(self.max_y + 1):
                val = self.grid[(col_index, row_index)]
                if (col_index, row_index) in self.visited:
                    output += 'X'
                else:
                    output += val
            output += "\n"
        time.sleep(self.pause)
        return output
