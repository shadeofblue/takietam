# 129
from bintree import Tree, TreeNode
from typing import Optional

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0

        def traverse(r: Optional[TreeNode], number = 0):
            nonlocal total
            if not r:
                return

            current_number = number + r.val

            if not r.left and not r.right:
                total += current_number

            traverse(r.left, current_number * 10)
            traverse(r.right, current_number * 10)

        traverse(root)

        return total


s = Solution()
t = Tree([1,2,3])
t.draw()
print(s.sumNumbers(t.root))
