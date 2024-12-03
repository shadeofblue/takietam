from typing import List, Optional, Iterator

class ListNode:
    def __init__(self, x, ll: Optional["LinkedList"] = None):
        self.val = x
        self.next: Optional["ListNode"] = None
        self.prev: Optional["ListNode"] = None
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
            self.tail.next = node
            node.prev = self.tail
        self.__nodes.append(node)

    @property
    def head(self) -> Optional[ListNode]:
        return self.__nodes[0] if self.__nodes else None

    @property
    def tail(self) -> Optional[ListNode]:
        return self.__nodes[-1] if self.__nodes else None

    def set_pos(self, pos: int):
        if pos >= 0:
            self.__nodes[-1].next = self.__nodes[pos]

class PureLinkedList:
    head: Optional[ListNode]
    tail: Optional[ListNode]

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, node: ListNode):
        if not self.head:
            self.head = node
        if self.tail:
            self.tail.next = node

        node.prev = self.tail
        node.next = None

        self.tail = node
        self.size += 1

    def remove(self, node: ListNode):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        node.prev = None
        node.next = None
        self.size -= 1


def iterate(head: ListNode) -> Iterator:
    while head:
        yield head.val
        head = head.next

