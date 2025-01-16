# 130

from typing import List, Set
from dataclasses import dataclass, field

def print_board(board: List[List[str]]):
    print("----------------")
    for r in board:
        print("".join([str(c) for c in r]))
    print("----------------")

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        ysize = len(board)
        xsize = len(board[0])

        regions_map: List[List[int]] = [[0 for _ in range(xsize)] for __ in range(ysize)]
        captureable_regions: Set[int]  = set()
        safe_regions: Set[int] = set()
        last_region = 0

        def explore(x: int, y: int, current_region: int = 0):
            # print(f"--- exploring: {x=}, {y=}, {current_region=}")
            nonlocal last_region

            if board[y][x] == "X":
                if current_region:
                    captureable_regions.add(current_region)
                return

            if regions_map[y][x]:
                return

            if not current_region:
                last_region += 1
                current_region = last_region

            regions_map[y][x] = current_region

            if x == 0:
                safe_regions.add(current_region)
            else:
                explore(x - 1, y, current_region)

            if y == 0:
                safe_regions.add(current_region)
            else:
                explore(x, y - 1, current_region)

            if x == xsize - 1:
                safe_regions.add(current_region)
            else:
                explore(x + 1, y, current_region)

            if y == ysize - 1:
                safe_regions.add(current_region)
            else:
                explore(x, y + 1, current_region)

        for y in range(ysize):
            for x in range(xsize):
                explore(x, y)

        # print_board(regions_map)

        captured_regions = captureable_regions - safe_regions

        # print(f"{captureable_regions=}, {safe_regions=}, {captured_regions=}")

        for y in range(ysize):
            for x in range(xsize):
                region = regions_map[y][x]
                if region in captured_regions:
                    board[y][x] = "X"


s = Solution()

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print_board(board)
s.solve(board)
print_board(board)

board = [["X"]]
print_board(board)
s.solve(board)
print_board(board)
