# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q = deque()
        q.append(root)
        level = 1
        while q:
            levelSize = len(q)
            for _ in range(levelSize):
                node = q.popleft()
                if not node:
                    continue
                if not node.left and not node.right:
                    return level
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            level += 1
        return level
        