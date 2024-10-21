# 88
from typing import List

class Solution_:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1 = i2 = 0
        while i1 < m + n and i2 < n:
            if nums1[i1] >= nums2[i2] or i1 - i2 >= m:
                nums1.insert(i1, nums2[i2])
                nums1.pop(-1)
                i2 += 1
            i1 += 1

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # print("----------")
        i1 = m - 1
        i2 = n - 1
        i = m + n - 1
        while i >= 0:
            # print(i, i1, i2, nums1, nums2)
            if i1 < 0 or (i2 >= 0 and nums1[i1] < nums2[i2]):
                # print("from n2")
                nums1[i] = nums2[i2]
                i -= 1
                i2 -= 1
            else:
                # print("from n1")
                nums1[i] = nums1[i1]
                i -= 1
                i1 -= 1



nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3

Solution().merge(nums1, m, nums2, n)
print(nums1)

nums1 = [1]
nums2 = []
m = 1
n = 0

Solution().merge(nums1, m, nums2, n)
print(nums1)

nums1 = [2,0]
nums2 = [1]
m = 1
n = 1
Solution().merge(nums1, m, nums2, n)
print(nums1)
