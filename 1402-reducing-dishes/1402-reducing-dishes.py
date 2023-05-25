class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        total = sum(satisfaction)
        index = None
        for i,val in enumerate(satisfaction):
            if total < 0: 
                total -= val
            else: 
                index = i
                break
        ans = 0
        if index == None: return ans
        for i in range(index,len(satisfaction)):
             ans += (i-index+1)*satisfaction[i]
        return ans