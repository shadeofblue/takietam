from bintree import Tree, TreeNode
from typing import List, Optional

def find_node(r: TreeNode, v: int):
    if not r:
        return

    if r.val == v:
        return r

    n = find_node(r.left, v)
    if n:
        return n

    n = find_node(r.right, v)
    if n:
        return n

class Solution:
    def find_node(self, r: TreeNode, n: TreeNode) -> Optional[List[TreeNode]]:
        if not r:
            return

        if r == n:
            return [r]

        found = self.find_node(r.left, n)

        if not found:
            found = self.find_node(r.right, n)

        if found:
            found.insert(0, r)

        return found


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = self.find_node(root, p)
        q_path = self.find_node(root, q)

        zipped = zip(p_path, q_path)

        common = list(filter(lambda pair: pair[0] == pair[1], zipped))
        return common[-1][0]


s = Solution()
t = Tree([3,5,1,6,2,0,8,None,None,7,4])
p = find_node(t.root, 5)
q = find_node(t.root, 1)
t.draw()
print(f"{p=}, {q=}")
print(s.lowestCommonAncestor(t.root, p, q))


t = Tree([3,5,1,6,2,0,8,None,None,7,4])
p = find_node(t.root, 5)
q = find_node(t.root, 4)
t.draw()
print(f"{p=}, {q=}")
print(s.lowestCommonAncestor(t.root, p, q))

