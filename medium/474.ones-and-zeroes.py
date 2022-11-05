class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        s0 = []
        s1 = []
        cache = {}
        for s in strs:
            c = Counter(s)
            s0.append(s.count('0'))
            s1.append(s.count('1'))
            
        def f(i,_m,_n):
            #print(i,_m,_n)
            if _m < 0 or _n < 0:
                return -1
            if i >= len(strs):
                return 0
            if (i,_m,_n) in cache:
                return cache[(i,_m,_n)]
            
            res = max(f(i+1,_m-s0[i],_n-s1[i])+1, f(i+1,_m,_n))
            cache[(i,_m,_n)] = res
            return res 
        
        return f(0,m,n)
        
        