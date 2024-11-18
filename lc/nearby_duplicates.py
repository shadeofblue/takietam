# 219
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_idx = {}
        for i in range(len(nums)):
            n = nums[i]
            j = last_idx.get(n)
            if j is not None and i - k <= j:
                return True
            last_idx[n] = i
        return False


s = Solution()

nums = [1,2,3,1]
k = 3
print(f"{nums=}, {k=}")
print(s.containsNearbyDuplicate(nums, k))

nums = [1,0,1,1]
k = 1
print(f"{nums=}, {k=}")
print(s.containsNearbyDuplicate(nums, k))

nums = [1,2,3,1,2,3]
k = 2
print(f"{nums=}, {k=}")
print(s.containsNearbyDuplicate(nums, k))
