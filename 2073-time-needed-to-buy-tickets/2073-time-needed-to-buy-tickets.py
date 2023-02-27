class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        summ = 0
        num = tickets[k]
        
        for i in tickets[:k + 1]:
            summ = summ + i if i< num else summ + num
            
        if k + 1 == len(tickets):
            return summ
        
        for i in tickets[k + 1:]:
            summ = summ + i if i < num else summ + num - 1
            
        return summ