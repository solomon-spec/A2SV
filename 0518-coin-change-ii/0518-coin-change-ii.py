class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dic = defaultdict(int)
        for i in range(len(coins)):dic[(0,i)] = 1
        
        for amt in range(1,amount+1):
            for i in range(len(coins)-1,-1,-1):
                if amt - coins[i] >= 0:
                    dic[(amt,i)] += (dic[(amt-coins[i],i)] + dic[(amt,i+1)])
                else: dic[(amt,i)] += dic[(amt,i+1)]
        print(dic[2,1])
        return dic[(amount,0)]
            
                    
                