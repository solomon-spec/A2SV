class Solution:
    def numSquares(self, n: int) -> int:
        @cache
        def dp(t):

            if t == 0: 
                return 0
            
            q = 1
            ans = inf
            while q*q <= t:
                ans = min(ans,dp(t-q*q)+1)
                q += 1
            return ans
        return dp(n)