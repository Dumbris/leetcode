# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    3
9       20
    15      7
"""


from collections import defaultdict
    
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        m = defaultdict(list)
        def dfs(node: TreeNode, cur_coord:int, cur_level:int, m: Dict):
            if not node:
                return
            m[cur_coord].append((cur_level, node.val)) 
            dfs(node.left, cur_coord-1, cur_level+1, m)
            dfs(node.right, cur_coord+1, cur_level+1, m)
            
        dfs(root, 0, 0, m)
        
        res = []
        for _,v in sorted(m.items()):
            res.append([i[1] for i in sorted(v, key=lambda x: x[0])])
        
        return res
            
        