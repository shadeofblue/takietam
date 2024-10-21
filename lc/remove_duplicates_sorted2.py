# 80
from typing import List

class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        idx_d = 0
        idx_s = 0
        r = 0
        d = 0
        e = None

        while idx_s < len(nums):
            # print("----------")
            # print(f"{nums=}, {idx_s=}, {idx_d=}, {e=}, {d=}, {r=}")
            # import time
            # time.sleep(0.1)
            if nums[idx_s] > nums[idx_d]:
                # if e != nums[idx_d]:
                #     e = nums[idx_d]
                # if r <= 1:
                #     r += 1
                #     idx_d += 1
                # else:
                #     d += 1

                idx_d += 1
                nums[idx_d] = nums[idx_s]
                r = 0
            elif idx_s != idx_d:
                if r == 0:
                    r = 1
                    idx_d += 1
                    nums[idx_d] = nums[idx_s]
                else:
                    d += 1

            idx_s += 1
            # print(f"{nums=}, {idx_s=}, {idx_d=}, {e=}, {d=}, {r=}")

        return idx_s - d

nums = [1,1,1,2,2,3]
s = Solution().removeDuplicates(nums)
print(s, nums)

nums = [0,0,1,1,1,1,2,3,3]
s = Solution().removeDuplicates(nums)
print(s, nums)

nums = [1,1,1,1]
s = Solution().removeDuplicates(nums)
print(s, nums)
