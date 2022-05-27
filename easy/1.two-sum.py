class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {num:i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            need = target - num
            if need not in h:
                continue
            if i == h[need]:
                continue
            return [i, h[need]]
        