#!/usr/bin/env python3

from math import sqrt

def part1(inputs: list["LineSeg"]):
    print("=== PART 1 ===")
    _max = max([max(line.a.x, line.a.y, line.b.x, line.b.y) for line in inputs])
    grid_size = 10**len(str(_max))

    ortho_lines = list(filter(is_ortho, inputs))
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

    for line in ortho_lines:
        mark_points(grid, line)

    # print_grid(grid)
    print(score_grid(grid))

def part2(inputs: list["LineSeg"]):
    pass

def is_ortho(line_seg: "LineSeg") -> bool:
    return (line_seg.a.x == line_seg.b.x) or (line_seg.a.y == line_seg.b.y)

def point_on_line(pt: "Point", line: "LineSeg") -> bool:
    return distance(pt, line.a) + distance(pt, line.b) == line.length()

def distance(a: "Point", b: "Point") -> float:
    # Euclidean distance
    return sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def mark_points(grid: list[list[int]], line: "LineSeg"):
    ax, ay = line.a.x, line.a.y
    bx, by = line.b.x, line.b.y

    # print(f"marking points on line seg: {line}")
    if ax == bx: # vertical line -> mark the 'y' points
        start = min(ay, by)
        for i in range(abs(ay - by) + 1):
            grid[ax][start+i] += 1
            # print(f"\tmarking point {Point(ax, start+i)}")
    elif ay == by:
        start = min(ax, bx)
        for i in range(abs(ax - bx) + 1):
            grid[start+i][ay] += 1
            # print(f"\tmarking point {Point(start+i, ay)}")

def print_grid(grid: list[list[int]]) -> None:
    grid_size = len(grid)
    for y in range(grid_size):
        for x in range(grid_size):
            print(grid[x][y] if grid[x][y]>0 else ".", end=" ")
        print()

def score_grid(grid: list[list[int]], threshold=2) -> int:
    return sum(1 for row in grid for el in row if el>=threshold)

def test_input() -> list[str]:
    lines = \
    """0,9 -> 5,9
        8,0 -> 0,8
        9,4 -> 3,4
        2,2 -> 2,1
        7,0 -> 7,4
        6,4 -> 2,0
        0,9 -> 2,9
        3,4 -> 1,4
        0,0 -> 8,8
        5,5 -> 8,2""".splitlines()

    return [line.strip() for line in lines]

class Point:
    def __init__(self, x, y) -> None:
        self.x, self.y = x, y

    def __repr__(self) -> str:
        return f"Point({self.x},{self.y})"

class LineSeg:
    def __init__(self, pt_a: Point, pt_b: Point) -> None:
        self.a, self.b = pt_a, pt_b

    def __repr__(self) -> str:
        return f"Line( ({self.a.x},{self.a.y}) -> ({self.b.x},{self.b.y}) )"

    def length(self) -> float:
        return distance(self.a, self.b)


def read_input():
    with open('input.txt', 'r') as f:
        return f.read().splitlines()

def process_inputs(lines: list[str]):
    processed = list()
    for line in lines:
        splits = line.split('->')
        a = splits[0].strip().split(',')
        b = splits[1].strip().split(',')
        pt_a = Point(int(a[0]), int(a[1]))
        pt_b = Point(int(b[0]), int(b[1]))
        processed.append(LineSeg(pt_a, pt_b))

    return processed


if __name__ == "__main__":
    file_contents = test_input()
    file_contents = read_input()
    inputs = process_inputs(file_contents)
    part1(inputs)
    # part2(inputs)

