class Solution:
    def myPow(self, x: float, n: int) -> float:
        def f(x,n):
            if n == 1:
                return x
          
            if n % 2 == 0:
                res = f(x,n//2)
                res *= res
                return res
            else:
                res = f(x,n//2)
                res *= res
                res *= x
                return res
        if n == 0:
            return 1
        elif n < 0:
            return 1/f(x,-1*n)
        else:
            return f(x,n)