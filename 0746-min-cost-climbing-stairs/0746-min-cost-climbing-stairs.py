class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        dic = {}
        def dp(n):
            if n < 2:
                return cost[n]
            if n not in dic:
                dic[n] = min(dp(n-1) + cost[n],dp(n - 2)+cost[n])
            return dic[n]
        return dp(len(cost)-1)