class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        startWindow = 0
        cur_sum = 0
        for endWindow in range(len(nums)):
            cur_sum += nums[endWindow]
            while (cur_sum + k) < (endWindow - startWindow + 1):
                cur_sum -= nums[startWindow]
                startWindow += 1
            res = max(res, endWindow - startWindow + 1)
        return res