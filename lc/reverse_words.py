# 151

class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        w = ""
        for c in s:
            if c == " ":
                if w:
                    words.append(w)
                    w = ""
            else:
                w += c
        if w:
            words.append(w)

        return " ".join([w for w in reversed(words)])

s = "the sky is blue"
print(s)
print(Solution().reverseWords(s))

s = "  hello world  "
print(s)
print(Solution().reverseWords(s))

s = "a good   example"
print(s)
print(Solution().reverseWords(s))
