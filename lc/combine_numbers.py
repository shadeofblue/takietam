# 77
from typing import List, Tuple

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def _combine(combination: Tuple[int, ...], nums: List[int]):
            # print(f"--- {combination=}, {nums=}")
            if len(combination) == k:
                yield combination
            else:
                for i in range(len(nums)):
                    new_combination = combination + (nums[i], )
                    new_nums = nums[i+1:]
                    yield from _combine(new_combination, new_nums)

        return list(_combine((), list(range(1, n + 1))))


s = Solution()

n = 4
k = 2
print(f"{n=}, {k=}")
print(s.combine(n, k))

n = 1
k = 1
print(f"{n=}, {k=}")
print(s.combine(n, k))
