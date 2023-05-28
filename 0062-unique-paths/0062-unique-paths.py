class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = defaultdict(int)
        def dp(x,y):
            if x + y <= 1: return 1
            state = (x,y)
            if state not in memo:
                if x >= 1:memo[state] += dp(x-1,y)
                if y >= 1: memo[state] += dp(x,y-1)
            return memo[state]
        return dp(n-1,m-1)
                
        