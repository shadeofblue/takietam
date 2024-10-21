# 45
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = [None for _ in range(n)]
        cur_i = 0
        if n > 0:
            jumps[cur_i] = 0

        while cur_i < n:
            max_jump = nums[cur_i]
            for jump_i in range(1, max_jump + 1):
                dest_i = cur_i + jump_i
                # print(f"{n=}, {cur_i=}, {jump_i=}, {jumps=}, {nums=}")
                jump_n = jumps[cur_i] + 1
                if dest_i < n:
                    if jumps[dest_i] is None or jumps[dest_i] > jump_n:
                        jumps[dest_i] = jump_n
            cur_i += 1

        return jumps[n - 1]


nums = [2,3,1,1,4]
print(Solution().jump(nums))

nums = [2,3,0,1,4]
print(Solution().jump(nums))

