from random import shuffle
from typing import Tuple


class Cell:
    def __init__(self, value):
        self.value = str(value) if value else '0'
        self.visible = False

Mine = Cell('X')


class Game:
    def __init__(self, x: int, y: int, no_mines: int):
        self.x = x
        self.y = y

        dummy_board = [Mine] * no_mines + [None for _ in range(y * x - no_mines)]
        shuffle(dummy_board)

        self.board = [[None for _ in range(self.x)] for _ in range(self.y)]

        for i, c in enumerate(dummy_board):
            if c is Mine:
                y, x = divmod(i, self.y)
                self.board[y][x] = c

        for x in range(self.x):
            for y in range(self.y):

                if self.board[y][x] is not Mine:
                    adj_mines = sum([self.board[y][x] is Mine for x, y in self._adj_xy(x, y)])

                    self.board[y][x] = Cell(adj_mines)

    def print(self):
        """Prints board to standard output"""
        rows = []

        for row in self.board:
            cells = []

            for cell in row:
                cells.append(cell.value if cell.visible else '-')

            rows.append(' '.join(cells))

        print('\n'.join(rows) + '\n')

    def act(self, x: int, y: int) -> bool:
        """Acts on x,y cell - like a click in classic minesweeper."""
        if not self.board[y][x].visible:
            if self.board[y][x] is Mine:
                self.uncover_all()
                return True
            else:
                self.board[y][x].visible = True
                if self.board[y][x].value == '0':
                    for _x, _y in self._adj_xy(x,y):
                        self.act(_x, _y)
        return False

    def uncover_all(self):
        """Makes all cells visible"""
        for row in self.board:
            for cell in row:
                cell.visible = True

    def _adj_xy(self, x: int, y: int) -> Tuple[Tuple[int]]:
        """Returns all adjacent cells to x, y"""
        adj = []

        if y > 0:
            adj.append((x, y - 1))
            if x > 0: adj.append((x - 1, y - 1))
            if x < self.x - 1: adj.append((x + 1, y - 1))

        if y < self.y - 1:
            adj.append((x, y+ 1))
            if x > 0: adj.append((x - 1, y + 1))
            if x < self.x - 1: adj.append((x + 1, y + 1))

        if x < self.x - 1: adj.append((x + 1, y))
        if x > 0: adj.append((x - 1, y))

        return tuple(adj)

if __name__ == '__main__':
    g = Game(10, 10, 10)
    g.print()
    g.act(0, 1)
    g.print()
    g.act(0, 2)
    g.print()
    g.act(2, 1)
    g.print()
    g.act(2, 2)
    g.print()
    g.act(2, 3)
    g.print()
