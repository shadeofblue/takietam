from typing import List, Tuple

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def _permute(permutation: Tuple[int, ...], remaining_nums: Tuple[int, ...]) -> List[Tuple[int, ...]]:
            if not remaining_nums:
                yield permutation
            else:
                l = len(remaining_nums)
                for i in range(l):
                    new_permutation = permutation + (remaining_nums[i], )
                    new_remaining = remaining_nums[0:i] + remaining_nums[i+1:l]
                    yield from _permute(new_permutation, new_remaining)

        return list([list(t) for t in _permute((), tuple(nums) )])

class SolutionList:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results: List[List[int]] = list()

        l = len(nums)
        if l == 1:
            return [nums]

        for i in range(l):
            prefix = [nums[i]]
            suffixes = self.permute(nums[0:i] + nums[i+1:l])
            for suffix in suffixes:
                results.append(prefix + suffix)

        return results


s = Solution()

nums = [1,2,3]
print(nums)
print(s.permute(nums))

nums = [0,1]
print(nums)
print(s.permute(nums))

nums = [1]
print(nums)
print(s.permute(nums))
