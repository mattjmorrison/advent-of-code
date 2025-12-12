import re
from collections import deque

class Button:

    def __init__(self, raw):
        self.raw = raw
        self.lights: list[int] = list(map(int, raw.split(',')))

    def press(self, state):
        l = list(state)
        for light in self.lights:
            l[light] = not l[light]
        return l

    def update_joltage(self, joltage):
        j = list(joltage)
        for light in self.lights:
            j[light] += 1
        return j


class Machine:

    def __init__(self, raw):
        self.raw = raw
        self.lights: list[bool] = []
        self.buttons: list[Button] = []
        self.joltage: list[int] = []
        self.parse()
        self.state = [False] * len(self.lights)

    def press(self, button, state=None):
        state = state or self.state
        return self.buttons[button].press(state)

    def parse(self):
        self.build_lights()
        self.build_buttons()
        self.build_joltage()

    def build_buttons(self):
        matches = re.findall(r'\((.+?)\)', self.raw)
        for match in matches:
            self.buttons.append(Button(match))
        return self.buttons

    def build_lights(self):
        match = re.search(r'\[(.+)\]', self.raw)
        for char in match.group(1):
            self.lights.append(char == '#')

    def build_joltage(self):
        match = re.search(r'\{(.+)\}', self.raw)
        self.joltage = list(map(int, match.group(1).split(',')))

    def turn_on(self):
        q = deque([(self.state, 0)])
        done = {tuple(self.state)}
        while(len(q)):
            state, count = q.popleft()
            if state == tuple(self.lights):
                return count
            for button in self.buttons:
                new_state = tuple(button.press(state))
                if new_state in done:
                    continue
                q.append((new_state, count + 1))
                done.add(new_state)

    def configure_joltage(self):
        q = deque([(self.state, 0)])
        done = {tuple(self.state)}
        while(len(q)):
            state, count = q.popleft()
            if state == tuple(self.joltage):
                return count
            for button in self.buttons:
                new_state = tuple(button.update_joltage(state))
                if new_state in done:
                    continue
                q.append((new_state, count + 1))
                done.add(new_state)


class Puzzle:

    def __init__(self, input):
        self.input: str = input

    def build_machines(self):
        machines = []
        for row in self.input.split('\n'):
            machines.append(Machine(row))
        return machines

    def solve_part_one(self):
        return sum(machine.turn_on() for machine in self.build_machines())

    def solve_part_two(self):
        return sum(machine.configure_joltage() for machine in self.build_machines())
