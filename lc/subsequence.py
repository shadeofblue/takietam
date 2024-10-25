# 392

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si = 0
        ti = 0

        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                si += 1
            ti += 1

        return si == len(s)

s = "abc"
t = "ahbgdc"
print(s)
print(t)
print(Solution().isSubsequence(s, t))

s = "axc"
t = "ahbgdc"
print(s)
print(t)
print(Solution().isSubsequence(s, t))
