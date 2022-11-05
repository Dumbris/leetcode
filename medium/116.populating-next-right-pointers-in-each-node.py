"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        q = deque()
        q.append((root,0))
        last_node = root
        last_level = 0
        while q:
            node,level = q.popleft()
            if last_node != node:
                if last_level == level:
                    last_node.next = node
            last_node = node
            last_level = level
                    
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
        return root
            
            
        