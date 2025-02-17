from typing import List, Tuple

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def _combine(candidates_remaining: Tuple[int, ...], combination: Tuple[int, ...] = (), combination_sum: int = 0) -> List[Tuple[int, ...]]:
            l = len(candidates_remaining)
            for i in range(l):
                c = candidates_remaining[i]
                new_sum = combination_sum + c
                new_combination = combination + (c, )
                if new_sum == target:
                    yield new_combination
                elif new_sum < target:
                    yield from _combine(candidates_remaining[i:], new_combination, new_sum)

        return [list(t) for t in _combine(tuple(candidates))]

s = Solution()

candidates = [2,3,6,7]
target = 7
print(f"{candidates=}, {target=}")
print(s.combinationSum(candidates, target))

candidates = [2,3,5]
target = 8
print(f"{candidates=}, {target=}")
print(s.combinationSum(candidates, target))

candidates = [2]
target = 1
print(f"{candidates=}, {target=}")
print(s.combinationSum(candidates, target))

