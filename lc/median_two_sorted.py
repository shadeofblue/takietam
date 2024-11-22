# 4
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        l = l1 + l2
        cnt = 0
        mprev = m = None


        while cnt < l / 2 + 1:
            cnt += 1
            if not nums2:
                feeder = nums1
            elif not nums1:
                feeder = nums2
            else:
                feeder = nums1 if nums1[0] <= nums2[0] else nums2

            # print("---> ", cnt, feeder)
            mprev = m
            m = feeder.pop(0) if feeder else None

        if cnt != l / 2 + 1:
            return mprev

        return (mprev + m) / 2


s = Solution()

nums1 = [1,3]
nums2 = [2]
print(nums1)
print(nums2)
print(s.findMedianSortedArrays(nums1, nums2))

nums1 = [1,2]
nums2 = [3,4]
print(nums1)
print(nums2)
print(s.findMedianSortedArrays(nums1, nums2))

nums1 = []
nums2 = [1]
print(nums1)
print(nums2)
print(s.findMedianSortedArrays(nums1, nums2))

nums1 = []
nums2 = [1, 2]
print(nums1)
print(nums2)
print(s.findMedianSortedArrays(nums1, nums2))

nums1 = []
nums2 = [1, 2, 3]
print(nums1)
print(nums2)
print(s.findMedianSortedArrays(nums1, nums2))
