# 169
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counters = dict()
        max_v = None
        max = 0
        for v in nums:
            if v not in counters:
                c = 1
                counters[v] = 1
            else:
                c = counters[v]
                c += 1
                counters[v] = c
            if c > max:
                max = c
                max_v = v

        return max_v

nums = [3,2,3]
print(Solution().majorityElement(nums))

nums = [2,2,1,1,1,2,2]
print(Solution().majorityElement(nums))


