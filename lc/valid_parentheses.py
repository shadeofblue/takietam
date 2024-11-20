# 20

OPENING = "({["
CLOSING = ")}]"
BRACKETS_MAP ={CLOSING[i]: OPENING[i] for i in range(len(CLOSING))}

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []
        for c in s:
            if c in OPENING:
                bracket_stack.append(c)
            else:
                if not bracket_stack or bracket_stack.pop() != BRACKETS_MAP[c]:
                    return False

        return not bool(bracket_stack)


sol = Solution()

s = "()"
print(s)
print(sol.isValid(s))

s = "()[]{}"
print(s)
print(sol.isValid(s))

s = "(]"
print(s)
print(sol.isValid(s))

s = "([])"
print(s)
print(sol.isValid(s))

