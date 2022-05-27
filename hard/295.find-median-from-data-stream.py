
#from heapq import * 
import heapq 

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        heapq.heapify(self.max_heap)
        heapq.heapify(self.min_heap)
        
#max[2,1],min[]
    def addNum(self, num: int) -> None:
        if len(self.max_heap) == 0:
            heapq.heappush(self.max_heap, -num)
        else:
            if num > -self.max_heap[0]: #2  6
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
                
            if len(self.min_heap) > len(self.max_heap):
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
            elif len(self.min_heap) + 1 < len(self.max_heap):
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))


    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0])/2
        else:
            return -self.max_heap[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()