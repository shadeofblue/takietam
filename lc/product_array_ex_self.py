# 238
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # print(nums)
        cnt = nums[0]
        answer = [1]
        for i in range(1, len(nums)):
            answer.append(cnt)
            cnt *= nums[i]

        # print(answer)

        cnt = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            answer[i] *= cnt
            cnt *= nums[i]

        return answer


nums = [1,2,3,4]
print(Solution().productExceptSelf(nums))


nums = [-1,1,0,-3,3]
print(Solution().productExceptSelf(nums))



# [ ] [ ] [ ]
#
#
#
# 1   2   3   4   5   6   7
#
# cnt = 720
#
# cnt = 7
#
# __  1   2   6   24  120  720