# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, acc):
            if not node:
                return acc
            
            left_h = dfs(node.left, acc+1)
            right_h = dfs(node.right, acc+1)
            if (not left_h) or (not right_h):
                return None
            if abs(left_h - right_h) > 1:
                return None
            return max(left_h, right_h)
        
        return dfs(root, 1)