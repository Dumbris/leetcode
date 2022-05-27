import heapq

"""
[1,3,-1,-3,5,3,6,7]
3

[] , []
max, min
"""
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        max_heap = []
        min_heap = []
        heapq.heapify(max_heap)
        heapq.heapify(min_heap)
        
        res = []
        
        def balance():
            if len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            elif len(max_heap) < len(min_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
        
        def addNum(num:int):
            if len(max_heap) == 0 or num <= -max_heap[0]:
                heapq.heappush(max_heap, -num)
            else:
                heapq.heappush(min_heap, num)
            balance()
        
        def getMedian():
            if len(max_heap) == len(min_heap):
                return (-max_heap[0] + min_heap[0]) / 2
            else:
                return -max_heap[0]
        left = 0    
        for right in range(len(nums)):
            addNum(nums[right])
            
            if right+1 > k:
                if nums[left] <= -max_heap[0]:
                    max_heap.remove(-nums[left])
                    heapq.heapify(max_heap)
                else:
                    min_heap.remove(nums[left])
                    heapq.heapify(min_heap)
                balance()
                left += 1
            
            if right+1 >= k:
                #get median
                #print(max_heap, min_heap)
                res.append(getMedian())
                
        return res
        