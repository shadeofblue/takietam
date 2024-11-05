# 36
from typing import List, Dict, Set


class Solution:
    def printBoard(self, board: List[List[str]]) -> bool:
        for y in range(19):
            yd, yi = divmod(y, 6)
            for x in range(19):
                xd, xi = divmod(x, 6)
                if xi == 0 and yi == 0:
                    v = "+"
                elif yi == 0:
                    v = "-"
                elif xi == 0:
                    v = "|"
                elif xi in (1, 5) or yi in (1, 5):
                    v = " "
                else:
                    v = board[yd * 3 + yi - 2][xd * 3 + xi - 2]
                print(v or "_", end="")

            print("")


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        unique: Dict[str, Set] = {}
        for x in range(9):
            for y in range(9):
                column_id = f"c{x}"
                row_id = f"r{y}"
                sector_id = f"s{x // 3}{y // 3}"
                unique.setdefault(column_id, set())
                unique.setdefault(row_id, set())
                unique.setdefault(sector_id, set())
                v = board[y][x]
                if v != ".":
                    if v in unique[column_id] | unique[row_id] | unique[sector_id]:
                        # print(v in unique[column_id], v in unique[row_id], v in unique[sector_id])
                        return False
                    unique[column_id].add(v)
                    unique[row_id].add(v)
                    unique[sector_id].add(v)
        return True

s = Solution()

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]
         ]

s.printBoard(board)
print(s.isValidSudoku(board))

board = [["8","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

s.printBoard(board)
print(s.isValidSudoku(board))

