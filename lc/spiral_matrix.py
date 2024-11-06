# 54
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
                    v = f"{matrix[yd][xd]:4.0f}"
                print(v, end="")
            print("")

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        out = []
        m = len(matrix)
        n = len(matrix[0])

        wsad = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        wsad_idx = 0

        x = min_x = 0
        y = min_y = 0
        max_x = n - 1
        max_y = m - 1

        while max_x >= min_x and max_y >= min_y:
            # print(f"{wsad=}, {wsad_idx=}, {min_x=}, {min_y=}, {max_x=}, {max_y=}")
            dx, dy = wsad[wsad_idx]
            while min_x <= x <= max_x and min_y <= y <= max_y:
                # print(f"{x=}, {y=}")
                v = matrix[y][x]
                # print(f"{v=}")
                out.append(v)
                x += dx
                y += dy

            wsad_idx = (wsad_idx + 1) % len(wsad)
            if wsad_idx == 1:
                min_y += 1
                x = max_x
                y = min_y
            elif wsad_idx == 2:
                max_x -= 1
                x = max_x
                y = max_y
            elif wsad_idx == 3:
                max_y -= 1
                y = max_y
                x = min_x
            else:
                min_x += 1
                x = min_x
                y = min_y

        return out


s = Solution()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
s.drawMatrix(matrix)
print(s.spiralOrder(matrix))

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
s.drawMatrix(matrix)
print(s.spiralOrder(matrix))
