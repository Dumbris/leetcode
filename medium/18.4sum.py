class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        nums.sort()
        def find_pair(nums, first, second, target):
            left = second + 1
            right = len(nums) - 1
            while left < right:
                sum4 = nums[first] + nums[second] + nums[left] + nums[right]
                if sum4 == target:
                    res.add((nums[first], nums[second], nums[left], nums[right]))
                if sum4 < target:
                    left += 1
                else:
                    right -= 1
                
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                find_pair(nums, i, j, target)
                
        return [list(item) for item in res]
            
        