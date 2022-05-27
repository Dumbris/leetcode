# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.l = 10**4
        self.head = head
        

    def getRandom(self) -> int:
        #r1 = random.randint(0, self.l)
        r1 = int(random.random() * self.l)
        return self._getNode(r1)

    def _getNode(self, i):
        c = 0
        node = self.head
        while node:
            if c == i:
                return node.val
            node = node.next
            c += 1
        self.l = c
        return self._getNode(i % self.l)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()