import math

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        res = []
        for i in nums:
            if i not in h:
                h[i] = 1
            else:
                h[i] += 1
        print(h)
        for _ in range(k):
            _max = 1
            _max_k = list(h.keys())[0]
            for k,v in h.items():
                if v > _max:
                    _max = v
                    _max_k = k
            res.append(_max_k)
            del h[_max_k]
        return res
                
            
        