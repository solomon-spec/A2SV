class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        n,m = len(word1),len(word2)
        def dp(w1,w2):
            if w1 >= n or w2>=m : return max(n-w1,m-w2)
          
            state = (w1,w2)
            if state not in memo:
                
                if word1[w1] == word2[w2]: memo[state]= dp(w1+1,w2+1)
                else:
                    memo[state] = min(dp(w1+1,w2),dp(w1,w2+1),dp(w1+1,w2+1)) + 1
                    
            return memo[state]
        return dp(0,0)
            