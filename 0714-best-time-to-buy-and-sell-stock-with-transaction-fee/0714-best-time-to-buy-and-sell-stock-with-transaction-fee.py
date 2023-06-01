class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = -prices[0]
        profit = 0
        n = len(prices)
        for i in range(1, n):
            cash = max(cash, profit - prices[i])
            profit =  max(profit, cash+prices[i]-fee)
            print(cash,profit)
        return profit
