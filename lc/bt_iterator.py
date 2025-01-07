# 173
from bintree import Tree, TreeNode
from typing import Optional


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self._root = root
        self._iterator = self._next()
        self._cached_next: Optional[int] = None

    def _next(self):
        def traverse(r: TreeNode):
            if not r:
                yield from []
                return

            yield from traverse(r.left)
            yield r.val
            yield from traverse(r.right)

        yield from traverse(self._root)

    def next(self) -> int:
        if self._cached_next is not None:
            v = self._cached_next
            self._cached_next = None
            return v
        return next(self._iterator)

    def hasNext(self) -> bool:
        if self._cached_next is not None:
            return True

        try:
            self._cached_next = self.next()
            return True
        except StopIteration:
            return False


def run(methods, args):
    instance = globals()[methods.pop(0)](*(args.pop(0)))
    out = [None]
    for i in range(len(methods)):
        m = getattr(instance, methods[i])
        a = args[i]
        out.append(m(*a))
    return out

t = Tree([7, 3, 15, None, None, 9, 20])
t.draw()
methods = ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
args = [[t.root], [], [], [], [], [], [], [], [], []]
print([f"{m}({', '.join(str(s) for s in a)})" for m, a in zip(methods, args)])
out = run(methods, args)
print(out)

