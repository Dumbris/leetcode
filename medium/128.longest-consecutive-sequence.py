class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        starts = []
        # identify starts
        for i in nums:
            if i not in nums_set:
                continue
            j = i
            while j in nums_set:
                nums_set.remove(j)
                j -= 1
                
            starts.append(j+1)
        #find ends
        nums_set = set(nums)
        res = 0
        for s in starts:
            j = s
            while j in nums_set:
                nums_set.remove(j)
                j += 1
            res = max(res, j - 1 - s + 1)
        return res
        