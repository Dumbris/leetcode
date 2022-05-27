"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_list_dummy = Node(0)
        #orig_head = head
        node = head
        last_new_node = new_list_dummy
        #build new linked list
        while node:
            new_node = Node(node.val)
            last_new_node.next = new_node
            node.new_node = new_node
            node = node.next
            last_new_node = new_node
        #copy randon pointers  
        node = head
        while node:
            if node.random:
                #print(node.new_node.random.val)
                node.new_node.random = node.random.new_node
            node = node.next
        return new_list_dummy.next
            
        