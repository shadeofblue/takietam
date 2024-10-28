# 3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        i = 0
        j = 0
        maxlen = 0
        while i + maxlen < len(s):
            c = s[j]
            # print(f"{i=}, {j=}, {c=}, {maxlen=}, {chars=}, {s=}")
            try:
                prev_i = chars[c]
                if prev_i >= i:
                    i = prev_i + 1
                chars[c] = j
                j = max(i + 1, j + 1)
                l = j - i #+ (1 if j < maxlen and s[i] != s[j] else 0)
            except KeyError:
                chars[c] = j
                j += 1
                l = j - i

            if l > maxlen:
                maxlen = l

            # print(f"--- {i=}, {j=}, {c=}, {l=}, {maxlen=}, {chars=}, {s=}")

        return maxlen



s = "abcabcbb"
print(s)
print(Solution().lengthOfLongestSubstring(s))

s = "bbbbb"
print(s)
print(Solution().lengthOfLongestSubstring(s))

s = "pwwkew"
print(s)
print(Solution().lengthOfLongestSubstring(s))

s = "pwwke"
print(s)
print(Solution().lengthOfLongestSubstring(s))

s = " "
print(s)
print(Solution().lengthOfLongestSubstring(s))

s = "dvdf"
print(s)
print(Solution().lengthOfLongestSubstring(s))
