class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        knight_moves = [(1, 2), (2, 1), (-1, 2), (-2, 1),(1, -2), (2, -1), (-1, -2), (-2, -1)]
        
        def isvalid(x,y):
            if(x>=0 and x<n and y>=0 and y<n):
                return True
            return False
        memo = {}
        def dp(x,y,k):
            if not isvalid(x,y): return 0
            
            if k == 0:return 1
            state = (x,y,k)
            
            if state not in memo:
                inboard = 0
                for i,j in knight_moves:
                    inboard += dp(x+i,y+j,k-1)
                memo[state] = (inboard/8)
            
            return memo[state]
            
        return dp(row,column,k)

                
            