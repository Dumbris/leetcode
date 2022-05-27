"""
[3,0,1]
   ^
[2,0,1]
 ^   
 
[1,0,2]
[0,1,2]
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        l = len(nums) #3
        while i < l:
            if nums[i] < l and nums[i] != i:
                #print(i, nums, nums[nums[i]], nums[i])
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]] #i1,i0 = 3,0 [0,3,1]
            else:
                i += 1
                
        for j in range(len(nums)):
            if nums[j] != j:
                return j
        return len(nums)
                