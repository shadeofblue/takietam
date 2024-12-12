from bintree import Tree, TreeNode
from typing import Optional


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:

        def traverse(r: TreeNode) -> TreeNode:
            bottom = r
            left = r.left
            right = r.right

            if left:
                bottom = traverse(left)
                r.left = None
                r.right = left

            if right:
                new_bottom = traverse(right)
                bottom.right = right
                bottom = new_bottom

            return bottom

        if root:
            traverse(root)

        return root

s = Solution()
t = Tree([1,2,5,3,4,None,6])
t.draw()
s.flatten(t.root)
t.draw()
