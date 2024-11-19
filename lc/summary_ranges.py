# 228
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Range:
    start: int
    end: int

    def __str__(self):
        return f"{self.start}" if self.start == self.end else f"{self.start}->{self.end}"

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges: List[Range[int, int]] = []
        range: Optional[Range] = None

        for n in nums:
            if not range or range.end != n - 1:
                if range:
                    ranges.append(range)
                range = Range(n, n)
            else:
                range.end += 1

        if range:
            ranges.append(range)

        return [str(r) for r in ranges]


s = Solution()


nums = [0,1,2,4,5,7]
print(nums)
print(s.summaryRanges(nums))

nums = [0,2,3,4,6,8,9]
print(nums)
print(s.summaryRanges(nums))
