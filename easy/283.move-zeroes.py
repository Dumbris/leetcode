"""
[0,1,0,3,12]



zeros ids

[1,0,3,12,0]


[1,3,12,0,0] <--
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z_count = 0
        l = len(nums)-1
        i = 0
        while i <= l: 
            if nums[i] == 0:
                z_count += 1
            else:
                nums[i-z_count] = nums[i] #1-1=1,3-2=3,
            i += 1
        
        i = l - z_count + 1
        while i <= l:
                nums[i] = 0
                i += 1
            
            
        
        
        