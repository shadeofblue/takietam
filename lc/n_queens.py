# 52
from dataclasses import dataclass
from typing import List


@dataclass
class Piece:
    x: int
    y: int

    def collides(self, p: "Piece"):
        return self.x == p.x or self.y == p.y or abs(self.x - p.x) == abs(self.y - p.y)

class Solution:

    def totalNQueens(self, n: int) -> int:
        solutions: List[List[Piece]] = []

        def check(row: int, queens: List[Piece]) -> None:
            # print(f"check {row=}, {queens=}")
            if row >= n:
                if len(queens) == n:
                    # print(f" ------ {queens=}")
                    solutions.append(queens)
                return

            for x in range(n):
                p = Piece(x, row)
                if all([not p.collides(q) for q in queens]):
                    new_queens = queens.copy()
                    new_queens.append(p)
                    check(row + 1, new_queens)

        check(0, [])

        # print(f"{n=} => {solutions=}")
        return len(solutions)


s = Solution()

# n = 5

for n in range(1, 10):
    print(f"{n} => ", s.totalNQueens(n))
