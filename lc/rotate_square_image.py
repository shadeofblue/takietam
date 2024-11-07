# 48
from typing import List


class Solution:

    def draw_matrix(self, matrix: List[List[int]]):
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

    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for y1 in range(n // 2):
            y2 = n - y1 - 1
            # print(f"{y1=}, {y2=}")
            for x1 in range(y1, y2):
                x2 = n - x1 - 1
                vmap = ((y1, x1), (x1, y2), (y2, x2), (x2, y1),)
                v = []
                for vmap_idx in range(4):
                    coords = vmap[vmap_idx]
                    # print("src: ", coords, end="   ")
                    v.append(matrix[coords[0]][coords[1]])
                # print("\n", v)
                for vmap_idx in range(4):
                    coords = vmap[(vmap_idx + 1) % 4]
                    # print("dst: ", coords, end="   ")
                    matrix[coords[0]][coords[1]] = v[vmap_idx]
                # print("")
                # self.draw_matrix(matrix)


s = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
s.draw_matrix(matrix)
s.rotate(matrix)
s.draw_matrix(matrix)

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s.draw_matrix(matrix)
s.rotate(matrix)
s.draw_matrix(matrix)
