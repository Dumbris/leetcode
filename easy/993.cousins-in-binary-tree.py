# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque()
        x_level, y_level = None, None
        x_parent, y_parent = None, None
        q.append((root, None))
        level = 0
        while q:
            #level
            levelSize = len(q)
            for _ in range(levelSize):
                node, parent = q.popleft()
                if node.val == x:
                    x_level = level
                    x_parent = parent
                if node.val == y:
                    y_level = level
                    y_parent = parent
                if (x_level and y_level) and (x_level == y_level) and (x_parent != y_parent):
                    return True
                if node.left: q.append((node.left, node))
                if node.right: q.append((node.right, node))
            level += 1
        return False