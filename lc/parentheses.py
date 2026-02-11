from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        visited = set()
        solutions = []

        stack = []

        while True:
            current, opened, closed = stack[-1] if stack else ("", 0, 0)
            # print("     ---- ", current, opened, closed, stack)

            if n == opened == closed:
                # print("SOLUTION: ", current)
                solutions.append(current)
                stack.pop()
                continue

            if n > opened:
                candidate = current + "("
                if candidate not in visited:
                    stack.append((candidate, opened + 1, closed))
                    visited.add(candidate)
                    continue

            if n > closed < opened:
                candidate = current + ")"
                if candidate not in visited:
                    stack.append((candidate, opened, closed + 1))
                    visited.add(candidate)
                    continue

            if stack:
                stack.pop()
                continue

            return solutions


print("--------------------------------------------------------------------", 1)
s = Solution().generateParenthesis(1)
print(s)

print("--------------------------------------------------------------------", 2)
s = Solution().generateParenthesis(2)
print(s)

print("--------------------------------------------------------------------", 3)
s = Solution().generateParenthesis(3)
print(s)

print("--------------------------------------------------------------------", 4)
s = Solution().generateParenthesis(4)
print(s)
