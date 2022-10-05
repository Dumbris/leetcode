import heapq 

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []
        res = []
        c = 0
        seen = set()
        heapq.heapify(h)
        heapq.heappush(h, (nums1[0]+nums2[0], 0,0))
        while h and c < k and c < len(nums1) * len(nums2):
            d = heapq.heappop(h)
            #print(d[1], d[2])
            if (d[1], d[2]) in seen:
                continue
            res.append([nums1[d[1]], nums2[d[2]]])
            seen.add((d[1], d[2]))
            c += 1
            new1 = d[1]+1
            new2 = d[2]
            if new1 < len(nums1) and (new1,new2) not in seen:
                heapq.heappush(h, (nums1[new1]+nums2[new2], new1, new2))
            new1 = d[1]
            new2 = d[2]+1
            if new2 < len(nums2) and (new1,new2) not in seen:
                heapq.heappush(h, (nums1[new1]+nums2[new2], new1, new2))
            
            
        return res