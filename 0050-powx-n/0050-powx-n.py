class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        if n > 0:
            var = self.myPow(x,n//2)
            if n % 2 == 0:
                return var*var
            var = self.myPow(x,(n-1)//2)
            return x*var*var
      
        return 1/(self.myPow(x,abs(n)))
        
    