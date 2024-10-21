# 122
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # print(prices)
        # deltas = []
        # prev_p = None
        # for p in prices:
        #     if prev_p is None:
        #         deltas.append(0)
        #     else:
        #         deltas.append(p - prev_p)
        #     prev_p = p
        # print(deltas)
        max_profit = 0
        bi = None
        i = None
        for i in range(1, len(prices)):
            delta = prices[i] - prices[i - 1]
            if delta > 0 and bi is None:
                bi = i - 1
            if delta < 0  and bi is not None:
                si = i - 1
                profit = prices[si] - prices[bi]
                # print(f"{profit=}, {bi=}, {prices[bi]=}, {si=}, {prices[si]=}")
                max_profit += profit
                bi = None

        if bi is not None and i is not None:
            profit = prices[i] - prices[bi]
            # print(f"{profit=}, {bi=}, {prices[bi]=}, {i=}, {prices[i]=}")
            max_profit += profit

        return max_profit


prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))

prices = [1,2,3,4,5]
print(Solution().maxProfit(prices))

prices = [7,6,4,3,1]
print(Solution().maxProfit(prices))
