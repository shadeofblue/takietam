# 98
from bintree import Tree, TreeNode
from typing import Optional

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def is_valid(n: Optional[TreeNode], min_v: Optional[int] = None, max_v: Optional[int] = None) -> bool:
            # print(f"is valid? {n=}, {min_v=}, {max_v=}")
            if not n:
                return True

            if min_v is not None and n.val <= min_v:
                return False

            if max_v is not None and n.val >= max_v:
                return False

            left_valid = is_valid(n.left, min_v = min_v, max_v = n.val)
            if not left_valid:
                return False
            right_valid = is_valid(n.right, min_v = n.val, max_v = max_v)
            if not right_valid:
                return False

            return True

        return is_valid(root)


s = Solution()

t = Tree([2,1,3])
t.draw()
print(s.isValidBST(t.root))

t = Tree([5,1,4,None,None,3,6])
t.draw()
print(s.isValidBST(t.root))

t = Tree([2,2,2])
t.draw()
print(s.isValidBST(t.root))

t = Tree([0,None,-1])
t.draw()
print(s.isValidBST(t.root))

