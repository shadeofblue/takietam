# 57
from dataclasses import dataclass
from typing import List

@dataclass
class Interval:
    start: int
    end: int

    @classmethod
    def from_list(cls, l: List[int]) -> "Interval":
        return cls(l[0], l[1])

    def as_list(self):
        return [self.start, self.end]

    def __str__(self):
        return f"({self.start}:{self.end})"

    def overlaps(self, i: "Interval"):
        return not (self.start > i.end or self.end < i.start)

    def merge(self, i: "Interval"):
        assert self.overlaps(i)
        self.start = min(self.start, i.start)
        self.end = max(self.end, i.end)


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = [Interval.from_list(l) for l in intervals]
        new_interval = Interval.from_list(newInterval)
        new_intervals: List[Interval] = []

        def handle_interval(i: Interval):
            if new_intervals and new_intervals[-1].overlaps(i):
                new_intervals[-1].merge(i)
            else:
                new_intervals.append(i)

        for i in intervals:
            if new_interval and i.start > new_interval.start:
                handle_interval(new_interval)
                new_interval = None
            handle_interval(i)

        if new_interval:
            handle_interval(new_interval)

        return [i.as_list() for i in new_intervals]


s = Solution()

intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(f"{intervals=}\n{newInterval=}")
print(s.insert(intervals, newInterval))

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(f"{intervals=}\n{newInterval=}")
print(s.insert(intervals, newInterval))

