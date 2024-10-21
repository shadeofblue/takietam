# 26

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w = 0
        r = 0
        v = None
        while r < len(nums):
            if v is None or nums[r] > v:
                v = nums[r]
                if w != r:
                    nums[w] = nums[r]
                w += 1
            r += 1

        return w



nums = [1,1,2]
s = Solution().removeDuplicates(nums)
print(s, nums)

nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution().removeDuplicates(nums)
print(s, nums)

