# 128
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class NmapEntry:
    n: int
    prv: int = 0
    nxt: int = 0

    @property
    def length(self):
        return self.prv + self.nxt + 1

    def __str__(self):
        return f"n={self.n}, prv={self.prv}, nxt={self.nxt}, length={self.length}"

from typing import Dict, List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nmap = {}
        done = set()
        maxl = 0
        for num in nums:
            if num in done:
                continue
            done.add(num)
            plength = nmap.get(num - 1, 0)
            nlength = nmap.get(num + 1, 0)
            length = plength + nlength + 1
            p = num - plength
            n = num + nlength
            if p not in nmap or nmap.get(p) < length:
                nmap[p] = length
            if n not in nmap or nmap.get(n) < length:
                nmap[n] = length

            # print(num, nmap)
            maxl = max([maxl, length])

        return maxl

    def longestConsecutiveSort(self, nums: List[int]) -> int:
        nums = sorted(nums)
        prev_n = None
        l = 0
        maxl = 0
        for i in range(len(nums)):
            n  = nums[i]
            if prev_n is None or n - prev_n > 1:
                if l > maxl:
                    maxl = l
                l = 1
                prev_n = n
            elif n - prev_n == 1:
                l += 1
                prev_n = n
        return max([l, maxl])

    def longestConsecutiveWtf(self, nums: List[int]) -> int:
        nmap: Dict[int, NmapEntry] = {}
        for i in range(len(nums)):
            nmap.setdefault(nums[i], NmapEntry(nums[i]))

        for ne in nmap.values():
            nec = ne
            while True:
                nmap_prev = nmap.get(nec.n - 1)
                # print(f"--- prev --- {nec=}, {nmap_prev=}")
                if not nmap_prev:
                    break
                nec.prv = max([nec.prv, nmap_prev.prv + 1])
                if nmap_prev.nxt >= nec.nxt + 1:
                    break
                nmap_prev.nxt = nec.nxt + 1
                nec = nmap_prev

        for ne in nmap.values():
            nec = ne
            while True:
                nmap_next = nmap.get(nec.n + 1)
                # print(f"--- next --- {nec=}, {nmap_next=}")
                if not nmap_next:
                    break
                nec.nxt = max([nec.nxt, nmap_next.nxt + 1])
                if nmap_next.prv >= nec.prv + 1:
                    break
                nmap_next.prv = nec.prv + 1
                nec = nmap_next

        # for n in sorted(nmap.keys()):
        #     print(nmap.get(n))
        #
        return max([ne.length for ne in nmap.values()] + [0])


s = Solution()
nums = [100,4,200,1,3,2]
print(nums)
print(s.longestConsecutive(nums))

nums = [0,3,7,2,5,8,4,6,0,1]
print(nums)
print(s.longestConsecutive(nums))

nums = [-4,-1,4,-5,1,-6,9,-6,0,2,2,7,0,9,-3,8,9,-2,-6,5,0,3,4,-2]
print(nums)
print(s.longestConsecutive(nums))
