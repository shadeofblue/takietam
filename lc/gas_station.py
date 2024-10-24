# 134
from typing import List

class Solution1:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # print(gas)
        # print(cost)
        n = len(gas)
        s = 0
        i = 0
        t = 0
        f = 0
        while i < s + n and s < n:
            ii = i % n
            g = gas[ii]
            c = cost[ii]
            f += c
            t += g
            # print(f"{n=}, {s=}, {i=}, {ii=}, {g=}, {c=}, {t=}, {f=}")

            if f > t:
                s += 1
                i = s
                t = 0
                f = 0
                # print(f"not enough gas -> new: {i=}, {s=}, {t=}, {f=}")
            else:
                i += 1

        return s if s < n else -1


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # print(gas)
        # print(cost)
        n = len(gas)
        deltas = []
        sums = []
        sum = 0
        for i in range(n * 2):
            delta = gas[i % n] - cost[i % n]
            deltas.append(delta)
            sum += delta
            sums.append(sum)
        # print(deltas)
        # print(sums)

        s = 0
        lngdi = 0
        i = 0
        while i < s + n and s < n:
            gd = deltas[i]
            if gd < 0:
                lngdi = i
            g = deltas[s] + (sums[i] - sums[s])

            # print(f"{n=}, {s=}, {lngdi=}, {i=}, {(i % n)=} {gd=}, {g=}, {deltas[s]=}, {sums[i]=}, {sums[s]=}")
            if g < 0:
                s = lngdi + 1
                lngdi = s
                i = s
            else:
                i += 1

        return s if s < n else -1



gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(Solution().canCompleteCircuit(gas, cost))

gas = [2,3,4]
cost = [3,4,3]
print(Solution().canCompleteCircuit(gas, cost))


gas = [1,2,3,4,5,5,70]
cost = [2,3,4,3,9,6,2]
print(Solution().canCompleteCircuit(gas, cost))

gas = [4]
cost = [5]
print(Solution().canCompleteCircuit(gas, cost))

gas = [5]
cost = [4]
print(Solution().canCompleteCircuit(gas, cost))
