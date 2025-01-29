# 208
from typing import Dict, Optional

class Trie:
    prefix: str
    children: Dict[str, "Trie"]
    is_leaf: bool

    def __repr__(self):
        return f"Trie <{self.prefix=}, {self.is_leaf=}, children={list(self.children.keys())}>"

    def __init__(self, prefix = ""):
        self.prefix = prefix
        self.children = {}
        self.is_leaf = False

    def _get_local_prefix(self, word: str):
        return word[:len(self.prefix) + 1]

    def _get_child_trie(self, word: str, create = False) -> Optional["Trie"]:
        lp = self._get_local_prefix(word)
        child = self.children.get(lp)
        if not child and create:
            child = self.children.setdefault(lp, Trie(lp))
        return child

    def insert(self, word: str) -> None:
        assert word.startswith(self.prefix)

        if word == self.prefix:
            self.is_leaf = True
            return

        child = self._get_child_trie(word, create=True)
        child.insert(word)

    def search(self, word: str, include_non_leaves = False) -> bool:
        if word == self.prefix and (self.is_leaf or include_non_leaves):
            return True

        child = self._get_child_trie(word)
        if not child:
            return False

        return child.search(word, include_non_leaves=include_non_leaves)


    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, include_non_leaves=True)


def run(methods, args):
    instance = globals()[methods.pop(0)](*(args.pop(0)))
    out = [None]
    for i in range(len(methods)):
        m = getattr(instance, methods[i])
        a = args[i]
        out.append(m(*a))
    return out


methods = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
args = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
print([f"{m}({', '.join(str(s) for s in a)})" for m, a in zip(methods, args)])
out = run(methods, args)
print(out)
