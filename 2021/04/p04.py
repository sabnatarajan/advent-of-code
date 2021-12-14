#!/usr/bin/env python3

def part1(inputs: tuple[list[int], list["Board"]]):
    print("=== PART 1 ===")
    numbers_drawn, boards = inputs

    round = 0
    for number in numbers_drawn:
        round += 1
        for idx, board in enumerate(boards):
            board.mark(number)
            if board.check_bingo():
                board_val = boards[idx].value
                print(board)
                print(f"Board {idx+1} won, {round=}, {number=}, {board_val=}, answer={board_val * number}")
                break
        else:
            continue
        break

def part2(inputs: tuple[list[int], list["Board"]]):
    print("=== PART 2 ===")
    numbers_drawn, boards = inputs

    wins = [0] * len(boards) # Keep track of which boards have won, 1 if won else 0
    round = 0
    for number in numbers_drawn:
        round += 1
        for idx, board in enumerate(boards):
            if wins[idx]: # this board has already won
                continue
            board.mark(number)
            if board.check_bingo():
                board_val = boards[idx].value
                wins[idx] = 1
                latest_winning_board = idx

        yet_to_win = [board_num for board_num, _ in enumerate(wins) if wins[board_num] == 0]
        # print(f"current wins: {sum(wins)}, yet to win: {yet_to_win}, {len(yet_to_win)}")
        if sum(wins) == len(boards):
            last_board = boards[latest_winning_board]
            board_val = last_board.value
            print(last_board)
            print(f"Last to win: board {latest_winning_board+1}, {round=}, {number=}, {board_val=}, answer={board_val * number}")
            break

class Board:

    def __init__(self, rows: list[str]):
        self.cells: list["Cell"] = list()
        for r, row in enumerate(rows):
            for c, cell in enumerate(row.split()):
                self.cells.append(Cell(int(cell), r, c))

    def mark(self, number):
        cell = self.get_cell(number)
        if cell:
            cell.mark()

    def get_cell(self, number):
        cells = [cell for cell in self.cells if cell.val==number]
        if cells:
            return cells[0]
        else:
            return None

    @property
    def value(self):
        return sum(cell.val for cell in self.cells if not cell.marked)

    def check_bingo(self):
        for row in self._rows():
            if all(cell.marked for cell in row):
                return True

        for col in self._cols():
            if all(cell.marked for cell in col):
                return True

        return False

    def _rows(self) -> list[list["Cell"]]:
        return [self.cells[i*5:(i+1)*5] for i in range(5)]

    def _cols(self) -> list[list["Cell"]]:
        cols = list()
        for c in range(5):
            col = list()
            for r in range(5):
                col.append(self.cells[r*5 + c])
            cols.append(col)

        return cols

    def __repr__(self) -> str:
        repr_str = "Board("
        for i in range(5):
            for cell in self.cells[i*5: (i+1)*5]:
                repr_str += f"{cell.val:02d}" + f"{'. ' if cell.marked else '  '}"
                # rows.append(",".join([str(cell.val) for cell in self.cells[i*5:i*5+5]]))
            repr_str += "\n      " if i < 4 else ""
        return repr_str + "\b\b)"

class Cell:
    def __init__(self, val, r, c) -> None:
        self.r, self.c, self.val = r, c, val
        self.marked = False

    def mark(self):
        self.marked = True

    def __repr__(self) -> str:
        return f"Cell(val={self.val}, r={self.r}, c={self.c})"

def test_input() -> list[str]:
    lines = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

    22 13 17 11  0
     8  2 23  4 24
    21  9 14 16  7
     6 10  3 18  5
     1 12 20 15 19

     3 15  0  2 22
     9 18 13 17  5
    19  8  7 25 23
    20 11 10 24  4
    14 21 16 12  6

    14 21 17 24  4
    10 16 15  9 19
    18  8 23 26 20
    22 11 13  6  5
     2  0 12  3  7""".splitlines()

    return [line.strip() for line in lines]

def read_input():
    with open('input.txt', 'r') as f:
        return f.read().splitlines()

def process_inputs(lines: list[str]) -> tuple[list[int], list[Board]]:
    numbers_drawn = [int(num) for num in lines[0].strip().split(',')]

    boards = list()
    start_line = 2
    while (start_line < len(lines)):
        board_rows = lines[start_line: start_line+5]
        boards.append(Board(board_rows))
        start_line += 6

    return numbers_drawn, boards

if __name__ == "__main__":
    # file_contents = test_input()
    file_contents = read_input()
    inputs = process_inputs(file_contents)
    part1(inputs)
    part2(inputs)

