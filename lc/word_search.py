from typing import List, Set, Tuple, Iterable, Dict

class Solution:
    def index(self, iterable: Iterable[str]):
        m = dict()
        for c in iterable:
            m.setdefault(c, 0)
            m[c] += 1
        return m

    def contains(self, idx: Dict[str, int], needle: Dict[str, int]):
        try:
            return all(
                idx[char] >= needle[char]
                for char in needle.keys()
            )
        except KeyError:
            return False

    def board_contains(self, board: List[List[str]], word: str):
        return self.contains(self.index(sum(board, start=[])), self.index(word))

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not self.board_contains(board, word):
            return False

        def search(sx: int, sy: int):
            cx = sx
            cy = sy
            candidates = [(cx, cy, "", set()), ]

            while candidates:
                # print("   ---   ", candidates)
                new_candidates = []
                for cx, cy, path, visited in candidates:
                    if path == word:
                        return True

                    next_letter = word[len(path)]
                    new_path = path + next_letter
                    if (
                            0 <= cy < len(board)
                            and 0 <= cx < len(board[0])
                            and board[cy][cx] == next_letter
                            and (cx, cy) not in visited
                            and len(path) < len(word)
                    ):
                        visited.add((cx, cy))
                        new_candidates += [
                            (cx - 1, cy, new_path, set(visited)),
                            (cx + 1, cy, new_path, set(visited)),
                            (cx, cy - 1, new_path, set(visited)),
                            (cx, cy + 1, new_path, set(visited)),
                        ]
                candidates = new_candidates

            return False

        for y in range(len(board)):
            for x in range(len(board[0])):
                if search(x, y):
                    return True

        return False


def draw_board(board: List[List[str]]):
    print("--------------")
    print("\n".join(["".join(row) for row in board]))
    print("--------------")


s = Solution()


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

draw_board(board)
print(word)
# print(Solution().board_contains(board, word))
print(Solution().exist(board, word))
print("--------------------------------------------------------------------")


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"

draw_board(board)
print(word)
# print(Solution().board_contains(board, word))
print(Solution().exist(board, word))
print("--------------------------------------------------------------------")

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","B"]]
word = "ABCB"


draw_board(board)
print(word)
# print(Solution().board_contains(board, word))
print(Solution().exist(board, word))
print("--------------------------------------------------------------------")

