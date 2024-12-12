# 124
from bintree import Tree, TreeNode
from typing import Optional

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = None

        def traverse(r: Optional[TreeNode]) -> Optional[int]:
            nonlocal max_sum

            if not r:
                return None

            local_maxima = [r.val]

            max_left = traverse(r.left)
            max_right = traverse(r.right)

            if max_left is not None:
                local_maxima.extend([max_left, max_left + r.val])

            if max_right is not None:
                local_maxima.extend([max_right, max_right + r.val])

            if max_left is not None and max_right is not None:
                local_maxima.append(max_left + max_right + r.val)

            local_max = max(local_maxima)

            if max_sum is None or local_max > max_sum:
                max_sum = local_max

            # print(f"{r=}, {max_sum=}, {local_max=}, {local_maxima=}")

            return max(filter(lambda v: v is not None, [
                (max_left + r.val) if max_left else None,
                r.val,
                (max_right) + r.val if max_right else None,
            ]))

        traverse(root)

        return max_sum

s = Solution()
t = Tree([1,2,3])
t.draw()
print(s.maxPathSum(t.root))

t = Tree([-10,9,20,None,None,15,7])
t.draw()
print(s.maxPathSum(t.root))
