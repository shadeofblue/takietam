#27

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = 0
        while i + n < len(nums):
            if nums[i] == val:
                nums[i] = nums[-1-n]
                n += 1
            else:
                i += 1

        return len(nums) - n

nums = [3,2,2,3]
s = Solution().removeElement(nums, 3)
print(s, nums)

nums = [0,1,2,2,3,0,4,2]
s = Solution().removeElement(nums, 2)
print(s, nums)
