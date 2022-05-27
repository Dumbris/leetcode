"""
[2,0,2,1,1,0]

[2,0,1]
[1,0,2]
[]
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else: #nums[i] == 2
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
    
        