from data import DATA
from puzzle import Puzzle
from copy import deepcopy
from concurrent.futures import ProcessPoolExecutor, wait


# def part_two() -> int:
#     puzzle = Puzzle(DATA)
#     puzzle.try_obsticles()
#     return puzzle.loops


def try_example(counter, original_map, start, block):
    # 1868 too high
    # 1755 -? 
    # 1646 - unsure
    # 1523 - ?
    # 1434 too low
    print(f"Starting {counter}")
    p = Puzzle("")
    p.try_obsticles(original_map, start, block)
    print(f"Ending {counter}")
    return p.loops


def try_again() -> None:
    puzzle = Puzzle(DATA)
    puzzle.answer
    puzzle.clear_starting_position()
    original_map = deepcopy(puzzle.map)
    original_log = deepcopy(puzzle.log)

    with ProcessPoolExecutor(max_workers=50) as exe:
        futures = []
        counter = 0
        for start, block in zip(original_log, original_log[1:]):
            counter += 1
            futures.append(exe.submit(try_example, counter, original_map, start, block))
        done, not_done = wait(futures)

    total = 0
    for x in done:
        total += x.result()
    print(total)


if __name__ == '__main__':
    try_again()
    # print(part_two())