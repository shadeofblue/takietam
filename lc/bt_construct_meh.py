# 105
from bintree import Tree, TreeNode
from typing import Dict, Optional, List


class Solution:
    def __init__(self):
        self.nodes_map: Dict[int, TreeNode] = {}
        self.new_nodes_map: Dict[int, TreeNode] = {}

    def build_pre(self, root: TreeNode, pre_order: List[int], in_order: List[int], target: int, debug=False) -> TreeNode:
        if debug:
            print(f"--- build pre: {root=}, {pre_order=}, {in_order=}, {target=}, {self.nodes_map=}")
        node = root
        while node.val != target and pre_order:
            val = pre_order.pop(0)
            if debug:
                print(f"-------- bp ---- {node=}, {root=}, {val=}")
            if val not in self.nodes_map:
                next_node = TreeNode(val)
                self.nodes_map[next_node.val] = next_node
                if not node.left:
                    node.left = next_node
                else:
                    node.right = next_node
                node = next_node

        return node

    def build_in(self, root: TreeNode, pre_order: List[int], in_order: List[int], target: int, debug=False) -> TreeNode:
        if debug:
            print(f"--- build in: {root=}, {pre_order=}, {in_order=}, {target=}, {self.nodes_map=}")
        node = root
        self.new_nodes_map: Dict[int, TreeNode] = {}

        while node.val != target and in_order:
            val = in_order.pop(0)
            if debug:
                print(f"-------- bi ---- {node=}, {root=}, {val=}")
            if val in self.nodes_map:
                next_node = self.nodes_map.get(val)
                if node != root:
                    root.right = node
                    self.nodes_map.update(self.new_nodes_map)
                    self.new_nodes_map = {}

                node = next_node
                root = node
            else:
                move_node = True
                if debug:
                    print(f"---->>>>> new ---- {node=} {val=} [ {pre_order=}, {in_order=}")
                next_node = TreeNode(val)
                self.new_nodes_map[next_node.val] = next_node
                if node != root:
                    if debug:
                        print("node != root")
                    if node.val in pre_order and next_node.val != target and pre_order.index(next_node.val) > pre_order.index(node.val):
                        node.right = next_node
                        move_node = False
                    else:
                        next_node.left = node

                if val == target:
                    if debug:
                        print("val == target")
                    self.nodes_map.update(self.new_nodes_map)
                    self.new_nodes_map = {}
                    root.right = next_node

                if move_node:
                    node = next_node

        return node

    def buildTree(self, preorder: List[int], inorder: List[int], debug=False) -> Optional[TreeNode]:
        self.nodes_map = {}

        if len(preorder) != len(inorder):
            raise ValueError("Tree node lists invalid")

        if not preorder:
            return

        root = None
        node = None

        if debug:
            ttt = Tree()

        while preorder and inorder:
            if debug:
                print("------------------------------------------------------------")
                ttt.draw()
                print("------------------------------------------------------------")
                print(f"--- {preorder=}, {inorder=}")
            if len(preorder) > len(inorder) or not node:
                if not node:
                    node = root = TreeNode(val=preorder.pop(0))
                    self.nodes_map[node.val] = node
                    if debug:
                        ttt._root = root
                node = self.build_pre(node, preorder, inorder, inorder.pop(0) if inorder else None, debug=debug)
            else:
                node = self.build_in(node, preorder, inorder, preorder.pop(0) if preorder else None, debug=debug)

        return root



# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# print(f"{preorder=}, {inorder=}")
# out_head = Solution().buildTree(preorder, inorder, debug=False)
# t = Tree(root=out_head)
# t.draw()
#
#
# preorder = [1,2,3]
# inorder = [1,2,3]
# print(f"{preorder=}, {inorder=}")
# out_head = Solution().buildTree(preorder, inorder, debug=False)
# t = Tree(root=out_head)
# t.draw()
#
preorder = [1,4,2,3]
inorder = [1,2,3,4]
print(f"{preorder=}, {inorder=}")
out_head = Solution().buildTree(preorder, inorder, debug=True)
t = Tree(root=out_head)
t.draw()

# preorder = [1,5,2,3,4]
# inorder = [1,2,3,4,5]
# print(f"{preorder=}, {inorder=}")
# out_head = Solution().buildTree(preorder, inorder, debug=True)
# t = Tree(root=out_head)
# t.draw()
