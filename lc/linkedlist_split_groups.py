# 86
from linkedlist import ListNode, LinkedList, iterate
from typing import Optional

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        p1_head = p2_head = p1 = p2 = None
        node = head
        while node:
            if node.val < x:
                if p1:
                    p1.next = node
                if not p1_head:
                    p1_head = node

                p1 = node

            else:
                if p2:
                    p2.next = node
                if not p2_head:
                    p2_head = node

                p2 = node

            node = node.next

        if not p1_head:
            return p2_head

        p1.next = p2_head
        if p2:
            p2.next = None
        return p1_head



s = Solution()

ll = LinkedList([1,4,3,2,5,2])
x = 3
print(list(iterate(ll.head)), f"{x=}")
phead = s.partition(ll.head, x)
print(list(iterate(phead)))

ll = LinkedList([2, 1])
x = 2
print(list(iterate(ll.head)), f"{x=}")
phead = s.partition(ll.head, x)
print(list(iterate(phead)))

ll = LinkedList([4, 3])
x = 2
print(list(iterate(ll.head)), f"{x=}")
phead = s.partition(ll.head, x)
print(list(iterate(phead)))

ll = LinkedList([0, 1])
x = 2
print(list(iterate(ll.head)), f"{x=}")
phead = s.partition(ll.head, x)
print(list(iterate(phead)))

