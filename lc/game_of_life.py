# 289
from asciimatics import screen, constants as scr_const
from typing import List

class Solution:
    def drawMatrix(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])

        for y in range(m*2+1):
            yd, yi = divmod(y, 2)
            for x in range(n*2+1):
                xd, xi = divmod(x, 2)
                if xi == 0 or yi == 0:
                    v = "    "
                else:
                    nv = matrix[yd][xd]
                    v = f"{nv:4.0f}"
                print(v, end="")
            print("")

    def get_board_value(self, board: List[List[int]], x: int, y: int, wrap: bool = False):
        h = len(board)
        w = len(board[0])
        if wrap or (0 <= x < w and 0 <= y < h):
            return board[y % h][x % w] & 1
        return 0

    def gameOfLife(self, board: List[List[int]], wrap: bool=False) -> None:
        h = len(board)
        w = len(board[0])

        # determine the next state
        for y in range(h):
            for x in range(w):
                c = self.get_board_value(board, x, y)
                neighbors = [
                    self.get_board_value(board, x - 1, y - 1, wrap),
                    self.get_board_value(board, x,     y - 1, wrap),
                    self.get_board_value(board, x + 1, y - 1, wrap),
                    self.get_board_value(board, x - 1, y,     wrap),
                    self.get_board_value(board, x + 1, y,     wrap),
                    self.get_board_value(board, x - 1, y + 1, wrap),
                    self.get_board_value(board, x,     y + 1, wrap),
                    self.get_board_value(board, x + 1, y + 1, wrap),
                ]
                s = sum(neighbors)
                # print(f"{x=}, {y=}, {s=}, {neighbors=}")
                if s == 3 or (s == 2 and c == 1):
                    board[y][x] = c | 2

        # self.drawMatrix(board)

        # set the next state
        for y in range(h):
            for x in range(w):
                board[y][x] = (board[y][x] & 2) >> 1

s = Solution()
#
# board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# s.drawMatrix(board)
# s.gameOfLife(board)
# s.drawMatrix(board)
#
# board = [[1,1],[1,0]]
# s.drawMatrix(board)
# s.gameOfLife(board)
# s.drawMatrix(board)

import random

def draw_board(scr: screen.Screen, board: List[List[int]]):
    # scr.clear_buffer(scr_const.COLOUR_BLACK, scr_const.A_NORMAL, scr_const.COLOUR_BLACK)
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] > 0:
                scr.print_at("#", x, y, colour=201, attr=scr_const.A_BOLD, bg=93)
            else:
                scr.print_at(" ", x, y,bg=54)
    scr.refresh()

def play(scr: screen.Screen):
    board = [[int(random.randint(0, 7) == 1) for _ in range(scr.width)] for __ in range(scr.height)]
    while not scr.get_event():
        draw_board(scr, board)
        s.gameOfLife(board, wrap=True)
        import time
        time.sleep(0.05)

with screen.ManagedScreen() as scr:
    play(scr)
