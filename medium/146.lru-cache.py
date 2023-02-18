from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.dq = deque()
        self.h = {}
        self.capacity = capacity
        
        

    def get(self, key: int) -> int:
        if key in self.h:
            #inx = dq.index(key)
            self.dq.remove(key)
            self.dq.appendleft(key)
            return self.h[key]
        else:
            return -1
            
        

    def put(self, key: int, value: int) -> None:
        if key in self.h:
            self.dq.remove(key)
        self.dq.appendleft(key)
        self.h[key] = value
        if len(self.dq) > self.capacity:
            key2 = self.dq.pop()
            del self.h[key2]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)