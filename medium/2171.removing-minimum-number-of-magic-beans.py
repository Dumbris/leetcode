import math

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        res = math.inf
        
        prefix = [0]
        s = sum(beans)
        left_sum = 0
        l = len(beans)
            
        for i,v in enumerate(beans):
            right_sum = s - left_sum - v
            right_diff = right_sum - v*((l-i)-1)
            diff = right_diff + left_sum
            res = min(res,diff)
            #print(i,v,right_sum,right_diff, diff, left_sum)
            left_sum += v
        return res
                
            
            
            
        