from pathlib import Path

def parse_assignment(region: str):
  s = region.split("-")
  start, end = int(s[0]), int(s[1])
  return set(range(start, end+1))

if __name__ == "__main__":
  with open(Path(__file__).parent / Path('input.txt')) as f:
    total_common = 0
    total_overlap = 0
    for line in f.readlines():
      splits = line.split(',')
      elf1 = parse_assignment(splits[0])
      elf2 = parse_assignment(splits[1])
      if elf1.issubset(elf2) or elf2.issubset(elf1):
        total_common += 1

      if not elf1.isdisjoint(elf2):
        total_overlap += 1

    print(f"Part 1: {total_common}")
    print(f"Part 2: {total_overlap}")