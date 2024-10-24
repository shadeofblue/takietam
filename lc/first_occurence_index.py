class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hi = 0
        ni = 0
        si = -1
        while hi < len(haystack) and ni < len(needle):
            # print(f"{hi=}, {ni=}, {si=}, {haystack[hi]=}, {needle[ni]=}")
            if haystack[hi] != needle[ni]:
                if si >= 0:
                    ni = 0
                    hi = si + 1
                    si = -1
                else:
                    hi += 1
            else:
                if si < 0:
                    si = hi
                hi += 1
                ni += 1

        return si if ni == len(needle) else -1

haystack = "sadbutsad"
needle = "sad"
print(haystack, needle, Solution().strStr(haystack, needle))

haystack = "happybutsad"
needle = "sad"
print(haystack, needle, Solution().strStr(haystack, needle))


haystack = "leetcode"
needle = "leeto"
print(haystack, needle, Solution().strStr(haystack, needle))


haystack = "aaa"
needle = "aaaa"
print(haystack, needle, Solution().strStr(haystack, needle))
