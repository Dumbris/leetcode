class Node:
    def __init__(self, name, prev_node, next_node=None):
        self.name = name
        self.prev_node = prev_node
        self.next_node = next_node
        

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current_node = Node(homepage, None)
        

    def visit(self, url: str) -> None:
        old_node = self.current_node
        node = Node(url, self.current_node)
        old_node.next_node = node 
        self.current_node = node
        

    def back(self, steps: int) -> str:
        while steps > 0:
            if self.current_node.prev_node:
                self.current_node = self.current_node.prev_node
            steps -= 1
        return self.current_node.name
        

    def forward(self, steps: int) -> str:
        while steps > 0:
            if self.current_node.next_node:
                self.current_node = self.current_node.next_node
            steps -= 1    
        return self.current_node.name
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)