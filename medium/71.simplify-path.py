"""
"/a/./b/../../c/"

[c]
"""

from collections import deque
 


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = deque()
        
        for item in path.split("/"):
            if len(item) == 0: #///
                continue
            if item == ".": # .
                continue
            if item == "..":
                if len(stack) > 0: stack.pop()
                continue
            stack.append(item)
            
        return "/" + "/".join(stack)