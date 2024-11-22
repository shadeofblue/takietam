# 141
from typing import Optional
from linkedlist import LinkedList, ListNode

class SolutionSet:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        vals = set()
        while head:
            # print(" ---> ", head)
            if head in vals:
                return True
            vals.add(head)
            if head.next:
                vals.add(head.val)
            head = head.next

        return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle = rabbit = head
        while turtle and rabbit:
            turtle = turtle.next
            rabbit = rabbit.next.next if rabbit.next else None
            if turtle and rabbit and turtle == rabbit:
                return True

        return False



s = Solution()
for l in range(2, 12):
    vals = list(range(l))
    ll = LinkedList(vals, 1)
    print(ll)
    print(s.hasCycle(ll.head))

vals = [1, 2]
ll = LinkedList(vals, 0)
print(ll)
print(s.hasCycle(ll.head))

vals = [1, 1]
ll = LinkedList(vals, -1)
print(ll)
print(s.hasCycle(ll.head))
