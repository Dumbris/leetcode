import random

class RandomizedSet:

    def __init__(self):
        self.h = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.h:
            return False
        self.arr.append(val)
        i = len(self.arr) - 1
        self.h[val] = i
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.h: 
            return False
        i = self.h[val]
        #print(i)
        del self.h[val]
        if len(self.arr) == 1:
            self.arr = []
        elif len(self.arr) - 1 == i:
            self.arr.pop()
        else:
            last_el = self.arr.pop()
            #print(self.arr)
            #last_i = len(self.arr) - 1
            self.arr[i] = last_el
            self.h[last_el] = i
        return True

        

    def getRandom(self) -> int:
        return self.arr[int(random.random() * len(self.arr))]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()