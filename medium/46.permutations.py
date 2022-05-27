[1,2,3]



class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def helper(fixed,i): #[1],1
            if i == len(nums):
                res.append(fixed)
            for j in range(len(nums)):
                if nums[j] not in fixed:
                    helper(fixed + [nums[j]], i+1) 
        
        helper([],0)
        
        return res
        