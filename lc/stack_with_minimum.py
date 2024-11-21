# 155
from typing import List

class Stack:
    def __init__(self):
        self.stack: List[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def __bool__(self):
        return bool(self.stack)


class MinStack(Stack):

    def __init__(self):
        super().__init__()
        self.minima_stack = Stack()

    def push(self, val: int) -> None:
        super().push(val)
        if not self.minima_stack or self.minima_stack.top() >= val:
            self.minima_stack.push(val)

    def pop(self) -> None:
        v = self.stack.pop()
        if self.minima_stack.top() == v:
            self.minima_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minima_stack.top()



def run(methods, args):
    out = []
    st = MinStack()
    for i in range(len(methods)):
        m = methods[i]
        a = args[i]
        if m != st.__class__.__name__:
            method = getattr(st, m)
            print(f"---{st.__class__.__name__}.{m}({','.join(str(ae) for ae in a)})")
            out.append(method(*a))

    return out


methods = ["MinStack","push","push","push","getMin","pop","top","getMin"]
args = [[],[-2],[0],[-3],[],[],[],[]]
print(run(methods, args))

