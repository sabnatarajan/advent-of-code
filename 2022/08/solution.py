from pathlib import Path

def print_grid(grid):
  for row in grid:
    for col in row:
      print(f"{col} ", end="")
    print()
  print()

if __name__ == "__main__":
  grid = []
  markers = []
  scenic_scores = []
  with open(Path(__file__).parent / Path("test_input.txt")) as f:
    for line in f.readlines():
      line = line.strip()
      row = [int(digit) for digit in line]
      marker_row = [0] * len(row)
      scenic_score_row = [1] * len(row)
      grid.append(row)
      markers.append(marker_row)
      scenic_scores.append(scenic_score_row)

  for x in range(1, len(grid)-1):
    score = 0
    tallest = -1

    # look left-right
    for y in range(1, len(grid)-1):
      cur = grid[x][y]
      prev = grid[x][y-1]
      tallest = max(tallest, prev)
      if cur > tallest: markers[x][y] = 1
      if cur > prev: scenic_scores[x][y] = 1 + scenic_scores[x][y-1]
      else: scenic_scores[x][y] = 1

    tallest = -1
    # look right-left
    for y in range(1, len(grid)-1)[::-1]:
      cur = grid[x][y]
      prev = grid[x][y+1]
      tallest = max(tallest, prev)
      if cur > tallest: markers[x][y] = 1

    tallest = -1
    # look top-bottom
    for y in range(1, len(grid)-1):
      cur = grid[y][x]
      prev = grid[y-1][x]
      tallest = max(tallest, prev)
      if cur > tallest: markers[y][x] = 1

    tallest = -1
    # look bottom-top
    for y in range(1, len(grid)-1)[::-1]:
      cur = grid[y][x]
      prev = grid[y+1][x]
      tallest = max(tallest, prev)
      if cur > tallest: markers[y][x] = 1

  visible_on_edges = (len(grid)-1)*4
  visible_inside = sum(sum(row) for row in markers)

  print_grid(markers)
  print(f"Part 1: {visible_on_edges + visible_inside}")
  
  print_grid(grid)
  print_grid(scenic_scores)