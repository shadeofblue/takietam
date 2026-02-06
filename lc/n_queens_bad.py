# 52
from typing import List, Set, Tuple

class Solution:
    def totalNQueens(self, n: int) -> int:
        in_solution: Set[Tuple[int, int]] = set()
        solutions: List[Set[Tuple[int, int]]] = []

        def check(queens: Set[Tuple[int, int]], x: int, y: int, candidates: Set[Tuple[int, int]]) -> None:
            if (x, y) in in_solution:
                print(f"already checked? {x=}, {y=}")
                return

            print(f"check {len(queens)}: {x=}, {y=}, {queens=}, {candidates=}")

            queens.add((x, y))

            if len(queens) == n:
                print("--------------------------------------------------------!!!!!")
                for t in queens:
                    in_solution.add(t)
                solutions.append(queens)
                return

            new_candidates = set()
            for c in candidates:
                if c[0] != x and c[1] != y and abs(c[0] - x) != abs(c[1] - y):
                    new_candidates.add(c)

            print(f"----------------- {candidates=}, {new_candidates=}")

            for c in new_candidates:
                check(queens.copy(), c[0], c[1], new_candidates.copy())


        for y in range(n):
            for x in range(n):
                check(set(), x, y, {(cx, cy) for cx in range(n) for cy in range(n)})

        print(f"{n=} => {solutions=}")
        return len(solutions)


s = Solution()

n = 5
print(f"{n} => ", s.totalNQueens(n))