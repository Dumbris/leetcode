# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def len_(self, list_):
        c = 0
        while list_:
            list_ = list_.next
            c += 1
        return c
    
    def get_d(self, headA, headB):
        c1 = self.len_(headA)
        c2 = self.len_(headB)
        if c1 == c2:
            return 0, headA, headB
        elif c1 > c2:
            return c1 - c2, headA, headB
        elif c2 > c1:
            return c2 - c1, headB, headA
        
    def move_to_d(self, d, list_):
        for _ in range(d):
            list_ = list_.next
        return list_
        
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA:
            return None
        if not headB:
            return None
        d, big_list, small_list = self.get_d(headA, headB)
        
        big_list = self.move_to_d(d, big_list)
        print(d, big_list.val, small_list.val)
        while big_list and small_list:
            print(d, big_list.val, small_list.val)
            if big_list.val == small_list.val:
                print("!")
                return big_list
            big_list = big_list.next
            small_list = small_list.next
            print("loop")
        return None