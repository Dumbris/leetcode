# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""

"""

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        seen = set()
        res = [None] * 100
        if not root:
            return []
        res[0] = root.val
        q = deque()
        q.append((root,0))
        
        while len(q) > 0:
            node, level = q.popleft()
            seen.add(node)
            res[level] = node.val
            if node.left and node.left not in seen:
                q.append((node.left, level+1))
            if node.right and node.right not in seen:
                q.append((node.right, level+1))
                
        return [r for r in res if r != None]

        