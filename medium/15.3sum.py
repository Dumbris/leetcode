"""
[-1,0,1,2,-1,-4]
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        h = {n:i for i,n in enumerate(nums)}
        res = []
        seen = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                target = -1 * (nums[i] + nums[j]) #1
                if target in h and h[target] != i and h[target] != j:
                    a1,a2,a3 = nums[i],nums[j],nums[h[target]]
                    r = [a1,a2,a3]
                    r.sort()
                    if tuple(r) not in seen:
                        res.append(r)
                        seen.add(tuple(r))
        return res