class Solution:
    dic = {}
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        if n > 0:
            if n % 2 == 0:
                return self.myPow(x*x,n//2)
            return x*self.myPow(x*x,(n-1)//2)
        
      
        return 1/(self.myPow(x,abs(n)))
        
    