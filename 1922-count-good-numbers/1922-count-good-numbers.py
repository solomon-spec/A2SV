class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = (10**9 + 7)
        def fn(a, n):
              if n == 0:
                return 1
              if n % 2 == 0:
                return fn(a*a % mod, n/2)
              return a * fn(a*a % mod, (n-1)/2)
        if n % 2 == 0:
            return fn(20,int(n/2)) % (10**9 + 7)
        else:
            return (5 * fn(20,n//2)) % (10**9 + 7)