# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, acc, path):
            if not node:
                return
            if not node.left and not node.right and acc+node.val == targetSum:
                res.append(path+[node.val])
                return
            dfs(node.left, acc+node.val, path+[node.val])
            dfs(node.right, acc+node.val, path+[node.val])

            
        dfs(root, 0, [])
        return res
                
        