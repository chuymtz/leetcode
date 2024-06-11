"""
youre a robber and you want to rob a house
the array is the amt of money in the house
the constraint is that you cannot rob adjacient hosues.


i dont think you can go back to a house you've skipped
you want to max the amt of money

[1,2,3,1] solution is 1+3=4

"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 =0, 0

        # [rob1, rob2,n, n+1]
        n= nums[0]
        for i, n in enumerate(nums):
            print(f"\n\n{i=} | robbing house with {n=}")
            print(f"{rob1=} {rob2=}")
            temp = max(n + rob1, rob2)
            print(f"{temp=}")
            rob1 = rob2
            rob2 = temp
            print(f"{rob1=} {rob2=}")

        return rob2

Solution().rob(nums = [1,2,3,1])




