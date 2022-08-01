import heapq
from collections import deque
 


class MinStack:

    def __init__(self):
        #stack = []
        self.stack = deque()
        self.h = []
        heapq.heapify(self.h)

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.h, val)
        
    def pop(self) -> None:
        val = self.stack.pop()
        self._heap_pop(val)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.h[0]
    
    def _heap_pop(self, val) -> None:
        i = self.h.index(val)
        self.h[i] = self.h[-1]
        self.h.pop()
        if i < len(self.h):
            heapq._siftup(self.h, i)
            heapq._siftdown(self.h, 0, i)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()