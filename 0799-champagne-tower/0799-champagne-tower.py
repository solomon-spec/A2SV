class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        memo = defaultdict(int)
        memo[(0,0)] = poured -1
        def dp(x,y):
            if y > x or y < 0: return 0
            if (x,y) not in memo:
                memo[(x,y)] = max(0,dp(x-1,y)/2) + max(0,dp(x-1,y-1)/2) -1
            return memo[(x,y)]
        return min(1,dp(query_row,query_glass) + 1)
        