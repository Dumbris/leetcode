"""
[[0,30],[5,10],[15,20]]
---------------------
    ------   -------
        --------
1    2.  3    3  2  1

10, 30, 
"""

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        res = 1
        h = []
        intervals.sort(key=lambda x: x[0])
        for i in intervals:
            heapq.heappush(h, i[1])
            if len(h) > 0:
                while h[0] <= i[0]:
                    heapq.heappop(h)
            res = max(res,len(h))
        return res
                
            
        