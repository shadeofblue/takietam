# 209
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        subarray_sum = 0
        min_len = None
        i = 0
        l = 0
        n = len(nums)
        while i < n:
            if subarray_sum < target:
                if i + l < n:
                    a = nums[i + l]
                    subarray_sum += a
                    if a >= target:
                        return 1
                    l += 1
                else:
                    break
            elif subarray_sum >= target:
                if not min_len or min_len > l:
                    min_len = l
                subarray_sum -= nums[i]
                i += 1
                if l > 0:
                    l -= 1

        return min_len or 0

target = 7
nums = [2,3,1,2,4,3]
print(target, nums)
print(Solution().minSubArrayLen(target, nums))


target = 4
nums = [1,4,4]
print(target, nums)
print(Solution().minSubArrayLen(target, nums))


target = 11
nums = [1,1,1,1,1,1,1,1]
print(target, nums)
print(Solution().minSubArrayLen(target, nums))
