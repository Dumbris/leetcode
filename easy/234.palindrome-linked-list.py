# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #find middle
        fast,slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse second half
        dummy = ListNode()
        node = slow
        dummy.next = node
        prev = None
        while node:
            _next = node.next
            node.next = prev
            prev = node
            node = _next
        node1 = head
        node2 = prev
        while node1 and node2:
            if node1.val != node2.val:
                return False
            node1 = node1.next
            node2 = node2.next
            
        return True
        