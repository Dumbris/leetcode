# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node, n):
            if not node:
                #res_max = max(res_max, n-1)
                return n
            return max(dfs(node.left, n+1), dfs(node.right, n+1))
        
        return dfs(root,0)