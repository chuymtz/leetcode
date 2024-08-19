"""

given an int array nums, find the continguous subarray (containing at least one num) which has the largest sum and return its sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
output = 6

https://www.youtube.com/watch?v=5WZl3MMT0Eg&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&index=4

"""
from typing import List

nums = [-2,1,-3,4,-1,2,1,-5,4]


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currSum = 0
        
        n = nums[1]
        for n in nums:
            if currSum < 0:
                currSum = 0
            # the is just max([0,currSum])
            currSum += n
            maxSub = max(maxSub, currSum)
            print(maxSub)
        return maxSub
            
Solution().maxSubArray(nums)


