# 146

from dataclasses import dataclass
from typing import Dict, Optional

class ListNode:
    def __init__(self, x, ll: Optional["LinkedList"] = None):
        self.val = x
        self.next: Optional["ListNode"] = None
        self.prev: Optional["ListNode"] = None
        self.ll = ll

    def __repr__(self):
        return f"{self.val}"


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


@dataclass
class LRUCacheEntry:
    node: ListNode
    val: Optional[int] = None

class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache_usage = PureLinkedList()
        self._storage: Dict [int, LRUCacheEntry] = {}

    def get(self, key: int) -> int:
        entry = self._storage.get(key)
        if not entry:
            return -1
        self._cache_usage.remove(entry.node)
        self._cache_usage.add(entry.node)
        return entry.val

    def put(self, key: int, value: int) -> None:
        entry = self._storage.get(key)
        if not entry:
            if len(self._storage.keys()) == self._capacity:
                least_used = self._cache_usage.head
                self._cache_usage.remove(least_used)
                del self._storage[least_used.val]

            entry = LRUCacheEntry(ListNode(key))
            self._storage[key] = entry
        else:
            self._cache_usage.remove(entry.node)

        self._cache_usage.add(entry.node)
        entry.val = value




def run(methods, args):
    instance = globals()[methods.pop(0)](*(args.pop(0)))
    out = [None]
    for i in range(len(methods)):
        m = getattr(instance, methods[i])
        a = args[i]
        out.append(m(*a))
    return out

methods = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
args = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
print([f"{m}({', '.join(str(s) for s in a)})" for m, a in zip(methods, args)])
out = run(methods, args)
print(out)