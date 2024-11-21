# 150
from typing import List

ADD = "+"
SUB = "-"
MUL = "*"
DIV = "/"


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: List[int] = []

        for t in tokens:
            if t in [ADD, SUB, MUL, DIV]:
                b = stack.pop()
                a = stack.pop()
                if t == ADD:
                    stack.append(a + b)
                elif t == SUB:
                    stack.append(a - b)
                elif t == MUL:
                    stack.append(a * b)
                elif t == DIV:
                    stack.append(int(a / b))
            else:
                stack.append(int(t))

        return stack.pop()


s = Solution()


tokens = ["2","1","+","3","*"]
print(tokens)
print(s.evalRPN(tokens))

tokens = ["4","13","5","/","+"]
print(tokens)
print(s.evalRPN(tokens))

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(tokens)
print(s.evalRPN(tokens))
