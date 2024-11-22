from typing import List, Optional

class ListNode:
    def __init__(self, x, ll: Optional["LinkedList"] = None):
        self.val = x
        self.next = None
        self.ll = ll

    def __repr__(self):
        return f"{self.val}"


class LinkedList:
    __nodes: List[ListNode]

    def __init__(self, vals: Optional[List] = None, pos: int = -1):
        self.__nodes = []
        if vals:
            for v in vals:
                self.add(v)
        self.set_pos(pos)

    def __repr__(self):
        return " | ".join([f"{n.val}{' -> ' + str(n.next.val) if n.next else ''}" for n in self.__nodes])

    def add(self, x):
        node = ListNode(x, ll=self)
        if self.__nodes:
            self.__nodes[-1].next = node
        self.__nodes.append(node)

    @property
    def head(self):
        return self.__nodes[0]

    def set_pos(self, pos: int):
        if pos >= 0:
            self.__nodes[-1].next = self.__nodes[pos]
