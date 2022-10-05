from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        l = len(s)
        c = Counter(s)        
        while l >= 0:     
            for top in c.most_common(2):
                if top[1] > 0:
                    if len(res) > 0 and res[-1] == top[0]:
                        return ""
                    res.append(top[0])
                    c[top[0]] -= 1
            l -= 2            
        return "".join(res)
                
        