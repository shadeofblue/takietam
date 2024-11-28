from linkedlist import ListNode, LinkedList, iterate

from typing import Optional, Tuple


class Solution:
    def reverse_group(self, first: ListNode, before_first: Optional[ListNode], after_last: Optional[ListNode]) -> Tuple[ListNode, ListNode]:
        # print(f"{first=}, {before_first=}, {after_last=}")
        node = first
        prev = None
        while node != after_last:
            next = node.next
            # print(f"---- {node=}, {prev=}, {next=}")
            if prev:
                node.next = prev
            prev = node
            node = next

        if before_first:
            before_first.next = prev

        first.next = after_last

        # print(f"---- {prev=}, {first=}")
        return prev, first

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        r_head = None
        first = node = head
        gcnt = 0
        before_first = None
        while node:
            next = node.next
            gcnt += 1
            if gcnt == k:
                begin, end = self.reverse_group(first, before_first, next)
                if not r_head:
                    r_head = begin
                before_first = end
                first = next
                gcnt = 0
            node = next

        return r_head



s = Solution()

ll = LinkedList([1,2,3,4,5])
k = 2
print(list(iterate(ll.head)), f"{k=}")
rl_head = s.reverseKGroup(ll.head, k )
print(list(iterate(rl_head)))

ll = LinkedList([1,2,3,4,5])
k = 3
print(list(iterate(ll.head)), f"{k=}")
rl_head = s.reverseKGroup(ll.head, k )
print(list(iterate(rl_head)))

ll = LinkedList([1,2,3,4,5,6])
k = 2
print(list(iterate(ll.head)), f"{k=}")
rl_head = s.reverseKGroup(ll.head, k )
print(list(iterate(rl_head)))

ll = LinkedList([1,2,3,4,5])
k = 1
print(list(iterate(ll.head)), f"{k=}")
rl_head = s.reverseKGroup(ll.head, k )
print(list(iterate(rl_head)))
