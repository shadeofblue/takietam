# 290

class Solution:

    def wordgen(self, s: str):
        word = ""
        for c in s:
            if c != " ":
                word += c
                continue
            yield word
            word = ""
        yield word

    def wordPattern(self, pattern: str, s: str) -> bool:
        pmap = {}
        wmap = {}
        i = 0
        for word in self.wordgen(s):
            if i >= len(pattern):
                return False
            pc = pattern[i]
            pmap.setdefault(pc, word)
            wmap.setdefault(word, pc)
            if wmap[word] != pc or pmap[pc] != word:
                # print(f"mismatch @{i}, {wmap[word]} => {pc} / {pmap[pc]} => {word}")
                return False
            i += 1
        return i == len(pattern)


sol = Solution()

pattern = "abba"
s = "dog cat cat dog"
print(f"{pattern=}, {s=}")
print(sol.wordPattern(pattern, s))

pattern = "abba"
s = "dog cat cat fish"
print(f"{pattern=}, {s=}")
print(sol.wordPattern(pattern, s))

pattern = "aaaa"
s = "dog cat cat dog"
print(f"{pattern=}, {s=}")
print(sol.wordPattern(pattern, s))


