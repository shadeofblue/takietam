# 58

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        p = " "
        for c in s:
            if c != " ":
                if p == " ":
                    l = 0
                l += 1
            p = c

        return l

s = "Hello World"
print(s)
print(Solution().lengthOfLastWord(s))

s = "   fly me   to   the moon  "
print(s)
print(Solution().lengthOfLastWord(s))

s = "luffy is still joyboy"
print(s)
print(Solution().lengthOfLastWord(s))
