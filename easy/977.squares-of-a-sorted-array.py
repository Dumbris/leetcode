class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left,right = 0,len(nums)-1
        res = []
        while left <= right:
            if abs(nums[left]) > abs(nums[right]): # 4 < 10, 4> 3
                res.append(nums[left]**2)
                left += 1
            else:
                res.append(nums[right]**2)
                right -= 1
        res.reverse()
        return res