# 226
from bintree import Tree, TreeNode
from typing import Optional


class SolutionInPlace:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = [root]
        while nodes:
            nodes_next = []
            for node in nodes:
                if node:
                    r = node.right
                    l = node.left
                    node.right = l
                    node.left = r
                    nodes_next.extend([r, l])

            nodes = nodes_next

        return root

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        new_root = TreeNode(root.val)
        new_root.left = self.invertTree(root.right)
        new_root.right = self.invertTree(root.left)
        return new_root


s = Solution()

tree = Tree([4,2,7,1,3,6,9])
tree.draw()
itree = Tree(root=s.invertTree(tree.root))
itree.draw()

tree = Tree([2, 1, 3])
tree.draw()
itree = Tree(root=s.invertTree(tree.root))
itree.draw()
