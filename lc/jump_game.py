# 55
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mi = 0
        l = len(nums)
        for i in range(l):
            if mi >= l - 1:
                return True
            if i > mi:
                return False
            ji = i + nums[i]
            if ji > mi:
                mi = ji
        return mi >= l - 1



nums = [2,3,1,1,4]
print(nums)
print(Solution().canJump(nums))

nums = [3,2,1,0,4]
print(nums)
print(Solution().canJump(nums))
