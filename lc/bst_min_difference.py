# 530
from bintree import Tree, TreeNode
from typing import List, Optional


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values: List[int] = []

        def traverse(n: Optional[TreeNode]):
            if not n:
                return

            values.append(n.val)
            traverse(n.left)
            traverse(n.right)

        traverse(root)

        deltas = []
        print(values)
        values = sorted(values)
        for i in range(1, len(values)):
            deltas.append(values[i] - values[i - 1])
        return min(deltas)

s = Solution()

t = Tree([4,2,6,1,3])
print(s.getMinimumDifference(t.root))

t = Tree([1,0,48,None,None,12,49])
print(s.getMinimumDifference(t.root))

