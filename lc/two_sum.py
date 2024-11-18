# 1
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counterparts = {}
        for i in range(len(nums)):
            n = nums[i]
            counterpart = target - n
            c_idx = counterparts.get(counterpart, -1)
            if c_idx >= 0:
                return c_idx, i
            counterparts[n] = i



nums = [2,7,11,15]
target = 9
print(nums, target)
print(Solution().twoSum(nums, target))


nums = [3,2,4]
target = 6
print(nums, target)
print(Solution().twoSum(nums, target))


nums = [3,3]
target = 6
print(nums, target)
print(Solution().twoSum(nums, target))

