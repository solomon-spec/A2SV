class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = {}
        n = len(matrix)
        def isvalid(y):
            if y >= 0 and y < n: return True
            return False
        
        def dp(x,y):
            if not isvalid(y): return inf
            if x == n-1: return matrix[x][y]
            if (x,y) not in memo:
                memo[(x,y)] = min(dp(x+1,y-1),dp(x+1,y),dp(x+1,y+1)) + matrix[x][y]
            return memo[(x,y)]
        ans = inf
        for i in range(n):
            ans = min(ans,dp(0,i))
        return ans
            
            
            