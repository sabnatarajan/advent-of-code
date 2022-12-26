from pathlib import Path
from enum import Enum

class Game(Enum):
  WIN = Z = 6
  LOSE = X = 0
  DRAW = Y = 3

class RPS(Enum):
  ROCK = A = 1
  PAPER = B = 2
  SCISSOR = C = 3

  def choose(self, result: "Game"):
    if result == Game.DRAW:
      return self
    if self == RPS.ROCK:
      return RPS.PAPER if result == Game.WIN else RPS.SCISSOR
    elif self == RPS.PAPER:
      return RPS.SCISSOR if result == Game.WIN else RPS.ROCK
    else:
      return RPS.ROCK if result == Game.WIN else RPS.PAPER


if __name__ == "__main__":
  games = []
  scores = []
  choices = []
  with open(Path(__file__).parent / Path('input.txt')) as f:
    for line in f.readlines():
      splits = line.split()
      p, res = RPS[splits[0]], Game[splits[1]]
      games.append([p, res])
      choice = p.choose(res)
      score = res.value + choice.value
      scores.append(score)

    # print(games)
    # print(choices)
    # print(scores)
    print(sum(scores))
