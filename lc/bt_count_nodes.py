from bintree import Tree, TreeNode
from typing import List, Optional


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = 0

        def traverse(n: TreeNode):
            nonlocal count
            count += 1
            if n.left:
                traverse(n.left)
            if n.right:
                traverse(n.right)

        if root:
            traverse(root)

        return count


s = Solution()

t = Tree([1,2,3,4,5,6])
t.draw()
print(s.countNodes(t.root))
