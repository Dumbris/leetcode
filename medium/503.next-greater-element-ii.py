"""

        [1,3,2,4,3]. [4]  
         [3  4,  4,-1,4] ^

[1,2,1]. [2]
[2,-1,2]
"""
import math

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        max_pos = None
        max_val = -math.inf
        for i in range(len(nums)):
            if max_val < nums[i]:
                max_val = nums[i]
                max_pos = i
        stack = [max_val]
        nums[max_pos] = -1
        def calc(i):
            if nums[i] == max_val:
                nums[i] = -1
                stack[::] = [max_val]
                return
            while nums[i] >= stack[-1]:
                stack.pop()
            if nums[i] < stack[-1]:
                old_val = nums[i]
                nums[i] = stack[-1]
                stack.append(old_val)

        if max_pos > 0:
            for i in range(max_pos-1,-1,-1):
                calc(i)
        for i in range(len(nums)-1,max_pos,-1):
            calc(i)

        return nums
                 



