def _display_aux(self):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    # No child.
    if self.right is None and self.left is None:
        line = '%s' % str(self)
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if self.right is None:
        lines, n, p, x = _display_aux(self.left)
        s = '%s' % str(self)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if self.left is None:
        lines, n, p, x = _display_aux(self.right)
        s = '%s' % str(self)
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(self.left)
    right, m, q, y = _display_aux(self.right)
    s = '%s' % self.val
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2



class IntervalTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.max = end
        self.left = None
        self.right = None
        
    def is_intersects(self, start, end):
        #print(self.start, start, self.end, end)
        # |-----| query
        #.   |-----| node
        #  |----------| query
        #.    |-----| node
        if start <= self.start and end > self.start: return True
        #      |-----| query
        #. |-----| node
        if (start >= self.start) and (start < self.end): return True
       
        return False

    def display(self):
        lines, *_ = _display_aux(self)
        for line in lines:
            print(line)


    
    
    def __repr__(self):
        return "[" + str(self.start) + ", " + str(self.end) + ", max(" + str(self.max) +")]"


class MyCalendar:

    def __init__(self):
        self.interval_tree = None
    
        
    def insert(self, parent_node: IntervalTreeNode, start: int, end: int):    
        if start < parent_node.start:
            #go left
            if parent_node.left:
                self.insert(parent_node.left, start, end)
            else:
                parent_node.left = IntervalTreeNode(start,end)
        else:
            if parent_node.right:
                self.insert(parent_node.right, start, end)
            else:
                parent_node.right = IntervalTreeNode(start,end)
    
    def update_max(self, node: IntervalTreeNode) -> int:
        if not node:
            return -1
        node.max = max(node.end, self.update_max(node.left), self.update_max(node.right))
        return node.max
    
    def search(self, node: IntervalTreeNode, start: int, end: int):
        x = node
        while x:
            if x.is_intersects(start, end): 
                return True
            elif not x.left:
                x = x.right
            elif x.left.max < start:
                x = x.right
            else:
                x = x.left
        return False
        
    def book(self, start: int, end: int) -> bool:
        if not self.interval_tree:
            self.interval_tree = IntervalTreeNode(start,end)
            return True
        #search
        res = self.search(self.interval_tree, start, end)
        #insert
        if not res:
            self.insert(self.interval_tree, start, end)
            self.update_max(self.interval_tree)
            #self.interval_tree.display()
        return not res
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)