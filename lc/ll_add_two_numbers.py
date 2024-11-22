# 2

from typing import Optional
from linkedlist import LinkedList, ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = node = None

        carry = 0
        while l1 or l2 or carry:
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            carry, s = divmod(d1 + d2 + carry, 10)
            new_node = ListNode(s)
            if not head:
                head = new_node
            else:
                node.next = new_node
            node = new_node

        return head


def print_num(l: ListNode):
    digits = []
    while l:
        digits.append(str(l.val))
        l = l.next
    print("".join(reversed(digits)))

s = Solution()

l1 = LinkedList([2,4,3])
l2 = LinkedList([5,6,4])
print_num(l1.head)
print_num(l2.head)
print_num(s.addTwoNumbers(l1.head, l2.head))

l1 = LinkedList([0])
l2 = LinkedList([0])
print_num(l1.head)
print_num(l2.head)
print_num(s.addTwoNumbers(l1.head, l2.head))

l1 = LinkedList([9,9,9,9,9,9,9])
l2 = LinkedList([9,9,9,9])
print_num(l1.head)
print_num(l2.head)
print_num(s.addTwoNumbers(l1.head, l2.head))
