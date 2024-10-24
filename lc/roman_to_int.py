# 13
class Solution:

    lookup = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def romanToInt(self, s: str) -> int:
        vout = 0
        p = None
        for d in reversed(s):
            v = self.lookup[d]
            if not p or p <= v:
                vout += v
            else:
                vout -= v
            p = v
        return vout



s = "III"
print(s)
print(Solution().romanToInt(s))

s = "LVIII"
print(s)
print(Solution().romanToInt(s))

s = "MCMXCIV"
print(s)
print(Solution().romanToInt(s))
