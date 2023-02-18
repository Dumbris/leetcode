# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def f(node):
            if node:
                node_left = node.left
                node_right = node.right
                node.left = None
                node.right = None
                yield node
                yield from f(node_left)
                yield from f(node_right)
        prev = None
        for node in f(root):
            if prev:
                prev.right = node                
            prev = node