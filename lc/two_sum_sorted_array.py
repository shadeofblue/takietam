# 167
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ai = 0
        bi = 1
        while ai < len(numbers) - 1:
            if bi >= len(numbers):
                ai += 1
                bi = ai + 1
                continue

            a = numbers[ai]
            b = numbers[bi]
            s = a + b
            # print(f"{ai=}: {a=}, {bi=}: {b=}, {s=}")
            if s == target:
                return [ai + 1, bi + 1]
            if s < target:
                if a == b:
                    ai += 1
                bi += 1
            else:
                ai += 1
                bi = ai + 1

numbers = [2,7,11,15]
target = 9
print(numbers)
print(target)
print(Solution().twoSum(numbers, target))

numbers = [2,3,4]
target = 6
print(numbers)
print(target)
print(Solution().twoSum(numbers, target))

numbers = [-1,0]
target = -1
print(numbers)
print(target)
print(Solution().twoSum(numbers, target))

numbers = [5,25,75]
target = 100
print(numbers)
print(target)
print(Solution().twoSum(numbers, target))
