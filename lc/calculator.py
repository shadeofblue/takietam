# 224
import re
from typing import Final, List, Optional, Union

ADD: Final = "+"
SUB: Final = "-"

OPERATORS = (ADD, SUB, )

class Expression:
    def __init__(self, parent: Optional["Expression"] = None, operator: Optional[str] = None, operands: Optional[List[Union["Expression", int, float]]] = None):
        self._parent: Optional[Expression] = parent
        self._operator: Optional[str] = operator
        if operands is not None:
            self._operands = operands
        else:
            self._operands = []
    def __repr__(self):
        return f"Exp<{self._operator if self._operator else ''}({self._operands})>"

    def set_operator(self, op: str):
        assert self._operator is None
        assert op in OPERATORS
        self._operator = op

    def add_value(self, v):
        if self._operator and not self._operands:
            self._operands.append(0)
        assert len(self._operands) <= 1
        self._operands.append(v)

    def _get_operand(self):
        val = self._operands.pop()
        if isinstance(val, Expression):
            return val.eval()
        return val

    @property
    def full(self):
        return len(self._operands) == 2

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    def nest(self):
        new_exp = Expression(parent=self, operator=self._operator, operands=self._operands)
        self._operands = [new_exp]
        self._operator = None

    def eval(self):
        if not self._operator:
            return self._get_operand()
        b = self._get_operand()
        a = self._get_operand()
        if self._operator == ADD:
            return a + b
        elif self._operator == SUB:
            return a - b

class Solution:
    def calculate(self, s: str) -> int:
        tokens = [list(filter(None, m))[0] for m in re.findall("(?P<operator>[\(\)\-\+])|(?P<value>\d+)", s)]
        exp = Expression()
        root = exp
        for t in tokens:
            if t in OPERATORS:
                if exp.full:
                    exp.nest()
                exp.set_operator(t)
            elif t == "(":
                new_exp = Expression(parent=exp)
                exp.add_value(new_exp)
                exp = new_exp
            elif t == ")":
                exp = exp.parent
            else:
                exp.add_value(int(t))
            # print(root)

        return root.eval()



sol = Solution()

s = "1 + 1"
print(s)
print(sol.calculate(s))

s = " 2-1 + 2 "
print(s)
print(sol.calculate(s))

s = "(1+(4+5+2)-3)+(6+8)"
print(s)
print(sol.calculate(s))

s = "- (145 + (43 + 51 + 21) - 34) + (688 + 18)"
print(s)
print(sol.calculate(s))
