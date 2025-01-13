# 102
from bintree import Tree, TreeNode
from typing import List, Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_values: List[List[int]] = []

        def traverse(n: Optional[TreeNode], lvl: int):
            if not n:
                return

            if len(level_values) < lvl + 1:
                level_values.append([])

            level_values[lvl].append(n.val)
            traverse(n.left, lvl + 1)
            traverse(n.right, lvl + 1)

        traverse(root, 0)
        return level_values


s = Solution()

t = Tree([3,9,20,None,None,15,7])
print(s.levelOrder(t.root))

t = Tree([1])
print(s.levelOrder(t.root))

t = Tree([])
print(s.levelOrder(t.root))
