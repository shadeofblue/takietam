# 242

class Solution:

    def map_string(self, s: str):
        smap = {}
        for c in s:
            smap.setdefault(c, 0)
            smap[c] += 1
        return smap

    def isAnagram(self, s: str, t: str) -> bool:
        return self.map_string(s) == self.map_string(t)


sol = Solution()

s = "anagram"
t = "nagaram"
print(f"{s=}, {t=}")
print(sol.isAnagram(s, t))


s = "rat"
t = "car"
print(f"{s=}, {t=}")
print(sol.isAnagram(s, t))
