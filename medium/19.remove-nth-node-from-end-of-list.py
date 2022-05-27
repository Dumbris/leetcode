# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        head_p = dummy
        node_n = dummy
        lag = 0
        while head_p:
            if lag <= n:
                lag += 1
            else:
                node_n = node_n.next
            head_p = head_p.next

        node_n.next = node_n.next.next
       
        return dummy.next
            
        