# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#->#->
#<-#<-#
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        orig_head = head
        #1
        
        fast = head
        slow = head
        while fast:
            fast = fast.next.next
            slow = slow.next
        
        #print(slow.val)
        #reverse
        middle = slow
        node = slow
        prev = None
        _next = None
        while node:
            _next = node.next
            node.next = prev
            prev = node
            node = _next
            #prev = node
        #print(prev, node)
        _m = prev.val
        while prev:
            _m = max(_m, head.val+prev.val)
            head = head.next
            prev = prev.next
        return _m
        