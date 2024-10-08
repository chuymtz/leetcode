"""
88. merge sorted arrays

given two sorted int arrs, nums1, nums2, merge nums2 INTO nums1 as one sorted arr
"""

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place  
 instead.
        """
        last = m + n - 1
        m -= 1
        n -= 1

        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[last] = nums1[m]
                m -= 1
            else:
                nums1[last] = nums2[n]
                n -= 1
            last-= 1

        # Handle remaining elements in nums2
        while n >= 0:
            nums1[last] = nums2[n]
            n -= 1
            last -= 1
        
        
        

nums1 = [1, 2,3,0,0,0]
nums2 = [2,5,6]

self = Sol(nums1, nums2)
self.merge()