# 211
import string
from typing import Dict

class WordDictionary:

    def __init__(self):
        self.children: Dict[str, "WordDictionary"] = {}
        self.leaf: bool = False

    def addWord(self, word: str) -> None:
        if len(word) < 1:
            self.leaf = True
            return

        c = word[0]
        assert c in string.ascii_lowercase

        self.children.setdefault(c, WordDictionary())
        self.children.get(c).addWord(word[1:])

    def search(self, word: str) -> bool:
        if len(word) < 1:
            return self.leaf

        c = word[0]
        if c == ".":
            for child in self.children.values():
                if child.search(word[1:]):
                    return True
        else:
            child = self.children.get(c)
            if child:
                return child.search(word[1:])

        return False


def run(methods, args):
    instance = globals()[methods.pop(0)](*(args.pop(0)))
    out = [None]
    for i in range(len(methods)):
        m = getattr(instance, methods[i])
        a = args[i]
        out.append(m(*a))
    return out


methods = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
args = [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
print([f"{m}({', '.join(str(s) for s in a)})" for m, a in zip(methods, args)])
out = run(methods, args)
print(out)

