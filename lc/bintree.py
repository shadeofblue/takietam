from typing import Dict, List, Optional

class TreeNode:
    def __init__(self, val=None, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val} [l: {self.left.val if self.left else None}, r:{self.right.val if self.right else None}]"

    def __str__(self):
        return f"{self.val}"

class Tree:
    def __init__(self, vals: Optional[List] = None, root: Optional[TreeNode] = None, node_class = None):
        self._node_class = type(root) if root else node_class or TreeNode
        self._root: Optional[TreeNode] = root
        if vals:
            self.add_nodes(vals)

    def add_nodes(self, vals: List, level: int = 0, nodes: Optional[Dict[int, List[TreeNode]]] = None):
        # print(f"{vals=}, {level=}, {nodes=}")
        if not vals:
            return

        if not nodes:
            nodes = {}

        node_count = 2 ** level
        node_vals = vals[:node_count]
        vcnt = 0
        for val in node_vals:
            if val is not None:
                val = self._node_class(val)

            nodes.setdefault(level, [])
            nodes[level].append(val)

            if level == 0:
                self._root = val
            else:
                parents = nodes.get(level - 1)
                parent_idx, dir_idx = divmod(vcnt, 2)
                # print(f"---------add --- {level=}, {parents=}, {parent_idx=}, {dir_idx=}")
                parent = parents[parent_idx]
                if parent:
                    if dir_idx == 0:
                        parent.left = val
                    else:
                        parent.right = val
            vcnt += 1

        self.add_nodes(vals[node_count:], level + 1, nodes)

    @property
    def root(self) -> Optional[TreeNode]:
        return self._root

    def draw(self):
        print("--- Tree ---")
        level = 0
        nodes: Dict[int, List[Optional[TreeNode]]] = {0: [self._root]}

        while level in nodes and any(nodes[level]):
            print(", ".join([str(n) for n in nodes[level]]))
            for node in nodes[level]:
                # print(f"---------- {level=}, {node=}")
                nodes.setdefault(level + 1, [])
                if node:
                    nodes[level + 1].extend([node.left, node.right])
            level += 1

        print("----------")

