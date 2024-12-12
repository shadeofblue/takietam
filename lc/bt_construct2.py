# 106
from bintree import Tree, TreeNode
from typing import Dict, List, Optional, NamedTuple

class NodeBounds(NamedTuple):
    left: int
    right: int

class Solution:

    def buildTree(self, in_order: List[int], post_order: List[int], debug=False) -> Optional[TreeNode]:
        nodes_map: Dict[int, TreeNode] = { v: TreeNode(v) for v in post_order }
        bounds_map: Dict[int, NodeBounds] = {}
        root_val = post_order[-1]
        root = nodes_map[root_val]
        bounds_map[root_val] = NodeBounds(0, len(in_order))

        for i in range(len(post_order) - 1, -1, -1):
            v = post_order[i]
            node = nodes_map[v]
            node_bounds = bounds_map[v]
            children_range = post_order[:i]
            in_idx = in_order.index(v)

            bounds_right = NodeBounds(in_idx+1, node_bounds.right)
            bounds_left = NodeBounds(node_bounds.left, in_idx)

            in_right = in_order[bounds_right.left:bounds_right.right]
            in_left = in_order[bounds_left.left:bounds_left.right]

            if in_right:
                v_right = next(filter(lambda v: v in in_right, reversed(children_range)))
                node.right = nodes_map[v_right]
                bounds_map[v_right] = bounds_right

            if in_left:
                v_left = next(filter(lambda v: v in in_left, reversed(children_range)))
                node.left = nodes_map[v_left]
                bounds_map[v_left] = bounds_left

            if debug:
                print(f"---- {node=}, {node_bounds=}")

        return root



s = Solution()

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
t = Tree(root=s.buildTree(inorder, postorder, debug=True))
t.draw()

inorder = [-1]
postorder = [-1]
t = Tree(root=s.buildTree(inorder, postorder, debug=True))
t.draw()


