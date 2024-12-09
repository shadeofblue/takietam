# 100
from bintree import Tree, TreeNode
from typing import Optional

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        nodes_p = [p]
        nodes_q = [q]

        while any(nodes_p) or any(nodes_q):
            next_p = []
            next_q = []

            if len(nodes_p) != len(nodes_q):
                return False

            for node_p, node_q in zip(nodes_p, nodes_q):
                p_val = node_p.val if node_p else None
                q_val = node_q.val if node_q else None

                if p_val != q_val:
                    return False

                if node_p:
                    next_p.extend([node_p.left, node_p.right])
                    next_q.extend([node_q.left, node_q.right])

            nodes_p = next_p
            nodes_q = next_q

        return True


s = Solution()

ptree = Tree([1, 2, 3])
qtree = Tree([1, 2, 3])
ptree.draw()
qtree.draw()
print(s.isSameTree(ptree.root, qtree.root))

ptree = Tree([1, 2])
qtree = Tree([1, None, 2])
ptree.draw()
qtree.draw()
print(s.isSameTree(ptree.root, qtree.root))

ptree = Tree([])
qtree = Tree([0])
ptree.draw()
qtree.draw()
print(s.isSameTree(ptree.root, qtree.root))
