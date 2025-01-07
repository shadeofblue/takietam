from bintree import Tree, TreeNode
from typing import Dict, List, Optional


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        max_level = -1
        level_values: Dict[int, List[int]] = {}

        def traverse(n: Optional[TreeNode], lvl: int):
            nonlocal max_level

            if not n:
                return

            level_values.setdefault(lvl, [])
            level_values[lvl].append(n.val)
            max_level = max(max_level, lvl)

            traverse(n.left, lvl + 1)
            traverse(n.right, lvl + 1)

        traverse(root, 0)
        return [sum(level_values[n]) / len(level_values[n]) for n in range(max_level + 1)]


s = Solution()

t = Tree([3,9,20,None,None,15,7])
t.draw()
print(s.averageOfLevels(t.root))


t = Tree([3,9,20,15,7])
t.draw()
print(s.averageOfLevels(t.root))

