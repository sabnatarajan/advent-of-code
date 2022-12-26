from pathlib import Path
from enum import Enum

class Game(Enum):
  WIN = 6
  LOSE = 0
  DRAW = 3

  @staticmethod
  def play(p1:"RPS", p2:"RPS") -> "Game":
    if p1 == p2:
      return Game.DRAW

    if p1 == RPS.ROCK:
      return Game.LOSE if p2 == RPS.PAPER else Game.WIN
    elif p1 == RPS.PAPER:
      return Game.LOSE if p2 == RPS.SCISSOR else Game.WIN
    else:
      return Game.LOSE if p2 == RPS.ROCK else Game.WIN

class RPS(Enum):
  ROCK = A = X = 1
  PAPER = B = Y = 2
  SCISSOR = C = Z = 3


if __name__ == "__main__":
  games = []
  scores = []
  with open(Path(__file__).parent / Path('input.txt')) as f:
    for line in f.readlines():
      splits = line.split()
      p1, p2 = RPS[splits[0]], RPS[splits[1]]
      games.append([p1, p2])
      score = Game.play(p2, p1).value + p2.value
      scores.append(score)

    # print(games)
    # print(scores)
    print(sum(scores))
