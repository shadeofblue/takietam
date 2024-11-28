# 21
from linkedlist import LinkedList, ListNode, iterate
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = last = None
        while list1 or list2:
            if not list1 or (list2 and list1.val >= list2.val):
                current = list2
                list2 = list2.next
            else:
                current = list1
                list1 = list1.next
            if last:
                last.next = current

            last = current

            if not head:
                head = current

        return head

s = Solution()

list1 = LinkedList([1,2,4])
list2 = LinkedList([1,3,4])
print(list1)
print(list2)
out = s.mergeTwoLists(list1.head, list2.head)
print(list(iterate(out)))

list1 = LinkedList([])
list2 = LinkedList([])
print(list1)
print(list2)
out = s.mergeTwoLists(list1.head, list2.head)
print(list(iterate(out)))

list1 = LinkedList([])
list2 = LinkedList([0])
print(list1)
print(list2)
out = s.mergeTwoLists(list1.head, list2.head)
print(list(iterate(out)))
