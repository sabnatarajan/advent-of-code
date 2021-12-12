#!/usr/bin/env python3

from os import X_OK

class Move:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def __repr__(self) -> str:
        return f"Move(x={self.x}, y={self.y})"

def part1(moves: list[Move]):
    print(final_position(moves))

def part2():
    pass

def final_position(moves: list[Move]):
    position = { "x": 0, "y": 0}
    for move in moves:
        position['x'] += move.x
        position['y'] += move.y

    return position['x'] * position['y']

def read_input():
    moves = list()
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            splits = line.strip().split(' ')
            direction = splits[0]
            magnitude = int(splits[1].strip())
            if direction == 'forward':
                moves.append(Move(magnitude, 0))
            elif direction == 'up':
                moves.append(Move(0, -1*magnitude))
            elif direction == 'down':
                moves.append(Move(0, magnitude))

        return moves

if __name__ == "__main__":
    inputs = read_input()
    part1(inputs)
    part2()
