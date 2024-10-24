# 42
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # print("height       ", height)
        l = len(height)
        if l < 3:
            return 0
        water_level = [height[0]]
        for i in range(1, l):
            water_level.append(max(height[i], water_level[i - 1]))

        # print("intermediate ", water_level)

        water_level[l - 1] = height[l - 1]
        for i in range(l - 2, -1, -1):
            water_level[i] = min(
                max(height[i], water_level[i + 1]),
                water_level[i]
            )

        # print(f"{water_level=}")

        return sum([water_level[i] - height[i] for i in range(l)])

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height))

height = [4,2,0,3,2,5]
print(Solution().trap(height))
