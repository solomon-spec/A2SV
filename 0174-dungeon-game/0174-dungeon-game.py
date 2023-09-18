class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dire = [(-1,0),(0,-1)]
        n = len(dungeon)
        m = len(dungeon[0])
        
        
        def is_valid(x,y):
            if 0 <= x < n and 0 <= y < m:
                return True
            return False
        ans = 0
        dp = [[1]*m for i in range(n)]
        dp[n-1][m-1] = max(1,-dungeon[n-1][m-1]+1)        
        
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if i == n-1 and j == m - 1: continue
                dp[i][j] = inf
                if is_valid(i+1,j): dp[i][j] = dp[i + 1][j]
                    
                if is_valid(i,j + 1):dp[i][j] = min(dp[i][j],dp[i][j + 1])
               
                if dungeon[i][j]  < 0:
                    dp[i][j] +=  -dungeon[i][j]
                else:
                    dp[i][j] = max(1,dp[i][j]-dungeon[i][j])
                print(dp[i][j])
        print(dp)
        return dp[0][0]
                
                