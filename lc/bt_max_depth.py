# 104
from bintree import Tree, TreeNode
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        lvl = 0
        nodes = [root]
        while any(nodes):
            nodes_next = []
            for node in nodes:
                if node:
                    nodes_next.extend([node.left, node.right])
            lvl += 1
            nodes = nodes_next

        return lvl

s = Solution()

tree = Tree([3,9,20,None,None,15,7])
tree.draw()
print(s.maxDepth(tree.root))
