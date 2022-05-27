"""
* .insert(cat)
c, .insert(at)
a, .insert(t)
t, .insert()
"""


class Trie:

    def __init__(self, val:str = None):
        self.val = val
        #print(val)
        self.children = {}
        self.is_terminal = False
        

    def insert(self, word: str) -> None:
        if len(word) == 0:
            self.is_terminal = True
            return
        ch = word[0]
        node = None
        if ch in self.children:
            node = self.children[ch]
        else:
            node = Trie(ch)
            self.children[ch] = node
        node.insert(word[1:])
        #print(word[1:])
        
        

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.is_terminal
        ch = word[0]
        #print(ch, " in ", self.children)
        if ch in self.children:
            return self.children[ch].search(word[1:])
        return False
        

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True
        ch = prefix[0]
        if ch in self.children:
            return self.children[ch].startsWith(prefix[1:])
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)