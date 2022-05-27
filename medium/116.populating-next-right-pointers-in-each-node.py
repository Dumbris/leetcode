"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        return self._connect(root, None)
    
    def _connect(self, root: 'Node', _next: 'Node') -> 'Node':
        
        if not root:
            return None
        
        #print(root.val, _next)
        
        root.next = _next
        self._connect(root.left, root.right)
        self._connect(root.right, root.next.left if root.next else None) 
        
        return root

        