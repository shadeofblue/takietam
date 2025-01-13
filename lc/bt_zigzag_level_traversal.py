# 103
from bintree import Tree, TreeNode
from typing import List, Optional


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
        zigzag_level_values = []
        for l in range(len(level_values)):
            zigzag_level_values.append(level_values[l] if l % 2 == 0 else list(reversed(level_values[l])))

        return zigzag_level_values


s = Solution()

t = Tree([3,9,20,None,None,15,7])
print(s.zigzagLevelOrder(t.root))

t = Tree([1])
print(s.zigzagLevelOrder(t.root))

t = Tree([])
print(s.zigzagLevelOrder(t.root))
