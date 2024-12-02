# 61
from linkedlist import ListNode, LinkedList, iterate
from typing import Optional


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # print(f" ---- {head=}, {k=}")
        last = prev = None
        node = head
        cnt = rcnt = 0
        while node:
            cnt += 1
            if rcnt < k:
                rcnt += 1
            else:
                last = last.next if last else head
            prev = node
            node = node.next

        # print(f" --------- {last=}, {cnt=}, {rcnt=}")

        if cnt <= k and head:
            return self.rotateRight(head, k % cnt)

        if not last:
            return head

        prev.next = head
        new_head = last.next
        last.next = None
        return new_head





s = Solution()

ll = LinkedList([1,2,3,4,5])
k = 0
print(list(iterate(ll.head)), k)
out_head = s.rotateRight(ll.head, k)
print(list(iterate(out_head)))


ll = LinkedList([1,2,3,4,5])
k = 2
print(list(iterate(ll.head)), k)
out_head = s.rotateRight(ll.head, k)
print(list(iterate(out_head)))


ll = LinkedList([0,1,2])
k = 4
print(list(iterate(ll.head)), k)
out_head = s.rotateRight(ll.head, k)
print(list(iterate(out_head)))

ll = LinkedList([0,1,2])
k = 3
print(list(iterate(ll.head)), k)
out_head = s.rotateRight(ll.head, k)
print(list(iterate(out_head)))
