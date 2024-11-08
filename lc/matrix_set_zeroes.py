# 73
from typing import List
from colors import bold, yellow

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
                    if nv == 0:
                        v = bold(yellow(v))
                print(v, end="")
            print("")

    def setZeroes(self, matrix: List[List[int]]) -> None:
        h = len(matrix)
        w = len(matrix[0])
        zero_rows = set()
        zero_columns = set()

        for y in range(h):
            for x in range(w):
                v = matrix[y][x]
                if v == 0:
                    zero_rows.add(y)
                    zero_columns.add(x)

        for x in zero_columns:
            if x >= w:
                break
            for y in range(h):
                matrix[y][x] = 0

        for y in zero_rows:
            if y >= h:
                break
            for x in range(w):
                matrix[y][x] = 0


s = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
s.drawMatrix(matrix)
s.setZeroes(matrix)
s.drawMatrix(matrix)

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
s.drawMatrix(matrix)
s.setZeroes(matrix)
s.drawMatrix(matrix)

matrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
s.drawMatrix(matrix)
s.setZeroes(matrix)
s.drawMatrix(matrix)
