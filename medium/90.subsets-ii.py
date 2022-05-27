[1,2,2]

[], [1], [1,2]

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        res = [[]]
        last_length = 0
        while i < len(nums):
            res_length = len(res)
            start = last_length if i > 0 and nums[i] == nums[i-1] else 0
            for j in range(start, res_length):
                new_item = list(res[j])
                new_item.append(nums[i])
                res.append(new_item)
            last_length = res_length
            
            i += 1
        return res