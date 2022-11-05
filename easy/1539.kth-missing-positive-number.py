class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        last_n = arr[0]
        c = arr[0] - 1
        if c >= k:
            return k
        for i in range(1,len(arr)):
            if arr[i] == (last_n + 1):
                last_n = arr[i]
                continue
                
            if  c + arr[i] - (last_n + 1) < k: #2+11-8=5
                c += arr[i] - (last_n + 1)
                last_n = arr[i] #7
                continue
                
            elif c + arr[i] - (last_n + 1) >= k:
                #0 + 10 - 1+1 >= 5
                #8 >= 5
                return last_n + (k-c) #7+(5-2)
        return last_n + (k-c)
        
                
            
        
        