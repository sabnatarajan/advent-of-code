#!/usr/bin/env python3

def part1(inputs: list):
    print(window(inputs, size=1))

def part2(inputs: list):
    print(window(inputs, size=3))

def window(inputs: list, size=1):
    sums = list()
    count_inc = 0
    for i in range(0, len(inputs)-size+1):
        sum = 0
        for j in range(size):
            sum += inputs[i+j]
        sums.append(sum)

    for prev, next in zip(sums[:-1], sums[1:]):
        if next > prev:
            count_inc += 1

    return count_inc


def read_input():
    # test inputs
    # inputs = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    with open('input.txt', 'r') as f:
        inputs = [int(_) for _ in f.readlines()]

    return inputs

if __name__ == "__main__":
    inputs = read_input()
    part1(inputs)
    part2(inputs)
