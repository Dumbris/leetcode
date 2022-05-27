"""
1,3,5*,6
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = len(nums)
        i,j = 0,l
        while i<=j:
            m = i + ((j-i)//2)
            #print(m)
            if target == nums[m]:
                return m
            elif target < nums[m]:
                #left
                j = m
            else:
                #right
                i = m + 1
            #print(i,j)    
            if i == j:
                return j
            
            
                
        