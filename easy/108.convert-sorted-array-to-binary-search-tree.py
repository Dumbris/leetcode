# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def getNode(nums1):
            if len(nums1) == 0:
                return
            lstLen = len(nums1)
            index = (lstLen - 1) // 2
            return TreeNode(nums1[index], getNode(nums1[:index]), getNode(nums1[index+1:]))
        return getNode(nums)  