"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        def in_order(node:'Node'):
            if not node:
                return
            
            yield from in_order(node.left)
            yield node
            yield from in_order(node.right)
            
        prev = None
        head = None
        for node in in_order(root):
            #print(prev, node.val)
            if prev:
                prev.right = node
                node.left = prev
            else:
                head = node
            prev = node
        head.left = prev
        prev.right = head
        return head
        