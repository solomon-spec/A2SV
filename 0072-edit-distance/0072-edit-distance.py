class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dp(cur,target):
            if not target or not cur: return max(len(cur),len(target))
          
            state = (cur,target)
            if state not in memo:
                
                if cur[0] == target[0]: memo[state]= dp(cur[1:],target[1:])
                else:
                    memo[state] = min(dp(cur[1:],target),dp(cur,target[1:]),dp(cur[1:],target[1:])) + 1
                    
            return memo[state]
        return dp(word1,word2)
            