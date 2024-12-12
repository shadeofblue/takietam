# 112
from bintree import Tree, TreeNode
from typing import Optional

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traverse(r: TreeNode, prev_sum = 0):
            if not r:
                return False

            current_sum = r.val + prev_sum

            if (not r.left and not r.right) and current_sum == targetSum:
                return True

            result = traverse(r.left, current_sum) or traverse(r.right, current_sum)
            return result

        return traverse(root)

s = Solution()
t = Tree([5,4,8,11,None,13,4,7,2,None,None,None,1])
targetSum = 22
t.draw()
print(s.hasPathSum(t.root, targetSum))
