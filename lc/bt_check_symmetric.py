# 101
from bintree import Tree, TreeNode
from typing import Optional, Iterator


class Solution:
    def get_next_child(self, root: Optional[TreeNode], left_first: bool) -> Iterator[Optional[TreeNode]]:
        # print(f"-------- {root=}, {left_first=}")
        if root:
            nodes = [root.left, root.right] if left_first else [root.right, root.left]
            for n in nodes:
                yield n
                yield from self.get_next_child(n, left_first)


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        for l, r in zip(
                self.get_next_child(root, True),
                self.get_next_child(root, False)
        ):
            # print(f"{l=}, {r=}")
            if type(l) != type(r):
                return False
            if l and l.val != r.val:
                return False
        return True


s = Solution()

tree = Tree([1,2,2,3,4,4,3])
tree.draw()
print(s.isSymmetric(tree.root))

tree = Tree([1,2,2,None,3,None,3])
tree.draw()
print(s.isSymmetric(tree.root))
