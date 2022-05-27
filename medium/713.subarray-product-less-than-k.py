class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        _prod = 1
        left = 0
        for right in range(len(nums)):
            _prod *= nums[right]
            while _prod >= k and left < right:
                _prod /= nums[left]
                left += 1
            if _prod < k:    
                res += right - left + 1
        return res