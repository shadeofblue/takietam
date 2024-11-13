# 383

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_map = {}
        for c in magazine:
            magazine_map.setdefault(c, 0)
            magazine_map[c] += 1

        ransomnote_map = {}
        for c in ransomNote:
            ransomnote_map.setdefault(c, 0)
            ransomnote_map[c] += 1
            needed = ransomnote_map[c]
            available = magazine_map.get(c, 0)
            if needed > available:
                # print(f"too little `{c}`-s, {needed=}, {available=}.")
                return False

        return True


s = Solution()

ransomNote = "a"
magazine = "b"
print(ransomNote, magazine)
print(s.canConstruct(ransomNote, magazine))

ransomNote = "aa"
magazine = "ab"
print(ransomNote, magazine)
print(s.canConstruct(ransomNote, magazine))

ransomNote = "aa"
magazine = "aab"
print(ransomNote, magazine)
print(s.canConstruct(ransomNote, magazine))

