from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        h = defaultdict(int)
        h2 = defaultdict(int)
        for i,ch in enumerate(s):
            h[ch] += 1
            h2[ch] = i
        for k,v in h.items():
            if v == 1:
                return h2[k]
        return -1
