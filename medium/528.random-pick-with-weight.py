"""
1,1,1,1
0,1
"""
import random

class Solution:

    def __init__(self, w: List[int]):
        #normalize weights
        self.sum = sum(w)
        self.buckets = []
        s = 0
        for i in w:
            s += i
            self.buckets.append(s)
            

    def pickIndex(self) -> int:
        r = self.sum * random.random()
        for i,n in enumerate(self.buckets):
            if n >= r:
                return i
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()