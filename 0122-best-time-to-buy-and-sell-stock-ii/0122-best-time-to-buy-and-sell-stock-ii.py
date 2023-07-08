class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought = [-prices[0]]
        notb = [0]
        for i in range(1,len(prices)):
            b =  max(bought[-1],notb[-1]-prices[i])
            n = max(bought[-1]+prices[i],notb[-1])
            bought.append(b)
            notb.append(n)
        return max(bought[-1],notb[-1])