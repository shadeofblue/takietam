# 167
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        counterparts = dict()
        for i in range(n):
            v = numbers[i]
            cnt = target - v
            print(f"{cnt=}, {counterparts=}")

            if not cnt in counterparts:
                counterparts[v] = i
                continue

            return [counterparts[cnt] + 1, i +1]


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
