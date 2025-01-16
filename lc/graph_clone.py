# 133



from typing import Optional, Dict

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return f"{self.val}: {[n.val for n in self.neighbors]}"

def print_network(n: Optional[Node]):
    print("------")
    visited = set()

    def explore(en: Optional[Node]):
        if not en:
            return

        if en in visited:
            return

        print(en)
        visited.add(en)
        for neighbor in en.neighbors:
            explore(neighbor)

    explore(n)


def build_network(adjacency_list):
    nodes_map: Dict[int, Node] = {}

    for idx, _ in enumerate(adjacency_list, start=1):
        nodes_map[idx] = Node(idx)

    for idx, node_neighbors in enumerate(adjacency_list, start=1):
        node = nodes_map[idx]
        for neighbor_idx in node_neighbors:
            node.neighbors.append(nodes_map[neighbor_idx])

    return nodes_map[1] if nodes_map else None


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones_map: Dict[int, Node] = {}

        def explore_and_clone(n: Optional[Node]):
            if not n:
                return

            if id(n) in clones_map:
                return clones_map[id(n)]

            clone = Node(n.val)
            clones_map[id(n)] = clone
            for cn in n.neighbors:
                clone.neighbors.append(explore_and_clone(cn))

            return clone

        cloned = explore_and_clone(node)
        return cloned

s = Solution()

edges = [[2,4],[1,3],[2,4],[1,3]]
node = build_network(edges)
print_network(node)
cnode = s.cloneGraph(node)
print_network(cnode)

edges = [[]]
node = build_network(edges)
print_network(node)
cnode = s.cloneGraph(node)
print_network(cnode)

edges = []
node = build_network(edges)
print_network(node)
cnode = s.cloneGraph(node)
print_network(cnode)
