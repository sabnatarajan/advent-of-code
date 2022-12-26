import re
import copy
from pathlib import Path
from dataclasses import dataclass
from typing import List

@dataclass
class Move:
  from_: int
  to_: int
  qty: int

  @staticmethod
  def parse(move_str: str) -> "Move":
    m = re.match("move (\d*) from (\d*) to (\d*)", move_str)
    qty, f, t = m.groups()
    return Move(int(f)-1, int(t)-1, int(qty))

def print_stack(stack: List[List[str]]):
  for col in stack:
    for item in col[::-1]:
      print(item)

if __name__ == "__main__":
  lines = []
  # with open(Path(__file__).parent / Path('test_input.txt')) as f:
  with open(Path(__file__).parent / Path('input.txt')) as f:
    stack = []
    step=4
    stack_size = 0
    for i, line in enumerate(f.readlines()):
      lines.append(line)
      if line.strip() == "":
        print("begin moves")
        size_line_index = i-1

  stack_size = int(lines[size_line_index].split()[-1])
  stack_lines = lines[:size_line_index]
  move_lines = lines[size_line_index+2:]
  stack = [[] for _ in range(stack_size)]
  moves: List[Move] = []
    
  print(f"Empty stack: {stack} of {stack_size=}")
  for line in stack_lines:
    for i in range(0, len(line), step):
      s = line[i:i+step]
      item = re.sub("\[(.*)\]", r"\1", s).strip()
      pos = i//step
      if item != "":
        stack[pos].insert(0, item)

  print(f"Stack at start: {stack}")
    

  for line in move_lines:
    moves.append(Move.parse(line))

  # End setup

  # Execute moves part 1
  stack_part1 = copy.deepcopy(stack)
  for move in moves:
    buffer = []
    f, t = move.from_, move.to_
    for i in range(move.qty):
      if stack_part1[f]:
        buffer.append(stack_part1[f].pop())
    stack_part1[t].extend(buffer)

  message = "".join([items[-1] for items in stack_part1])
  print(f"Part 1: {message}")

  # Execute moves part 2
  stack_part2 = copy.deepcopy(stack)
  for move in moves:
    buffer = []
    f, t = move.from_, move.to_
    for i in range(move.qty):
      if stack_part2[f]:
        buffer.insert(0, stack_part2[f].pop())
    stack_part2[t].extend(buffer)

  message = "".join([items[-1] for items in stack_part2])
  print(f"Part 2: {message}")