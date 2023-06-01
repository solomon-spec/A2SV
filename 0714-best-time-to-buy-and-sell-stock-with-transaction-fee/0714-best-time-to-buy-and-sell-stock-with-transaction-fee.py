class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        def dp(i,cur):
            if i==len(prices) - 1:
                if cur == 1: return prices[-1] - fee
                return 0
            state = (i,cur)
            if state not in memo:
                if cur == 1:
                    memo[state] = max(dp(i+1,0)+prices[i]-fee,dp(i+1,1))
                else: memo[state] = max(dp(i+1,1)-prices[i],dp(i+1,0))
            return memo[state]
        return dp(0,0)