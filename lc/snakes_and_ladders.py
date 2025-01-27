from typing import List
from dataclasses import dataclass, field


@dataclass
class Node:
    val: int
    targets: List["Node"] = field(default_factory=list)
    visited = False
    final = False

    def __repr__(self):
        return f"Node<{self.val} tgts={[n.val for n in self.targets]}>"

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        nodes = [Node(i) for i in range(1, n*n+1)]
        node_pointers = []
        nodes[-1].final = True

        for i in range(1, n*n+1):
            y = n - 1 - ((i - 1) // n)
            x = (i - 1) % n if y % 2 != n % 2 else n - 1 - ((i - 1) % n)
            pi = board[y][x]
            # print(y, x, pi)
            node_pointers.append(pi - 1 if pi > 0 else None)

        start_index = node_pointers[0] or 0

        for i in range(n*n):
            node = nodes[i]
            for t in range(min(i + 1, n*n), min(i + 7, n*n)):
                if node_pointers[t] is None:
                    node.targets.append(nodes[t])
                else:
                    node.targets.append(nodes[node_pointers[t]])

        candidates = [nodes[start_index]]
        moves = 0
        # print(start_index, nodes, candidates, node_pointers)
        while candidates and not any([n.final for n in candidates]):
            candidates_next = []
            moves += 1
            for nc in candidates:
                if nc.visited:
                    continue
                nc.visited = True
                candidates_next.extend(nc.targets)
            candidates = candidates_next

        return moves if candidates else -1


s = Solution()

board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]

print(s.snakesAndLadders(board))

board = [[-1,-1],[-1,3]]
print(s.snakesAndLadders(board))


board = [[-1,-1,-1],[-1,9,8],[-1,8,9]]
print(s.snakesAndLadders(board))

board = [[1,1,-1],[1,1,1],[-1,1,1]]
print(s.snakesAndLadders(board))
