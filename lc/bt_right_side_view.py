from bintree import Tree, TreeNode
from typing import List, Optional


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightmost = []

        def traverse(n: Optional[TreeNode], lvl: int):
            nonlocal rightmost
            if not n:
                return

            if len(rightmost) < lvl + 1:
                rightmost.append(n.val)
            else:
                rightmost[lvl] = n.val

            traverse(n.left, lvl + 1)
            traverse(n.right, lvl + 1)

        traverse(root, 0)

        return rightmost



s = Solution()

tree = Tree([1,2,3,None,5,None,4])
tree.draw()
print(s.rightSideView(tree.root))

tree = Tree([1,2,3,4,None,None,None,5])
tree.draw()
print(s.rightSideView(tree.root))

tree = Tree([1,None,3])
tree.draw()
print(s.rightSideView(tree.root))

tree = Tree([])
tree.draw()
print(s.rightSideView(tree.root))

