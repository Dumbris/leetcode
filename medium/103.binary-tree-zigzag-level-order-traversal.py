# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)
        level = 0
        while q:
            levelSize = len(q)
            levelItems = []
            for _ in range(levelSize):
                node = q.popleft()
                if not node:
                    continue
                levelItems.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if level % 2 != 0:
                levelItems.reverse()
            if len(levelItems) > 0: res.append(levelItems)
            level += 1
        return res
        