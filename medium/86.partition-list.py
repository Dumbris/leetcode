# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head_min = ListNode()
        head_max = ListNode()
        head_min_orig = head_min
        head_max_orig = head_max
        node = head
        while node:
            if node.val < x:
                head_min.next = node
                head_min = head_min.next
            else:
                head_max.next = node
                head_max = head_max.next
            node = node.next
        head_max.next = None
        head_min.next = head_max_orig.next
        return head_min_orig.next
        