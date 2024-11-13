# 205

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        for i in range(len(s)):
            sc = s[i]
            tc = t[i]
            smap.setdefault(sc, tc)
            tmap.setdefault(tc, sc)
            if smap[sc] != tc or tmap[tc] != sc:
                # print(f"@{i}: needed: {sc} => {tc}, actually {sc} => {smap[sc]} / {tc} <= {tmap[tc]}.")
                return False
        return True


solution = Solution()
s = "egg"
t = "add"
print(s, t)
print(solution.isIsomorphic(s, t))

s = "foo"
t = "bar"
print(s, t)
print(solution.isIsomorphic(s, t))

s = "paper"
t = "title"
print(s, t)
print(solution.isIsomorphic(s, t))

s = "badc"
t = "baba"
print(s, t)
print(solution.isIsomorphic(s, t))

