"""
0,1,2,2,3
^ ^
0,1,0,1,1,2,2,3,3,4
  ^   ^         ^ ^   
move right until new number
swap left+1 and right
move left and right

[1,1,1,2]
   ^ ^
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nextnondub = 1
        for i in range(1,len(nums)): #0
            if nums[nextnondub-1] != nums[i]:
                nums[nextnondub] = nums[i]
                nextnondub += 1
        return nextnondub

            
        