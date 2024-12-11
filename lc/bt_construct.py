# 105
from bintree import Tree, TreeNode
from typing import Dict, Optional, List, NamedTuple


class NodeBounds(NamedTuple):
    left: int
    right: int


class SolutionRecursive:
    def buildTree(self, pre_order: List[int], in_order: List[int], debug=False, level=0) -> Optional[TreeNode]:
        if debug:
            print(f"--- {level}: {pre_order=}, {in_order=}")

        if not pre_order:
            return None

        if len(pre_order) != len(in_order):
            raise ValueError("Not valid node lists")

        root_val = pre_order[0]
        root = TreeNode(root_val)
        root_inorder_idx = in_order.index(root_val)

        in_order_left = in_order[:root_inorder_idx]
        in_order_right = in_order[root_inorder_idx+1:]
        pre_order_left = list(filter(lambda v: v in in_order_left, pre_order))
        pre_order_right = list(filter(lambda v: v in in_order_right, pre_order))

        root.left = self.buildTree(pre_order_left, in_order_left, debug=debug, level=level+1)
        root.right = self.buildTree(pre_order_right, in_order_right, debug=debug, level=level+1)

        if debug:
            print(f"------ {level}: {root=}, {pre_order_left=}, {in_order_left=}, {pre_order_right=}, {in_order_right=}")

        return root

class Solution:

    def buildTree(self, pre_order: List[int], in_order: List[int], debug=False) -> Optional[TreeNode]:
        nodes: Dict[int, TreeNode] = {
            p: TreeNode(p) for p in pre_order
        }
        in_order_lut = {
            p: in_order.index(p) for p in pre_order
        }
        node_bounds_lut: Dict[int, NodeBounds] = {}

        root = nodes.get(pre_order[0])
        node_bounds_lut[root.val] = NodeBounds(0, len(pre_order))

        for i in range(len(pre_order)):
            p = pre_order[i]
            node = nodes[p]
            in_idx = in_order_lut[p]
            node_bounds = node_bounds_lut[p]

            bounds_left = NodeBounds(node_bounds.left, in_idx)
            bounds_right = NodeBounds(in_idx+1, node_bounds.right)

            in_left = in_order[bounds_left.left:bounds_left.right]
            in_right = in_order[bounds_right.left:bounds_right.right]

            if in_left:
                p_left = next(filter(lambda p: p in in_left, pre_order[i+1:]))
                node.left = nodes[p_left]
                node_bounds_lut[p_left] = bounds_left

            if in_right:
                p_right = next(filter(lambda p: p in in_right, pre_order[i+1:]))
                node.right = nodes[p_right]
                node_bounds_lut[p_right] = bounds_right

            if debug:
                print(f"--- {node=}, {bounds_left=}, {bounds_right=}, {len(in_left)=}, {len(in_right)=}")

        return root





preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
print(f"{preorder=}, {inorder=}")
out_head = Solution().buildTree(preorder, inorder, debug=True)
t = Tree(root=out_head)
t.draw()


preorder = [1,2,3]
inorder = [1,2,3]
print(f"{preorder=}, {inorder=}")
out_head = Solution().buildTree(preorder, inorder, debug=True)
t = Tree(root=out_head)
t.draw()

preorder = [1,4,2,3]
inorder = [1,2,3,4]
print(f"{preorder=}, {inorder=}")
out_head = Solution().buildTree(preorder, inorder, debug=True)
t = Tree(root=out_head)
t.draw()

preorder = [1,5,2,3,4]
inorder = [1,2,3,4,5]
print(f"{preorder=}, {inorder=}")
out_head = Solution().buildTree(preorder, inorder, debug=True)
t = Tree(root=out_head)
t.draw()

