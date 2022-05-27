# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head
        _next = head.next
        return self._reverseList(head, head.next)
        
    def _reverseList(self, head: Optional[ListNode], _next: Optional[ListNode]) -> Optional[ListNode]:
        #print(head)
        if not _next:
            return head
        second = _next.next
        
        _next.next = head
        
        if head.next == _next:
            head.next = None
        return self._reverseList(_next, second)
        