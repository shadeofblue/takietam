# 399

from typing import Dict, List, Set, Optional

class Solution:
    def __init__(self):
        self.nodes: Dict[str, Dict[str, float]] = {}

    def findRoute(self, src: str, tgt: str) -> Optional[List[str]]:
        if src not in self.nodes or tgt not in self.nodes:
            return

        visited: Set[str] = set()
        routes: List[List[str]] = []

        def explore(nval: str, current_route: List[str]):
            # print(f"--- explore: {nval}")
            if nval in visited:
                return

            visited.add(nval)

            if nval == tgt:
                routes.append(current_route)
                return

            for n2val in self.nodes[nval].keys():
                # print(f"{nval} ---> {n2val}")
                new_route = current_route.copy()
                new_route.append(n2val)
                explore(n2val, new_route)

        explore(src, [src])

        route: Optional[List[str]] = None

        for r in routes:
            if not route or len(route) > len(r):
                route = r

        return route

    def getValue(self, nval: str, dval: str):
        route = self.findRoute(nval, dval)
        if not route:
            value = -1.0
        else:
            value = 1.0
            for ri in range(len(route) - 1):
                n = self.nodes[route[ri]]
                value *= n.get(route[ri + 1])

        # print(f"query: {nval} / {dval} -> {route} => {value}")
        return value


    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        for equation, value in zip(equations, values):
            nval, dval = equation
            self.nodes.setdefault(nval, {})
            self.nodes.setdefault(dval, {})

            n = self.nodes.get(nval)
            d = self.nodes.get(dval)

            n.setdefault(dval, value)
            d.setdefault(nval, 1 / value)

        responses = [self.getValue(nval, dval) for nval, dval in queries]
        return responses


equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(Solution().calcEquation(equations, values, queries))


equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
print(Solution().calcEquation(equations, values, queries))


equations = [["a","b"]]
values = [0.5]
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
print(Solution().calcEquation(equations, values, queries))

