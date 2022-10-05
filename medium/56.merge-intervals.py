

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        last_start = intervals[0][0]
        last_end = intervals[0][1]
        current_int = []
        for i in intervals:
            start = i[0]
            end = i[1]
            if last_end < start:
                current_int.append(last_start)
                current_int.append(last_end)
                res.append(current_int)
                current_int = []
                last_start = start
            last_end = max(end, last_end)
        current_int.append(last_start)
        current_int.append(last_end)
        res.append(current_int)
        return res
                