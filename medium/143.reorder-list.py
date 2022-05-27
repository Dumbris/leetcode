# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #1 -> 2 -> 3
        #None <- 1 <- ,
        def reverse(node):
            prev = None #
            while node:
                _next = node.next #2
                node.next = prev #none
                prev = node
                node = _next
            return prev
                
        
        fast, slow = head, head
        prev_slow = None
        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next
        if fast == slow: return head
        #unlink first part and first element from second part
        if prev_slow: prev_slow.next = None
        #slow is middle
        node2 = reverse(slow)
        #print(node2)
        node1 = head
        #print(node1)
        dummy = ListNode()
        dummy.next = node1
        c = 0
        #[1 2]
        #[4 3]
        #1 -> 4 -> 2 -> 3
        while node1 and node2:
            if c % 2 == 0:
                node1_next = node1.next #2
                node1.next = node2 #4
                node1 = node1_next #2
            else:
                node2_next = node2.next #3
                node2.next = node1 #2
                node2 = node2_next #3
            c += 1

        return dummy.next
        