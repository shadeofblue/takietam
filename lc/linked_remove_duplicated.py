# 82
from linkedlist import LinkedList, ListNode, iterate

from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last_unique = prev = None
        dcnt = 1
        node = head
        while node:
            # print(f"{node=}, {prev=}, {head=}, {last_unique=}, {dcnt=}")
            if prev and prev.val == node.val:
                dcnt += 1
            elif dcnt > 1:
                dcnt = 1
                if last_unique:
                    last_unique.next = node
                else:
                    head = node
            else:
                last_unique = prev
            prev = node
            node = node.next

        if dcnt > 1:
            if last_unique:
                last_unique.next = node
            else:
                return None

        return head



s = Solution()

ll = LinkedList([1,2,3,3,4,4,5])
print(list(iterate(ll.head)))
shead = s.deleteDuplicates(ll.head)
print(list(iterate(shead)))

ll = LinkedList([1,1,1,2,3])
print(list(iterate(ll.head)))
shead = s.deleteDuplicates(ll.head)
print(list(iterate(shead)))

ll = LinkedList([1,1,1,2,3,3,3])
print(list(iterate(ll.head)))
shead = s.deleteDuplicates(ll.head)
print(list(iterate(shead)))

ll = LinkedList([1,1])
print(list(iterate(ll.head)))
shead = s.deleteDuplicates(ll.head)
print(list(iterate(shead)))

