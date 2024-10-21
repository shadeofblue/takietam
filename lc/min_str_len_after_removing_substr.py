# 2696
#import re
from typing import List, Tuple

class Solution:
    pattern = "AB|CD"
    patterns = [
        "AB",
        "CD"
    ]

    def assert_legal(self, s: str):
        assert re.match("^[A-Z]+$", s)


    def search(self, s: str, start):
        try:
            f = min([f for f in [s.find(p, start) for p in self.patterns] if f >= 0])
            return f
        except ValueError:
            pass

    # def findmatches(self, s: str):
    #     start = 0
    #     matches: List[Tuple[int, int]] = []
    #     found = True
    #
    #     while found:
    #         #print("ss: ", s[start:])
    #         found = re.search(self.pattern, s[start:])
    #         if found:
    #             matches.append((found.span()[0]+start, found.span()[1]+start))
    #             start = found.span()[0]+1+start
    #     #print("matches", matches)
    #     return matches

    def findmatches2(self, s: str):
        start = 0
        matches: List[Tuple[int, int]] = []
        found = True

        while found:
            # print("ss: ", s[start:])
            found = self.search(s, start)
            if found is not None:
                matches.append((found, found+2))
                start = found+start+1
        # print("matches", matches)
        return matches

    def minLength(self, s: str, rl=0) -> int:
        # print("src: ", s, len(s), "rl: ", rl)
        # self.assert_legal(s)
        matches = self.findmatches2(s)
        if not matches:
            return len(s)

        candidates = [s[:m[0]] + s[m[1]:] for m in matches]
        # print("candidates: ", candidates)
        l = [self.minLength(c, rl+1) for c in candidates]
        return min(l)


s = Solution()
min_l = s.minLength("ABFCACDB")
print(min_l)