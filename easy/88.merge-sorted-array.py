"""
[1,2,2,0,0,0] ,  [3,5,6]


[1,2,3,*0,*0,0] ,  [2,*5,6]


----
[1,2,7,0,0,0] ,  [*2,5,6]

[1,2,2,3,*0,0] ,  [*4,5,6]




Output: [1,2,2,3,4,5,6]


        
[1,2,3,7,10,0,0] [2,5,*6]

7, 10
"""

import math
import heapq

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j = 0,0
    
        heap = [math.inf]
        
        heapq.heapify(heap)
        
        while i < m+n:
            if i < m:
                if j < n and nums2[j] <= heap[0]:
                    #work with nums2
                    if nums1[i] > nums2[j]:
                        #use nums2
                        heapq.heappush(heap,nums1[i])
                        nums1[i] = nums2[j]
                        j += 1
                else:
                    #work with q
                    if nums1[i] > heap[0]:
                        _min = heapq.heappop(heap)
                        heapq.heappush(heap,nums1[i])
                        nums1[i] = _min
            else:
                if j < n and nums2[j] <= heap[0]:
                    nums1[i] = nums2[j]
                    j += 1
                else:
                    nums1[i] = heapq.heappop(heap)

                
            i += 1
                