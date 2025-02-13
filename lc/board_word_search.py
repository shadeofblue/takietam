# 212
from typing import List, Dict, Tuple, Set

class Solution:
    def __init__(self):
        self.char_map: Dict[str, List[Tuple[int, int]]] = {}

    def map_chars(self, board: List[List[str]]) -> None:
        for y in range(len(board)):
            row = board[y]
            for x in range(len(row)):
                c = row[x]
                self.char_map.setdefault(c, [])
                self.char_map[c].append((x, y))

    def search_word(self, board: List[List[str]], word: str) -> bool:


        def explore(x: int, y: int, w: str, visited: Set[Tuple[int, int]]) -> bool:
            # out of bounds
            if y < 0 or x < 0 or y >= len(board) or x >= len(board[0]):
                return False
            # already visited
            if (x, y) in visited:
                return False
            # wrong path
            if board[y][x] != w[0]:
                return False

            visited.add((x, y))

            # success! :)
            if len(w) == 1:
                return True

            candidates = [
                (x - 1, y, w[1:]),
                (x + 1, y, w[1:]),
                (x, y - 1, w[1:]),
                (x, y + 1, w[1:]),
            ]
            for c in candidates:
                visited_new = visited.copy()
                if explore(*c, visited=visited_new):
                    return True

        for x, y in self.char_map.get(word[0], []):
            if explore(x, y, word, set()):
                return True

        return False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = []
        self.map_chars(board)
        for word in words:
            if self.search_word(board, word):
                result.append(word)

        return result

def draw_board(board: List[List[str]]):
    print("--------------")
    print("\n".join(["".join(row) for row in board]))
    print("--------------")


board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain", "oathk"]
draw_board(board)
print(f"{words=}")
print(Solution().findWords(board, words))

board = [["a","b"],["c","d"]]
words = ["abcb"]
draw_board(board)
print(f"{words=}")
print(Solution().findWords(board, words))
