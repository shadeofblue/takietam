# 274
from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # print(citations)

        histogram = {}
        for c in citations:
            histogram.setdefault(c, 0)
            histogram[c] += 1

        # print(histogram)

        h_keys = sorted([h for h in histogram.keys() if h > 0], reverse=True)

        # print(h_keys)

        num_articles = 0
        h = 0
        for h in h_keys:
            # print(f"-----{h=}, {histogram[h]=}, {num_articles=}")
            if num_articles >= h:
                return num_articles

            num_articles += histogram[h]

            if num_articles >= h:
                return h

        return min(num_articles, h)



citations = [3, 0, 6, 1, 5]
print(Solution().hIndex(citations))

citations = [1,3,1]
print(Solution().hIndex(citations))

citations = [100]
print(Solution().hIndex(citations))

citations = [4,4,0,0]
print(Solution().hIndex(citations))

citations = [1,7,9,4]
print(Solution().hIndex(citations))
