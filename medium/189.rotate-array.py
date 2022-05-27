"""
[1,2,3,4,5,6,7] -> [7,1,2,3,4,5,6] -> [6,7,1,2,3,4,5]

1) Using queue
2) Python slices
3) swap elements

reverse

[1,2,3,4,5,6,7]
[7,6,5, 4,3,2,1]

[5,6,7,1,2,3,4]<-

[4,3,2,1, 7,6,5]


-------------

[-1,-100,3,99]
[99,3, -100,-1]
swap   swap

[3,99,-1,-100]  <-
"""


class Solution:
    def reverse(self, nums: List[int]) -> List[int]:
        print(nums)
        i,j = 0,len(nums)-1
        while i < j:
            nums[j], nums[i] = nums[i],nums[j]
            j -= 1
            i += 1
        return nums
            
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)
        
        i,j = 0,len(nums)-1
        while i < j:
            nums[j], nums[i] = nums[i],nums[j]
            j -= 1
            i += 1
        #reverse left part
        i,j = 0,k-1
        while i < j:
            nums[j], nums[i] = nums[i],nums[j]
            j -= 1
            i += 1
        #reverse right part
        i,j = k,len(nums)-1
        while i < j:
            nums[j], nums[i] = nums[i],nums[j]
            j -= 1
            i += 1
        