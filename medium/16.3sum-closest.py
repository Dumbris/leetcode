class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = math.inf
        dist = math.inf
        for i in range(len(nums)):
            left, right = i+1, len(nums) - 1
            while left < right:
                _sum = nums[i] + nums [left] + nums[right]
                if abs(target - _sum) < dist:
                    res = _sum
                    dist = abs(target - _sum)
                if _sum > target:
                    right -= 1
                else:
                    left += 1
        return res
        