"""
[[1,3],[2,6],[8,10],[15,18]]

[[1,6],[8,10],[15,18]]
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        last_b, last_e = intervals[0] #1,3
        for b,e in intervals[1:]:
            if b <= last_e: #8,
                last_e = max(e,last_e) 
                continue
            res.append([last_b, last_e])
            last_b, last_e = b,e #8,10
        res.append([last_b, last_e])
        return res
                
            
            
            
            
        