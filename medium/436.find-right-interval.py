from bisect import bisect_right

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        idx = {i[0]:e for e,i in enumerate(intervals)}
        start_arr = sorted([i[0] for i in intervals])
        res = []
        for i in intervals:
            if i[1] in idx:
                res.append(idx[i[1]])
                continue
            right = bisect_right(start_arr, i[1])
            if right != len(start_arr):
                res.append(idx[start_arr[right]])
            else:
                res.append(-1)
            
        return res
        