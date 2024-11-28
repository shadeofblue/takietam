# 92
from linkedlist import ListNode, LinkedList, iterate

from typing import Optional


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i = 1
        node = head
        first = before_first = prev = next =  None
        while node and i <= right:
            # print(i)
            next = node.next
            if i == left - 1:
                before_first = node
            if i == left:
                first = node
            if i > left:
                node.next = prev
            prev = node
            node = next
            i += 1

        # print(f"{head.ll=}, {before_first=}, {first=}, {node=}, {prev=}")

        if first:
            first.next = node

        if before_first:
            before_first.next = prev
        else:
            head = prev

        return head



s = Solution()

ll = LinkedList([1, 2, 3, 4, 5])
print(list(iterate(ll.head)))
left = 2
right = 4
rl = s.reverseBetween(ll.head, left, right)
print(ll)
print(list(iterate(rl)))

ll = LinkedList([5])
print(list(iterate(ll.head)))
left = 1
right = 1
rl = s.reverseBetween(ll.head, left, right)
print(ll)
print(list(iterate(rl)))

ll = LinkedList([3,5])
print(list(iterate(ll.head)))
left = 1
right = 2
rl = s.reverseBetween(ll.head, left, right)
print(ll)
print(list(iterate(rl)))
