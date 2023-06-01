class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def dp(x,y):
            if x == len(triangle) - 1:
                return triangle[x][y]
            if (x,y) not in memo:
                memo[(x,y)] = min(dp(x+1,y),dp(x+1,y+1))+ triangle[x][y]
            return memo[(x,y)]
        return dp(0,0)