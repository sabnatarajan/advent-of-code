from pathlib import Path

def prio(c: str):
  if c.isupper():
    return ord(c) - 64 + 26
  else:
    return ord(c) - 96

if __name__ == "__main__":
  # Part 1
  with open(Path(__file__).parent / ("input.txt")) as f:
    total_priority = 0
    for line in f.readlines():
      l = len(line)//2
      c1, c2 = set(line[:l]), set(line[l:])
      common = c1.intersection(c2)

      total_priority += sum([prio(_) for _ in common])
    print(f"Part 1: {total_priority}")


  # Part 2
  with open(Path(__file__).parent / ("input.txt")) as f:
    total_priority = 0
    i = 0
    c = []
    while line := f.readline():
      line = line.strip()
      i += 1
      c.append(set(line))
      if i%3 == 0:
        common = c[0].intersection(c[1]).intersection(c[2])
        total_priority += sum([prio(_) for _ in common])
        c = []

    print(f"Part 2: {total_priority}")