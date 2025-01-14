# 230
from bintree import Tree, TreeNode
from typing import List, Optional

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values: List[int] = []
        solution = None

        def traverse(n: Optional[TreeNode]):
            nonlocal solution

            if solution:
                return

            if not n:
                return

            traverse(n.left)
            values.append(n.val)
            if len(values) == k:
                solution = values[-1]
            traverse(n.right)

        traverse(root)
        return solution


s = Solution()

t = Tree([3,1,4,None,2])
k = 1
print(s.kthSmallest(t.root, k))

t = Tree([5,3,6,2,4,None,None,1])
k = 3
print(s.kthSmallest(t.root, k))
