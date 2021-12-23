#!/usr/bin/env python3

def part1(inputs: list[int]):
    print("=== PART 1 ===")
    max_pos = max(inputs)

    min_pos = None
    min_fuel = 2**31-1
    for pos in range(max_pos):
        total_fuel = sum(fuel_cost(i, pos) for i in inputs)
        min_pos, min_fuel = (pos, total_fuel) if total_fuel < min_fuel else (min_pos, min_fuel)

    print(f"{min_pos=}, {min_fuel=}")

def part2(inputs: list[int]):
    print("=== PART 2 ===")
    max_pos = max(inputs)

    min_pos = None
    min_fuel = 2**31-1
    for pos in range(max_pos):
        total_fuel = sum(fuel_cost(i, pos, constant=False) for i in inputs)
        min_pos, min_fuel = (pos, total_fuel) if total_fuel < min_fuel else (min_pos, min_fuel)

    print(f"{min_pos=}, {min_fuel=}")

def fuel_cost(a: int, b: int, constant=True) -> int:
    diff = abs(a-b)
    if constant:
        return diff
    else:
        return int(diff * (diff+1) / 2)

def process_input(file: str) -> list[int]:
    return [int(_) for _ in file.split(',')]

def test_input() -> str:
    return "16,1,2,0,4,2,7,1,2,14"

def read_input() -> str:
    with open('input.txt', 'r') as f:
        return f.readline()

if __name__ == "__main__":
    file = test_input()
    file = read_input()
    inputs = process_input(file)
    part1(inputs)
    part2(inputs)
