# 11
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        li = 0
        ri = n -1
        maxhl = 0
        maxhr = 0
        area_max = 0
        while li < ri:
            hl = height[li]
            hr = height[ri]

            if hl < maxhl:
                li += 1
                continue

            maxhl = hl

            if hr < maxhr:
                ri -= 1
                continue

            maxhr = hr

            h = min(hl, hr)
            a = ri - li
            area = h * a
            if area > area_max:
                area_max = area

            # print(f"{li=}, {ri=}, {hl=}, {hr=}, {h=}, {a=}, {area=}, {maxhl=}, {maxhr=}, {area_max=}")

            if hl < hr:
                li += 1
            else:
                ri -= 1

        return area_max


class SolutionSlow:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        li = 0
        maxhl = 0
        area_max = 0
        while li < n - 1:
            hl = height[li]
            if hl <= maxhl:
                li += 1
                continue

            ri = n - 1
            maxhr = 0
            while ri > li:
                hr = height[ri]
                if hr <= maxhr:
                    ri -= 1
                    continue

                h = min(hl, hr)
                a = ri - li
                area = a * h
                # print(f"{li=}, {ri=}, {hl=}, {hr=}, {h=}, {a=}, {area=}, {maxhl=}, {maxhr=}, {area_max=}")
                if area > area_max:
                    maxhl = hl
                    maxhr = hr
                    area_max = area

                ri -= 1
            li += 1
        return area_max






height = [1,8,6,2,5,4,8,3,7]
print(height)
print(Solution().maxArea(height))

height = [1,1]
print(height)
print(Solution().maxArea(height))
