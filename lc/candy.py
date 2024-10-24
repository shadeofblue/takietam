# 135
from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # print(ratings)
        l = len(ratings)
        candies = [1 for _ in range(l)]
        for i in range(1, l):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # print("intermediate ", candies)

        candy_cnt = candies[l - 1]
        for i in range(l - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
            candy_cnt += candies[i]

        # print(candies)
        return candy_cnt


ratings = [1,0,2]
print(Solution().candy(ratings))

ratings = [1,2,2]
print(Solution().candy(ratings))