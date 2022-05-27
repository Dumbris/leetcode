# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #move slow into cycle
        #calc lenght
        #set pointer2 into K nodes offset, pointer1 on head
        fast,slow = head, head
        cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                #found cycle
                cycle = True
                break
        if not cycle: return None
        
        counter = 1
        slow2 = slow.next
        while slow != slow2:
            slow2 = slow2.next
            counter += 1
        
        pointer1, pointer2 = head,head
        while counter > 0:
            pointer2 = pointer2.next
            counter -= 1
            
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1
        
        
        