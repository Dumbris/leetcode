class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        res = []
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                res.append(i)
        return res
            
        