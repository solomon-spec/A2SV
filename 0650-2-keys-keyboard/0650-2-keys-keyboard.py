class Solution:
    def isPrime(self,n):
            if n == 1: return False
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return (i)
            return n
    def minSteps(self, n: int) -> int:
        if n == 1: return 0
        x = self.isPrime(n)
        if x == n:
            return n
        return x + self.minSteps(n//x)
    
        