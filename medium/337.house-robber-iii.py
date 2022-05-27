# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0,0
            not_take_left, take_left = dfs(node.left)
            not_take_right, take_right = dfs(node.right)
            #take current node
            res_taken = node.val + not_take_left + not_take_right
            #not take current node, we have a choice
            res_not_taken = max(not_take_left, take_left) + max(not_take_right, take_right)
            return res_not_taken, res_taken
        not_taken, taken = dfs(root)
        return max(not_taken, taken)
                