# 200
from typing import List

from dataclasses import dataclass

@dataclass
class GridNode:
    val: int
    visited: bool = False

    @property
    def visitable(self):
        return bool(self.val) and not self.visited


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ly = len(grid)
        lx = len(grid[0]) if ly else 0

        num_islands = 0
        nodes_grid: List[List[GridNode]] = [[GridNode(int(x)) for x in row] for row in grid]

        def explore(gx: int, gy: int):
            n: GridNode = nodes_grid[gy][gx]
            if not n.visitable:
                return

            n.visited = True

            if gy > 0:
                explore(gx, gy - 1)
            if gx > 0:
                explore(gx - 1, gy)
            if gy < ly - 1:
                explore(gx, gy + 1)
            if gx < lx - 1:
                explore(gx + 1, gy)

        for y in range(ly):
            row = nodes_grid[y]
            for x in range(lx):
                node = row[x]
                if node.visitable:
                    num_islands += 1
                    explore(x, y)

        return num_islands



s = Solution()

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print("\n".join(["".join(["#" if v == "1" else "_" for v in r]) for r in grid]))
print(s.numIslands(grid))

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print("\n".join(["".join(["#" if v == "1" else "_" for v in r]) for r in grid]))
print(s.numIslands(grid))
