# 56
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Range:
    start: int
    end: int
    def __repr__(self):
        return f"({self.start})" if self.start == self.end else f"({self.start}->{self.end})"

    def overlaps(self, r: "Range") -> bool:
        return not (r.start > self.end or r.end < self.start)

    def merge(self, r: "Range") -> None:
        assert self.overlaps(r)
        self.start = min(self.start, r.start)
        self.end = max(self.end, r.end)

    @classmethod
    def from_list(cls, v: List[int]) -> "Range":
        return cls(v[0], v[1])

    def as_list(self) -> List[int]:
        return [self.start, self.end]

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals_in = sorted([Range.from_list(l) for l in intervals], key = lambda r: r.start)
        intervals_out: List[Range] = []

        for i in intervals_in:
            if intervals_out and intervals_out[-1].overlaps(i):
                intervals_out[-1].merge(i)
            else:
                intervals_out.append(i)

        return [i.as_list() for i in intervals_out]






class SolutionNaive:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals_out: List[Range] = []
        intervals_in = [Range.from_list(l) for l in intervals]

        while intervals_in:

            # print(f"{intervals_in=}\n{intervals_out=}")
            r_in = intervals_in.pop(0)
            unmerged: List[Range] = []
            merged: List[Range] = []

            while intervals_out:
                r_out = intervals_out.pop(0)
                if r_out.overlaps(r_in):
                    r_out.merge(r_in)
                    merged.append(r_out)
                else:
                    unmerged.append(r_out)

            if not merged:
                unmerged.append(r_in)

            # print(f" --- {merged=}\n --- {unmerged=}")

            intervals_out = unmerged
            while merged:
                r = merged.pop(0)
                intervals_in.insert(0, r)

        return [r.as_list() for r in intervals_out]


s = Solution()

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(intervals)
print(s.merge(intervals))

intervals = [[1,4],[4,5]]
print(intervals)
print(s.merge(intervals))
