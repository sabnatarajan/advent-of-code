#!/usr/bin/env python3

from os import X_OK

class Move:
    def __init__(self, dir=0, mag=0):
        self.dir, self.mag = dir, mag

    def __repr__(self) -> str:
        return f"Move(dir={self.dir}, mag={self.mag})"


def part1(moves: list[Move]):
    position = { "x": 0, "y": 0}
    for move in moves:
        if move.dir == 'forward':
            position['x'] += move.mag
        elif move.dir == 'up':
            position['y'] -= move.mag
        elif move.dir == 'down':
            position['y'] += move.mag

    final_position = position['x'] * position['y']
    print(final_position)

def part2(moves: list[Move]):
    aim = 0
    position = { "x": 0, "y": 0 }
    for move in moves:
        if move.dir == 'down':
            aim += move.mag
        elif move.dir == 'up':
            aim -= move.mag
        elif move.dir == 'forward':
            position['x'] += move.mag
            position['y'] += move.mag * aim

    final_position = position['x'] * position['y']
    print(final_position)

def read_input():
    moves = list()
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            splits = line.strip().split()
            move = Move(dir=splits[0], mag=int(splits[1]))
            moves.append(move)

        return moves

if __name__ == "__main__":
    inputs = read_input()
    part1(inputs)
    part2(inputs)
