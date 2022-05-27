class Solution:
    def fib(self, n: int) -> int:
        h = {}
        def f(n):
            if n < 2:
                return n
            if n in h:
                return h[n]
            f1 = f(n-1)
            h[n-1] = f1
            f2 = f(n-2)
            h[n-2] = f2
            return f1 + f2
        
        return f(n)
        