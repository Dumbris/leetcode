from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        g = defaultdict(list)
        g2 = defaultdict(list)
        for person, trustee in trust:
            g[person].append(trustee) #1(3,4) , 2(3,4), 4(3)
            g2[trustee].append(person) #3(1,2,4), 4(1,2), 2()
        
        
        candidates = [person for person in range(1,n+1) if len(g[person]) == 0]
        #print(g, g2, candidates)
        for c in candidates:
            if len(g2[c]) == n - 1:
                return c
        return -1
