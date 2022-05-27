# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res_head = ListNode()
        self._mergeTwoLists(l1,l2,res_head)
        return res_head.next
    
    def _mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode], res_tail: ListNode) -> Optional[ListNode]:
        #print(res_tail)
        if not l1 and not l2:
            return
        if not l1 and l2:
            res_tail.next = l2
            return
        if not l2 and l1:
            res_tail.next = l1
            return
        
        if l1.val <= l2.val:
            res_tail.next = l1
            self._mergeTwoLists(l1.next, l2, res_tail.next)
        else:
            res_tail.next = l2
            self._mergeTwoLists(l1, l2.next, res_tail.next)
            
        
        