import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        c = 0
        l = len(arr)
        h = []
        heapq.heapify(h)
        seen = set()
        heapq.heappush(h, (arr[0]/arr[l-1],0,l-1))
        while h and c < k:
            d = heappop(h)
            if (d[1],d[2]) in seen:
                continue
            c += 1
            if c == k:
                return [arr[d[1]], arr[d[2]]]
            seen.add((d[1],d[2]))
            new1, new2 = d[1]+1, d[2]
            if new1 < l: heapq.heappush(h, (arr[new1]/arr[new2],new1,new2)) 
            new1, new2 = d[1], d[2]-1
            if new2 >= 0: heapq.heappush(h, (arr[new1]/arr[new2],new1,new2)) 
        