# 452
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Balloon:
    start: int
    end: int

    def __repr__(self):
        return f"({self.start}-{self.end})"

    @classmethod
    def from_list(cls, v: List[int]) -> "Balloon":
        assert v[1] >= v[0]
        return cls(v[0], v[1])

    def as_list(self):
        return [self.start, self.end]

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        balloons = sorted([Balloon.from_list(l) for l in points], key=lambda b: b.start)
        arrows = int(bool(balloons))
        min_end: Optional[int] = None

        for b in balloons:
            if min_end is not None and b.start > min_end:
                # print(f" >>---> {min_end}")
                arrows += 1
                min_end = None
            min_end = b.end if min_end is None else min(b.end, min_end)

        # print(f" >>---> {min_end}")

        return arrows

s = Solution()


points = [[10,16],[2,8],[1,6],[7,12]]
print(f"{points=}")
print(f"arrows={s.findMinArrowShots(points)}")

points = [[1,2],[3,4],[5,6],[7,8]]
print(f"{points=}")
print(f"arrows={s.findMinArrowShots(points)}")


points = [[1,2],[2,3],[3,4],[4,5]]
print(f"{points=}")
print(f"arrows={s.findMinArrowShots(points)}")
