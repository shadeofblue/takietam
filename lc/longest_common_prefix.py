# 14
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        i = 0
        while True:
            try:
                c = set(s[i] for s in strs)
                if len(c) > 1:
                    return prefix
                prefix += list(c)[0]
            except IndexError:
                return prefix
            i += 1

strs = ["flower","flow","flight"]
print(strs)
print(Solution().longestCommonPrefix(strs))


strs = ["dog","racecar","car"]
print(strs)
print(Solution().longestCommonPrefix(strs))
