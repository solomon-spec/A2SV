class Solution:
    def fib(self, n: int) -> int:
        """if n == 0 or n == 1:
            return n
        return self.fib(n-1) + self.fib(n - 2)"""
        if n < 2:
            return n
        num = [1,1]
        for i in range(2,n):
            cur  = num[0] + num[1]
            num[0] = num[1]
            num[1] = cur
        return num[1]
        