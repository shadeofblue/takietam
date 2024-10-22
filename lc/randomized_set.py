# 380
import random

class RandomizedSetSet:

    def __init__(self):
        self.s = set()

    def insert(self, val: int) -> bool:
        if val in self.s:
            return False
        self.s.add(val)
        return True

    def remove(self, val: int) -> bool:
        try:
            self.s.remove(val)
            return True
        except KeyError:
            return False

    def getRandom(self) -> int:
        vals = [v for v in self.s]
        i = random.randrange(len(vals))
        return vals[i]



class RandomizedSet:

    def __init__(self):
        self.vals = {}

    def insert(self, val: int) -> bool:
        if val in self.vals:
            return False
        self.vals[val] = True
        return True

    def remove(self, val: int) -> bool:
        try:
            self.vals.pop(val)
            return True
        except KeyError:
            return False

    def getRandom(self) -> int:
        i = random.randrange(len(self.vals))
        vals = list(self.vals.keys())
        return vals[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

def run(methods, args):
    out = []
    rs = RandomizedSet()
    for i in range(len(methods)):
        m = methods[i]
        a = args[i]
        if m != rs.__class__.__name__:
            method = getattr(rs, m)
            out.append(method(*a))

    return out

methods = ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
args = [[],[1],[2],[2],[],[1],[2],[]]
print(run(methods, args))
