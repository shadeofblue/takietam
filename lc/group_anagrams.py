# 49
import string
from typing import Dict, List


class Solution:

    def worddict_hash(self, d: Dict[str, int]):
        return "".join([f"{char}{d.get(char, 0)}" for char in string.ascii_lowercase if char in d])

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: Dict[str, List[str]] = {}
        for word in strs:
            sdict = {}
            for c in word:
                sdict.setdefault(c, 0)
                sdict[c] += 1
            word_hash = self.worddict_hash(sdict)
            # print(word, word_hash)
            groups.setdefault(word_hash, [])
            groups[word_hash].append(word)

        return list(groups.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(strs)
print(Solution().groupAnagrams(strs))

strs = [""]
print(strs)
print(Solution().groupAnagrams(strs))

strs = ["a"]
print(strs)
print(Solution().groupAnagrams(strs))
