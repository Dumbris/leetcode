"""
[0,1,2,4,4]
  [1,2,3,1]
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        A = [0]*(len(nums)+1)
        A[1] = nums[0]
        for i in range(2,len(A)):
            A[i] = max(A[i-2]+nums[i-1], A[i-1])
        return A[-1]
            
        