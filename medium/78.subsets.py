#[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        i = 0
        res = [[]]
        while i < len(nums):
            res_length = len(res)
            for j in range(0, res_length):
                new_item = res[j].copy()
                new_item.append(nums[i])
                res.append(new_item)
            i += 1
        return res
            