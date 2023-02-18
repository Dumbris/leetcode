from collections import defaultdict

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        h = {}
        stack = []
        for i,ch in enumerate(s):
            h[ch] = i
        for i,ch in enumerate(s):
            if ch in set(stack):
                continue
            if not stack:
                stack.append(ch)
                continue 
            if ch > stack[-1]:
                stack.append(ch)
            else: 
                while len(stack) > 0 and ch < stack[-1] and h[stack[-1]] > i:
                    stack.pop()
                stack.append(ch)
        return "".join(stack)
            
#ebcabc
"""
cbacdcbc
a = 2
b = 6
c = 7
d = 4

a,c,d,b
if cur > peak: push

"""


