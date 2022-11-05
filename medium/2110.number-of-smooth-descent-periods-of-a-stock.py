"""
[4,3,2,1]
4+3+2



[5,4,3,2,1]
5+4+3+2
"""


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        start = 0
        prev = prices[start]
        count = 1
        res = 0
        
        def c(count):
            s = 0
            for i in range(count,0,-1):
                s += i
            #print(count, s)
            return s
        
        for end in range(1,len(prices)):
            #print(start,end,prev,count)
            if prev - prices[end] == 1:
                count += 1
            else:
                res += c(count)
                count = 1
                start = end
            prev = prices[end]
        res += c(count)
        return res
                
        
        
        