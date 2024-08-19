"""

"""


class Solution:
    def twoSumII(self, nums, target):
        
        for i, (a, b) in enumerate(zip(nums[:-1], nums[1:])):
            s = a+b
            print(f"{i=} | a+b = {a}+{b} = {s}")
            if s == target: 
                break
        
        return None
    

class Solution2:
    def twoSumII(self, nums, target):
        
        l, r = 0, len(nums)-1
        while l < r:
            a = nums[l]
            b = nums[r]
            curSum = a + b
            if curSum < target:
                l += 1
            elif curSum >target:
                r -= 1
            else:
                break
            print(f"{l=} | {r=} | a+b = {a} + {b} = {curSum}")
        return l, r, curSum


nums = [1, 3, 4, 5, 7, 10, 11]
target = 9
Solution2().twoSumII(nums, target)
