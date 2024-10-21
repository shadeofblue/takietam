# 189
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        buf = list()

        for ni in range(len(nums)):
            nri = ni - k
            buf.append(nums[nri])
            if nri >= 0:
                nums[nri] = buf[nri]

        for bi in range(k):
            bri = bi - k
            nums[bri] = buf[bri]


nums = [1,2,3,4,5,6,7]
print(nums)
Solution().rotate(nums, 3)
print(nums)

nums = [-1,-100,3,99]
print(nums)
Solution().rotate(nums, 2)
print(nums)

