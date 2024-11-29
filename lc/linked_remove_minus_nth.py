# 19
from linkedlist import ListNode, LinkedList, iterate

from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = nth = head
        prev = None
        cnt = 1
        while node.next:
            if cnt >= n:
                prev = nth
                nth = nth.next
            node = node.next
            cnt += 1

        # print(f"{prev=}, {nth=}, {node=}, {head=}")

        if nth == head:
            return nth.next

        prev.next = nth.next
        return head





s = Solution()
ll = LinkedList([1,2,3,4,5])
n = 2
print(list(iterate(ll.head)))
shead = s.removeNthFromEnd(ll.head, n)
print(list(iterate(shead)))


s = Solution()
ll = LinkedList([1])
n = 1
print(list(iterate(ll.head)))
shead = s.removeNthFromEnd(ll.head, n)
print(list(iterate(shead)))

s = Solution()
ll = LinkedList([1, 2])
n = 1
print(list(iterate(ll.head)))
shead = s.removeNthFromEnd(ll.head, n)
print(list(iterate(shead)))
