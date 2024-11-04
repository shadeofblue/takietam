# 76
from typing import List, Dict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        solution = None
        tmap = {}
        smap = {}
        smap_idx: Dict[str, List[int]] = {}
        for c in t:
            tmap.setdefault(c, 0)
            smap.setdefault(c, 0)
            smap_idx.setdefault(c, [])
            tmap[c] += 1

        start_i = None
        for i in range(len(s)):
            c = s[i]
            if c in tmap:
                if start_i is None:
                    start_i = i
                if smap[c] < tmap[c]:
                    # print(f"---- completing, {c=}, {start_i=}, {i=}, {smap=}, {smap_idx=},")
                    # completing a set
                    smap[c] += 1
                    smap_idx[c].append(i)
                elif smap[c] == tmap[c]:
                    # print(f"------- complete, {c=}, {start_i=}, {i=}, {smap=}, {smap_idx=},")
                    # set already complete
                    smap_idx[c].append(i)
                    # print(f"------- complete2, {c=}, {start_i=}, {i=}, {smap=}, {smap_idx=},")

                    sc = s[start_i]
                    while sc not in tmap or len(smap_idx[sc]) > tmap[sc]:
                        if sc in tmap:
                            # print(f"{sc=}, {len(smap_idx[sc])=}, {tmap[sc]=}")
                            smap_idx[sc].pop(0)
                        start_i += 1
                        sc = s[start_i]

                    # print(f"------- complete3, {c=}, {start_i=}, {i=}, {smap=}, {smap_idx=},")

                if smap == tmap:
                    slen = i - start_i + 1
                    # print(f"---------- solution?, {solution=}, {slen=}, {c=}, {start_i=}, {i=}, {smap=}, {smap_idx=},")
                    if solution is None or solution[1] - solution[0] > slen:
                        solution = (start_i, i + 1)

        return s[solution[0]:solution[1]] if solution else ""


s = "ADOBECODEBANC"
t = "ABC"
print(f"{s=}, {t=}")
print(Solution().minWindow(s, t))

s = "a"
t = "a"
print(f"{s=}, {t=}")
print(Solution().minWindow(s, t))

s = "a"
t = "aa"
print(f"{s=}, {t=}")
print(Solution().minWindow(s, t))
