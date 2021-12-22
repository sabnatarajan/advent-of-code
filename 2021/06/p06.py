#!/usr/bin/env python3

from math import ceil

REPRODUCE_INTERVAL = 7

def part1(fishes: list[int]):
    print("=== PART 1 ===")
    count = len(fishes)
    for fish in fishes:
        new_fish = fish_produced(fish, 80)
        count += new_fish

    print(count)
        

def part2(fishes: list[int]):
    print("=== PART 2 ===")
    count = len(fishes)

    for fish in fishes:
        new_fish = fish_produced(fish, 256)
        count += new_fish

    print(count)


def fish_produced(fish_days_left: int, days: int, mem=dict()):
    if days in mem:
        # print(f"cache hit! F(8, {days})={mem.get(days)}")
        return mem[days]
    if fish_days_left > days:
        return 0

    times = ceil((days-fish_days_left)/REPRODUCE_INTERVAL)
    # print(f"this {fish=} will reproduce {times=} in {days=}")
    count = 0
    for time in range(times)[::-1]:
        d = days - fish_days_left - 1 - REPRODUCE_INTERVAL*time
        fp = fish_produced(8, d, mem=mem)
        mem[d] = fp
        count += fp

    return count + times
# === PART 1 ===
# 380758
# === PART 2 ===
# 1710623015163

def process_input(contents: str) -> list[int]:
    return [int(timer) for timer in contents.split(',')]

def test_input() -> str:
    return "3,4,3,1,2"

def read_input() -> str:
    with open('input.txt', 'r') as f:
        return f.readline()

if __name__ == "__main__":
    file = test_input()
    file = read_input()
    inputs = process_input(file)
    part1(inputs)
    part2(inputs)
