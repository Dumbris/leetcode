import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        heapq.heapify(h)
        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(h,(dist,point))
        res = []    
        for i in range(k):
            res.append(heapq.heappop(h)[1])
        return res