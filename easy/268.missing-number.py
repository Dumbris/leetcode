"""
[3,0,1]
 ^
i,j
0,3

"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = max(nums)
        nums.append(n)
        i = 0
        while i < n:
            j = nums[i] #index
            if (nums[i] != nums[j]):
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        #print(nums)
        for i in range(len(nums)):
            if nums[i] != i:
                return i
                
        