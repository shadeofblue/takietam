
from typing import Iterator, Optional, List

class Node:
    def __init__(self, x, next: Optional["Node"] = None, random: Optional["Node"] = None):
        self.val = x
        self.next = None
        self.random = None

    def __repr__(self):
        return f"id={id(self)}|v={self.val}|rid={id(self.random) if self.random else None}|r={self.random.val if self.random else None}"

def construct_linked(lst: List) -> Optional[Node]:
    nodes: List[Node] = []
    for l in lst:
        node = Node(l[0])
        if nodes:
            nodes[-1].next = node
        nodes.append(node)
    for i in range(len(lst)):
        l = lst[i]
        if l[1] is not None:
            nodes[i].random = nodes[l[1]]

    return nodes[0] if nodes else None

def iterate(head: Node) -> Iterator:
    while head:
        yield head
        head = head.next

def print_list(head: Node):
    print([h for h in iterate(head)])


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_head: Optional[Node] = None
        new_last: Optional[Node] = None
        node = head

        node_lut = {}
        while node:
            nodeid = id(node)
            new_node = Node(node.val)
            node_lut[nodeid] = new_node
            if new_last:
                new_last.next = new_node
            new_last = new_node
            if not new_head:
                new_head = new_node
            node = node.next

        node = head
        while node:
            nodeid = id(node)
            new_node = node_lut[nodeid]
            if node.random:
                new_node.random = node_lut[id(node.random)]
            node = node.next

        return new_head


s = Solution()
head = construct_linked([[7,None],[13,0],[11,4],[10,2],[1,0]])
print_list(head)
copy = s.copyRandomList(head)
print_list(copy)
