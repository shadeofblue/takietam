# 121
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxfp = None
        max_future_prices = [None for _ in range(len(prices))]

        for s in range(len(prices) - 1, -1, -1):
            p = prices[s]
            if maxfp is None or maxfp < p:
                maxfp = p
            max_future_prices[s] = maxfp

        maxp = 0

        for b in range(len(prices) - 1):
            p = max_future_prices[b] - prices[b]
            if p > maxp:
                maxp = p

        return maxp


prices = [7,1,5,3,6,4]
print(prices)
print(Solution().maxProfit(prices))
