"""
88. merge sorted arrays

given two sorted int arrs, nums1, nums2, merge nums2 INTO nums1 as one sorted arr
"""

from typing import List

class Sol:
    def __init__(self,nums1: List[int], nums2: List[int]) -> None:
        self.nums1 = nums1
        self.nums2 = nums2
        self.n = len(self.nums2)
        self.m = len(self.nums1) - self.n
    def merge(self):
        m = self.m -1
        n = self.n-1
        # get index of last indx of 1
        last = m + n +1
        iter = 0
        while m >= 0 and n >=0:
            if self.nums1[m] > self.nums2[n]:
                self.nums1[last] = self.nums1[m]
                m-=1
            else:
                self.nums1[last] = self.nums2[n]
                n-=1
            print(self.nums1)
            print(iter)
            iter += 1
            last -= 1
        
        while n>=0:
            nums1[last] = nums2[n]
            n, last = n-1, last
        
        
        

nums1 = [1, 2,3,0,0,0]
nums2 = [2,5,6]

self = Sol(nums1, nums2)
self.merge()