class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for ch in s:
            if ch not in d:
                d[ch] = 0
            d[ch] += 1
        res = []
        arr = [(k,v) for k,v in d.items()]
        arr = sorted(arr, key = lambda x: x[1], reverse=True)
        for t in arr:
            for i in range(t[1]):
                res.append(t[0])
                
        return "".join(res)
            
        