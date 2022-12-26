from pathlib import Path

if __name__ == "__main__":
  elves_calories = []
  with open(Path(__file__).parent/Path('input.txt')) as f:
    elf_cal = []
    while line := f.readline():
      if not line.strip():
        elves_calories.append(elf_cal)
        elf_cal = []
      else:
        elf_cal.append(int(line.strip()))

  totals = sorted([sum(elf_cal) for elf_cal in elves_calories], reverse=True)
  max_elf = totals[0]
  top_3 = sum(totals[:3])
  
  print(f"Part 1: {max_elf}")
  print(f"Part 2: {top_3}")
