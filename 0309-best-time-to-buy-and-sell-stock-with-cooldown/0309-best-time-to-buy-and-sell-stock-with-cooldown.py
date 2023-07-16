class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought = -prices[0]
        sale = 0
        prev = 0
        for i in range(1,len(prices)):
            bought = max(bought,prev-prices[i])
            prev = max(prev,sale)
            sale = max(sale,bought+prices[i])
        return sale