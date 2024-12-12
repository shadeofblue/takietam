# 117
from bintree import Tree, TreeNode


class Node(TreeNode):
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        super().__init__(val, left, right)
        self.next = next

    def __repr__(self):
        return f"{self.val} [l: {self.left.val if self.left else None}, r:{self.right.val if self.right else None}, n: {self.next.val if self.next else None}]"

    def __str__(self):
        return f"{self.val} -> {self.next.val if self.next else '#'}"


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        leftmost = {}

        def traverse(r: 'Node', l = 0):
            r.next = leftmost.get(l)
            leftmost[l] = r
            if r.right:
                traverse(r.right, l+1)
            if r.left:
                traverse(r.left, l+1)

        if root:
            traverse(root)

        return root

s = Solution()
t = Tree([1,2,3,4,5,None,7], node_class=Node)
s.connect(t.root)
t.draw()
