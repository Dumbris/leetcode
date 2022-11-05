from collections import defaultdict

"""

aba

aaaabab

a 1 0,  
b 1
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        c = 0
        startWindow = 0
        m = defaultdict(int)
        for ch in p:
            m[ch] += 1
        
        def check(m):            
            for k,v in m.items():
                if v != 0:
                    return False
            return True
                
        for endWindow in range(len(s)):
            ch = s[endWindow]
            if ch in m:
                m[ch] -= 1
            if (endWindow - startWindow) >= len(p):
                ch = s[startWindow]
                if ch in m:
                    m[ch] += 1
                startWindow += 1
            #print(m)
            if check(m):
                res.append(startWindow)
                
        return res
 
                
                
            
            
            