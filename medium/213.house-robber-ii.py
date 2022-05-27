"""
         [2,3,2]
[max(2,2),2,5,]  

House[1]-House[n-1] or House[2]-House[n]

"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        A = [0]*(len(nums)+1)
        A2 = [0]*(len(nums)+1) #First selected
        A[0] = 0
        A2[0] = 0
        A2[1] = nums[0] 
        A[1] = 0
        for i in range(2,len(A)-1):
            A[i] = max(A[i-2] + nums[i-1], A[i-1])
            A2[i] = max(A2[i-2] + nums[i-1], A2[i-1])            
        j = len(A)-1  
        #print(A,A2)
        A2[j] = A2[j-1]
        A[j] = A[j-2] + nums[j-1]  
        #print(A,A2)
        return max(A[-1],A2[-1])