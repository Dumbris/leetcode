"""
[4,3,2,7,8,2,3,1]
 
7.     4

"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i, l = 0, len(nums)
        
        while i < l:
            j = nums[i] - 1 #3
            if j < l and nums[i] != nums[j]:
                nums[j], nums[i] = nums[i], nums[j] # 
            else:
                i += 1
                
        res = []    
        for k in range(len(nums)):
            if k + 1 != nums[k]:
                res.append(k+1)
        return res
                
        