class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0,1]
        if n < 2:
            return f[n]
        for i in range(2,n + 1):
            num = f[0]+ f[1]
            f[0] = f[1]
            f[1] = num
        return f[1]